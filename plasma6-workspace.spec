# Not using mklibname here to avoid clashing with the package
# by the same name from plasma-workspace 5.x
# Change once we're removing P5.
%define devname %{name}-devel
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

# filter qml/plugins provides
%global __provides_exclude_from ^(%{_kde5_qmldir}/.*\\.so|%{_qt5_plugindir}/.*\\.so)$

Name: plasma6-workspace
Version: 6.0.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-workspace/-/archive/%{gitbranch}/plasma-workspace-%{gitbranchd}.tar.bz2#/plasma-workspace-%{git}.tar.bz2
%else
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/plasma-workspace-%{version}.tar.xz
%endif
Source1: kde.pam
Patch0: plasma-workspace-bump-sonames.patch
Patch1: plasma-workspace-set-QT_QPA_PLATFORM.patch
Patch2: sddm-breeze-add-missing-import.patch
Patch3: plasma-workspace-default-OM-wallpaper.patch
# FIXME this needs to be redone properly (OM theme)
# Patch3: plasma-workspace-5.8.0-use-openmandriva-icon-and-background.patch
Summary: The KDE Plasma workspace
URL: http://kde.org/
License: GPL
Obsoletes: simplesystray < %{EVRD}
Group: Graphical desktop/KDE
BuildRequires: cmake(Breeze)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaActivitiesStats)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(Wayland) >= 5.90.0
BuildRequires: cmake(KWayland) >= 5.90.0
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: pkgconfig(libnm) >= 1.4.0
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6People)
BuildRequires: cmake(KF6KDED)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(PlasmaQuick) >= 5.90.0
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Su)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6Screen)
BuildRequires: cmake(KF6Baloo)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KScreenLocker)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6QuickCharts)
BuildRequires: cmake(KF6UnitConversion)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6WaylandCompositor)
BuildRequires: cmake(LayerShellQt)
BuildRequires: cmake(WaylandProtocols)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(dbusmenu-qt6)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(libgps) >= 3.15
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(systemd)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6ShaderTools)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= 1.24
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pam-devel
BuildRequires: pkgconfig(iso-codes)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(PolkitQt6-1)
BuildRequires: cmake(AppStreamQt)
BuildRequires: pkgconfig(libudev)
BuildRequires: gettext
# for DBus interfaces
BuildRequires: plasma6-kwin
# Both Plasma 5 and Plasma 6 provide
# cmake(KPipeWire), cmake(KSysGuard) and friends
BuildRequires: cmake(KPipeWire) >= 5.27.80
BuildRequires: plasma6-kwin-devel
BuildRequires: cmake(KWinDBusInterface) >= 5.27.80
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: xdotool
# needed for backgrounds and patch 2
Requires: distro-release-theme
Requires: qt6-qttools-dbus
Requires: plasma6-kactivitymanagerd
Requires: kf6-qqc2-desktop-style
Requires: qt6-qtimageformats
Recommends: kf6-kimageformats
Provides: virtual-notification-daemon
%ifarch %{armx}
Requires: %{name}-wayland = %{EVRD}
%else
Requires: %{name}-backend = %{EVRD}
%endif
Requires: iso-codes
# Because of pam file
Conflicts: kdm < 2:4.11.22-1.1
Conflicts: kio-extras < 15.08.0
Obsoletes: %{mklibname plasma-geolocation-interface} = 5.240.0
Obsoletes: %{mklibname colorcorrect} = 5.240.0
Obsoletes: %{mklibname weather_ion} = 5.240.0
Obsoletes: %{mklibname taskmanager} = 5.240.0
Obsoletes: %{mklibname notificationmanager} = 5.240.0

%description
The KDE Plasma workspace.

%package -n %{devname}
Summary: Development files for the KDE Plasma workspace
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files for the KDE Plasma workspace.

%package -n plasma6-sddm-theme-breeze
Summary: KDE Breeze theme for the SDDM display manager
Group: Graphical desktop/KDE
Requires: plasma6-sddm

%description -n plasma6-sddm-theme-breeze
KDE Breeze theme for the SDDM display manager.

%package x11
Summary: X11 support for Plasma Workspace
Group: Graphical desktop/KDE
Provides: %{name}-backend = %{EVRD}
# needed if anything will fail on startkde
Requires: xmessage
Requires: xprop
Requires: xset
Requires: xrdb
Requires: iso-codes
Requires: plasma6-kwin-x11
Requires: kf6-kidletime-x11
Requires: plasma6-libkscreen-x11

%description x11
X11 support for Plasma Workspace.

%package wayland
Summary: Wayland support for Plasma Workspace
Group: Graphical desktop/KDE
Requires: %{name}
Provides: %{name}-backend = %{EVRD}
Requires: xwayland
Requires: plasma6-kwin-wayland
Requires: kf6-kidletime-wayland
Requires: plasma6-libkscreen-wayland
Recommends: plasma6-xdg-desktop-portal-kde

%description wayland
Wayland support for Plasma Workspace.

