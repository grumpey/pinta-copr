%global debug_package %{nil}

Name:		pinta
Version:	3.0.3
Release:  2%{?dist} 
Summary:	An easy to use drawing and image editing program

# the code is licensed under the MIT license while the icons are licensed as CC-BY
# Automatically converted from old format: MIT and CC-BY - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:		https://pinta-project.com/

Source0:	https://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:  dotnet-sdk-9.0
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires: hicolor-icon-theme
Requires: dotnet-runtime-9.0
Requires: libadwaita

Recommends: webp-pixbuf-loader

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q

%build
%configure --prefix=%{_prefix} 
%make_build

%install
%make_install

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%find_lang %name

%files -f %{name}.lang
%license license-mit.txt license-pdn.txt
%doc readme.md
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/icons/hicolor/16x16/actions/about-pinta.png
%{_datadir}/icons/hicolor/16x16/actions/addins-manage.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-autolevel.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-blackandwhite.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-curves.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-huesaturation.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-invertcolors.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-levels.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-posterize.png
%{_datadir}/icons/hicolor/16x16/actions/adjustments-sepia.png
%{_datadir}/icons/hicolor/16x16/actions/edit-selection-erase.png
%{_datadir}/icons/hicolor/16x16/actions/edit-selection-fill.png
%{_datadir}/icons/hicolor/16x16/actions/edit-selection-invert.png
%{_datadir}/icons/hicolor/16x16/actions/edit-selection-offset.png
%{_datadir}/icons/hicolor/16x16/actions/effects-artistic-inksketch.png
%{_datadir}/icons/hicolor/16x16/actions/effects-artistic-oilpainting.png
%{_datadir}/icons/hicolor/16x16/actions/effects-artistic-pencilsketch.png
%{_datadir}/icons/hicolor/16x16/actions/effects-blurs-fragment.png
%{_datadir}/icons/hicolor/16x16/actions/effects-blurs-gaussianblur.png
%{_datadir}/icons/hicolor/16x16/actions/effects-blurs-motionblur.png
%{_datadir}/icons/hicolor/16x16/actions/effects-blurs-radialblur.png
%{_datadir}/icons/hicolor/16x16/actions/effects-blurs-unfocus.png
%{_datadir}/icons/hicolor/16x16/actions/effects-blurs-zoomblur.png
%{_datadir}/icons/hicolor/16x16/actions/effects-distort-bulge.png
%{_datadir}/icons/hicolor/16x16/actions/effects-distort-dents.png
%{_datadir}/icons/hicolor/16x16/actions/effects-distort-frostedglass.png
%{_datadir}/icons/hicolor/16x16/actions/effects-distort-pixelate.png
%{_datadir}/icons/hicolor/16x16/actions/effects-distort-polarinversion.png
%{_datadir}/icons/hicolor/16x16/actions/effects-distort-tile.png
%{_datadir}/icons/hicolor/16x16/actions/effects-distort-twist.png
%{_datadir}/icons/hicolor/16x16/actions/effects-noise-addnoise.png
%{_datadir}/icons/hicolor/16x16/actions/effects-noise-median.png
%{_datadir}/icons/hicolor/16x16/actions/effects-noise-reducenoise.png
%{_datadir}/icons/hicolor/16x16/actions/effects-photo-glow.png
%{_datadir}/icons/hicolor/16x16/actions/effects-photo-redeyeremove.png
%{_datadir}/icons/hicolor/16x16/actions/effects-photo-sharpen.png
%{_datadir}/icons/hicolor/16x16/actions/effects-photo-softenportrait.png
%{_datadir}/icons/hicolor/16x16/actions/effects-photo-vignette.png
%{_datadir}/icons/hicolor/16x16/actions/effects-render-clouds.png
%{_datadir}/icons/hicolor/16x16/actions/effects-render-juliafractal.png
%{_datadir}/icons/hicolor/16x16/actions/effects-render-mandelbrotfractal.png
%{_datadir}/icons/hicolor/16x16/actions/effects-render-voronoidiagram.png
%{_datadir}/icons/hicolor/16x16/actions/effects-stylize-edgedetect.png
%{_datadir}/icons/hicolor/16x16/actions/effects-stylize-emboss.png
%{_datadir}/icons/hicolor/16x16/actions/effects-stylize-outline.png
%{_datadir}/icons/hicolor/16x16/actions/effects-stylize-relief.png
%{_datadir}/icons/hicolor/16x16/actions/help-bug.png
%{_datadir}/icons/hicolor/16x16/actions/help-translate.png
%{_datadir}/icons/hicolor/16x16/actions/image-flatten.png
%{_datadir}/icons/hicolor/16x16/actions/image-resize-canvas.png
%{_datadir}/icons/hicolor/16x16/actions/image-resize.png
%{_datadir}/icons/hicolor/16x16/actions/layer-import.png
%{_datadir}/icons/hicolor/16x16/actions/view-grid.png
%{_datadir}/icons/hicolor/16x16/actions/view-rulers.png
%{_datadir}/icons/hicolor/16x16/actions/view-zoom-100.png
%{_datadir}/icons/hicolor/16x16/actions/view-zoom-selection.png
%{_datadir}/icons/hicolor/16x16/actions/view-zoom-window.png
%{_datadir}/icons/hicolor/scalable/actions/adjustments-brightnesscontrast-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/edit-swap-vert-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/effects-default-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/help-website-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-flip-horizontal-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-flip-vertical-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-orientation-landscape-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-orientation-portrait-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-base-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-down-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-left-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-ne-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-nw-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-right-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-se-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-sw-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-resize-canvas-up-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-rotate-180-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-rotate-90ccw-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/image-rotate-90cw-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/layers-add-layer-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/layers-duplicate-layer-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/layers-merge-down-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/layers-move-layer-down-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/layers-move-layer-up-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/layers-remove-layer-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/layers-rotate-zoom-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-antialiasing-disabled-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-antialiasing-enabled-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-blending-normal-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-blending-overwrite-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-clonestamp-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-colorpicker-sampling-1x1-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-colorpicker-sampling-3x3-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-colorpicker-sampling-5x5-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-colorpicker-sampling-7x7-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-colorpicker-sampling-9x9-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-colorpicker-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-ellipse-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-eraser-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-fillstyle-background-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-fillstyle-fill-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-fillstyle-outline-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-fillstyle-outlinefill-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-freeformshape-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-colormode-color-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-colormode-transparency-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-conical-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-diamond-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-linear-reflected-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-linear-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-radial-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-gradient-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-line-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-move-cursor-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-move-selection-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-move-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-paintbrush-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-paintbucket-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-pan-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-pencil-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-recolor-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-rectangle-rounded-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-rectangle-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-select-ellipse-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-select-lasso-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-select-magicwand-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-select-rectangle-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-text-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/tool-zoom-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/ui-crop-to-selection-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/ui-cursor-location-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/ui-deselect-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/ui-historylist-symbolic.svg

%changelog
* Mon Sep 08 2025 Joe Walker <joe.c.walker0@gmail.com> - 3.0.3-2 
- RPM build of pinta 3.0.3 after fixing a few things  