%prep
%autosetup -p1 -n plasma-workspace-%{?git:%{gitbranchd}}%{!?git:%{version}}
# (tpg) do not start second dbus user session
# see also https://invent.kde.org/plasma/plasma-workspace/-/merge_requests/128/diffs?commit_id=8475fe4545998c806704a45a7d912f777a11533f
sed -i -e 's/dbus-run-session //g' login-sessions/plasmawayland*.desktop.cmake

%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DINSTALL_SDDM_WAYLAND_SESSION:BOOL=On \
	-DPLASMA_SYSTEMD_BOOT=true \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/kde

# sddm breeze theme background
sed -i -e "s#^background=.*#background=%{_datadir}/mdk/backgrounds/OpenMandriva-splash.png#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf
sed -i -e "s#^type=.*#type=image#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf

# (tpg) fix autostart permissions
chmod 644 %{buildroot}%{_sysconfdir}/xdg/autostart/*

# FIXME as of Plasma 6 20230804 snapshot, mesa 23.2, VBox 7.0.10,
# Having the sddm wayland configuration installed crashes VBox and
# leaves the VM unusable.
# Use rootless X11 for the time being, even if we use plasma wayland.
rm %{buildroot}%{_sysconfdir}/sddm.conf.d/plasma-wayland.conf

# Bogus install of a test
rm -rf %{buildroot}%{_builddir}

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_bindir}/plasma-apply-colorscheme
%{_bindir}/plasma-apply-cursortheme
%{_bindir}/plasma-apply-desktoptheme
%{_bindir}/plasma-apply-lookandfeel
%{_bindir}/plasma-apply-wallpaperimage
%{_bindir}/plasma-shutdown
%{_sysconfdir}/xdg/autostart/gmenudbusmenuproxy.desktop
%{_sysconfdir}/xdg/autostart/org.kde.plasmashell.desktop
%{_sysconfdir}/xdg/autostart/xembedsniproxy.desktop
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_sysconfdir}/xdg/menus/plasma-applications.menu
%{_sysconfdir}/pam.d/kde
%{_bindir}/gmenudbusmenuproxy
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/krunner
%{_bindir}/ksmserver
%{_bindir}/ksplashqml
%{_bindir}/plasmashell
%{_bindir}/plasma_waitforname
%{_bindir}/plasmawindowed
%{_bindir}/plasma_session
%{_bindir}/xembedsniproxy
%{_bindir}/kde-systemd-start-condition
%{_libdir}/libkfontinst.so.*
%{_libdir}/libkfontinstui.so.*
%{_libdir}/libexec/baloorunner
%{_libdir}/libexec/ksmserver-logout-greeter
%dir %{_qtdir}/plugins/plasma
%dir %{_qtdir}/plugins/plasma/applets
%dir %{_qtdir}/plugins/kf6/krunner
%{_qtdir}/plugins/kf6/kded/*.so
%{_qtdir}/plugins/kf6/kio/*.so
%{_qtdir}/plugins/kf6/krunner/*.so
%{_qtdir}/plugins/plasma/containmentactions
%{_qtdir}/plugins/phonon_platform
%{_qtdir}/plugins/plasma/applets/*.so
%{_qtdir}/plugins/plasmacalendarplugins
%{_qtdir}/qml/org/kde/breeze
%{_qtdir}/qml/org/kde/colorcorrect
%dir %{_qtdir}/qml/org/kde/plasma/private
%{_qtdir}/qml/org/kde/plasma/private/brightnesscontrolplugin
%{_qtdir}/qml/org/kde/plasma/private/digitalclock
%{_qtdir}/qml/org/kde/plasma/private/shell
%{_qtdir}/qml/org/kde/plasma/private/sessions
%{_qtdir}/qml/org/kde/plasma/wallpapers
%{_qtdir}/qml/org/kde/plasma/workspace
%{_qtdir}/qml/org/kde/holidayeventshelperplugin
%{_qtdir}/qml/org/kde/plasma/private/appmenu
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.plasmashell.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-directories
%{_datadir}/kio_desktop/*.desktop
%{_datadir}/kio_desktop/*.trash
%{_datadir}/knotifications6/*.notifyrc
%{_datadir}/kstyle
%{_datadir}/plasma/look-and-feel
%{_datadir}/solid/actions/openWithFileManager.desktop
%dir %{_datadir}/plasma/plasmoids
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%{_datadir}/plasma/plasmoids/org.kde.plasma.cameraindicator
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu
%dir %{_datadir}/plasma/wallpapers
%{_datadir}/plasma/wallpapers/org.kde.color
%{_datadir}/plasma/wallpapers/org.kde.image
%{_datadir}/plasma/wallpapers/org.kde.slideshow
%{_libdir}/libkrdb.so
%{_qtdir}/qml/org/kde/taskmanager
%{_datadir}/qlogging-categories6/*.categories
%{_sysconfdir}/xdg/plasmanotifyrc
%{_qtdir}/qml/org/kde/notificationmanager
%{_qtdir}/qml/org/kde/plasma/private/containmentlayoutmanager
%{_qtdir}/qml/org/kde/plasma/private/kicker
%{_libdir}/libexec/plasma-sourceenv.sh
%{_bindir}/kcolorschemeeditor
%{_bindir}/kfontinst
%{_datadir}/kio/servicemenus/installfont.desktop
%{_bindir}/kfontview
%{_bindir}/lookandfeeltool
%{_libdir}/libexec/kf6/kauth/fontinst*
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_libdir}/libexec/kfontprint
%{_libdir}/libexec/plasma-changeicons
%{_libdir}/libexec/plasma-dbus-run-session-if-needed
%{_userunitdir}/*.service
%{_userunitdir}/*.target
%{_datadir}/applications/org.kde.kcolorschemeeditor.desktop
%{_datadir}/applications/org.kde.kfontview.desktop
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/icons/hicolor/*/mimetypes/fonts-package.*
%{_datadir}/icons/hicolor/*/apps/kfontview.*
%{_datadir}/icons/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_datadir}/kfontinst/icons/hicolor/*/actions/*.png
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod
%{_qtdir}/plugins/kf6/parts/kfontviewpart.so
%{_bindir}/plasma-interactiveconsole
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_kill.so
%{_qtdir}/plugins/plasma/kcminit/kcm_fonts_init.so
%{_qtdir}/plugins/plasma/kcminit/kcm_style_init.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_autostart.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_colors.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_cursortheme.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_desktoptheme.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_feedback.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_fonts.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_icons.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_lookandfeel.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_nightcolor.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_notifications.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_soundtheme.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_style.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_users.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%{_qtdir}/qml/org/kde/plasma/lookandfeel
%{_datadir}/applications/kcm_autostart.desktop
%{_datadir}/applications/kcm_colors.desktop
%{_datadir}/applications/kcm_cursortheme.desktop
%{_datadir}/applications/kcm_desktoptheme.desktop
%{_datadir}/applications/kcm_feedback.desktop
%{_datadir}/applications/kcm_fontinst.desktop
%{_datadir}/applications/kcm_fonts.desktop
%{_datadir}/applications/kcm_icons.desktop
%{_datadir}/applications/kcm_lookandfeel.desktop
%{_datadir}/applications/kcm_nightcolor.desktop
%{_datadir}/applications/kcm_notifications.desktop
%{_datadir}/applications/kcm_soundtheme.desktop 
%{_datadir}/applications/kcm_style.desktop
%{_datadir}/applications/kcm_users.desktop
%{_datadir}/applications/org.kde.plasmawindowed.desktop
%{_datadir}/plasma/avatars
%{_datadir}/kxmlgui5/kfontview
%{_bindir}/plasma-localegen-helper
%{_datadir}/applications/kcm_regionandlang.desktop
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%{_qtdir}/plugins/kf6/thumbcreator/fontthumbnail.so
%{_qtdir}/qml/org/kde/plasma/private/mediacontroller
%{_datadir}/zsh/site-functions/_plasmashell
%{_qtdir}/plugins/plasma5support/dataengine
%{_qtdir}/plugins/kf6/kfileitemaction/wallpaperfileitemaction.so
%{_qtdir}/plugins/kf6/packagestructure/plasma_*.so
%{_qtdir}/plugins/kf6/packagestructure/wallpaper_images.so
%{_qtdir}/plugins/plasma5support/geolocationprovider
%{_datadir}/plasma5support/services/*.operations
%{_libdir}/libkmpris.so*
%{_libdir}/qt6/qml/org/kde/plasma/private/mpris
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_wallpaper.so
%{_datadir}/applications/kcm_wallpaper.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.brightness
%{_libdir}/kconf_update_bin/plasma6.0-remove-dpi-settings
%{_libdir}/kconf_update_bin/plasma6.0-remove-old-shortcuts
%{_libdir}/kconf_update_bin/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels
%{_libdir}/kconf_update_bin/plasmashell-6.0-keep-custom-position-of-panels
%{_datadir}/kconf_update/plasmashell-6.0-keep-custom-position-of-panels.upd
%{_datadir}/kconf_update/plasma6.0-remove-dpi-settings.upd
%{_datadir}/kconf_update/plasma6.0-remove-old-shortcuts.upd
%{_datadir}/kconf_update/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels.upd
%{_datadir}/zsh/site-functions/_krunner
%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.py
%{_datadir}/kconf_update/migrate-calendar-to-plugin-id.upd

# Please do NOT split those into separate libpackages. They're used only
# internally.
%{_libdir}/libkworkspace6.so*
%{_libdir}/libplasma-geolocation-interface.so*
%{_libdir}/libweather_ion.so*
%{_libdir}/libtaskmanager.so*
%{_libdir}/libcolorcorrect.so.*
%{_libdir}/libnotificationmanager.so*

%files x11
%{_bindir}/startplasma-x11
%{_datadir}/xsessions/plasmax11.desktop

%files wayland
#%{_sysconfdir}/sddm.conf.d/plasma-wayland.conf
%{_bindir}/startplasma-wayland
%{_datadir}/wayland-sessions/plasma.desktop

%files -n plasma6-sddm-theme-breeze
%{_datadir}/sddm/themes/breeze

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkrdb.so
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/LibColorCorrect
%{_datadir}/dbus-1/interfaces/*.xml
%{_libdir}/cmake/LibNotificationManager
