%define devname %mklibname plasma-workspace -d
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230521

# filter qml/plugins provides
%global __provides_exclude_from ^(%{_kde5_qmldir}/.*\\.so|%{_qt5_plugindir}/.*\\.so)$

Name: plasma6-workspace
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-workspace/-/archive/master/plasma-workspace-master.tar.bz2#/plasma-workspace-%{git}.tar.bz2
%else
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Source1: kde.pam
Patch0: plasma-workspace-bump-sonames.patch
# FIXME this needs to be redone properly (OM theme)
# Patch2: plasma-workspace-5.8.0-use-openmandriva-icon-and-background.patch
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
BuildRequires: cmake(KF6Activities)
BuildRequires: cmake(KF6ActivitiesStats)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6Wayland)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: pkgconfig(libnm) >= 1.4.0
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6People)
BuildRequires: cmake(KF6KDED)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Plasma)
BuildRequires: cmake(KF6PlasmaQuick)
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
BuildRequires: cmake(KF6Plasma5Support)
BuildRequires: cmake(KF6KExiv2)
BuildRequires: cmake(KUserFeedbackQt6)
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
# Both Plasma 5 and Plasma 6 provide
# cmake(KPipeWire), cmake(KSysGuard) and friends
BuildRequires: cmake(KPipeWire) >= 5.27.80
BuildRequires: plasma6-kwin-devel
BuildRequires: cmake(KWinDBusInterface) >= 5.27.80
BuildRequires: cmake(KSysGuard) >= 5.27.80
# needed for backgrounds and patch 2
Requires: distro-release-theme
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

%description
The KDE Plasma workspace.

%libpackage kworkspace5 6
%{_libdir}/libkworkspace5.so.5*

%libpackage plasma-geolocation-interface 6
%{_libdir}/libplasma-geolocation-interface.so.5*

%libpackage weather_ion 8

%libpackage taskmanager 7
%{_libdir}/libtaskmanager.so.5*

%libpackage colorcorrect 6
%{_libdir}/libcolorcorrect.so.5*

%libpackage notificationmanager 5
%{_libdir}/libnotificationmanager.so.2

%package -n %{devname}
Summary: Development files for the KDE Plasma workspace
Group: Development/KDE and Qt
Requires: %{mklibname kworkspace5} = %{EVRD}
Requires: %{mklibname plasma-geolocation-interface} = %{EVRD}
Requires: %{mklibname taskmanager} = %{EVRD}
Requires: %{mklibname weather_ion} = %{EVRD}
Requires: %{mklibname colorcorrect} = %{EVRD}
Requires: %{mklibname notificationmanager} = %{EVRD}
Provides: %{mklibname -d kworkspace} = %{EVRD}
Provides: %{mklibname -d plasma-geolocation-interface} = %{EVRD}
Provides: %{mklibname -d taskmanager} = %{EVRD}
Provides: %{mklibname -d weather_ion} = %{EVRD}
Provides: %{mklibname -d colorcorrect} = %{EVRD}
Provides: %{mklibname -d notificationmanager} = %{EVRD}

%description -n %{devname}
Development files for the KDE Plasma workspace.

%package -n sddm-theme-breeze
Summary: KDE Breeze theme for the SDDM display manager
Group: Graphical desktop/KDE
Requires: sddm

%description -n sddm-theme-breeze
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

%description x11
X11 support for Plasma Workspace.

%package wayland
Summary: Wayland support for Plasma Workspace
Group: Graphical desktop/KDE
Requires: %{name}
Provides: %{name}-backend = %{EVRD}
Requires: xwayland
Requires: plasma6-kwin-wayland
Recommends: plasma6-xdg-desktop-portal-kde

%description wayland
Wayland support for Plasma Workspace.

%prep
%autosetup -p1 -n plasma-workspace-%{?git:master}%{!?git:%{version}}
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

# breeze backgrounds
rm -rf %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/background.png
ln -sf %{_datadir}/mdk/backgrounds/default.png %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/background.png

# sddm breeze theme background
rm -rf %{buildroot}%{_datadir}/sddm/themes/breeze/components/artwork/background.png
ln -sf %{_datadir}/mdk/backgrounds/OpenMandriva-splash.png %{buildroot}%{_datadir}/sddm/themes/breeze/components/artwork/background.png
sed -i -e "s#^background=.*#background=%{_datadir}/mdk/backgrounds/OpenMandriva-splash.png#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf
sed -i -e "s#^type=.*#type=image#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf

# (tpg) fix autostart permissions
chmod 644 %{buildroot}%{_sysconfdir}/xdg/autostart/*

%find_lang %{name} --all-name --with-html

%libpackage kfontinst 6
%{_libdir}/libkfontinst.so.5*

%libpackage kfontinstui 6
%{_libdir}/libkfontinstui.so.5*

%files -f %{name}.lang
%{_bindir}/plasma-apply-colorscheme
%{_bindir}/plasma-apply-cursortheme
%{_bindir}/plasma-apply-desktoptheme
%{_bindir}/plasma-apply-lookandfeel
%{_bindir}/plasma-apply-wallpaperimage
%{_bindir}/plasma-shutdown
%{_sysconfdir}/xdg/autostart/gmenudbusmenuproxy.desktop
%{_sysconfdir}/xdg/autostart/klipper.desktop
%{_sysconfdir}/xdg/autostart/org.kde.plasmashell.desktop
%{_sysconfdir}/xdg/autostart/xembedsniproxy.desktop
%{_sysconfdir}/xdg/taskmanagerrulesrc
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
%{_bindir}/systemmonitor
%{_bindir}/xembedsniproxy
%{_bindir}/kde-systemd-start-condition
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
%{_qtdir}/qml/org/kde/colorcorrect
%dir %{_qtdir}/qml/org/kde/plasma/private
%{_qtdir}/qml/org/kde/plasma/private/digitalclock
%{_qtdir}/qml/org/kde/plasma/private/shell
%{_qtdir}/qml/org/kde/plasma/private/sessions
%{_qtdir}/qml/org/kde/plasma/wallpapers
%{_qtdir}/qml/org/kde/plasma/workspace
%{_qtdir}/qml/org/kde/holidayeventshelperplugin
%{_qtdir}/qml/org/kde/plasma/private/appmenu
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.klipper.desktop
%{_datadir}/applications/org.kde.plasmashell.desktop
%{_datadir}/applications/org.kde.systemmonitor.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-directories
%{_datadir}/kio_desktop/*.desktop
%{_datadir}/kio_desktop/*.trash
%{_datadir}/knotifications6/*.notifyrc
%{_datadir}/kservices6/*
%{_datadir}/kservicetypes6/*.desktop
%{_datadir}/kstyle
%{_datadir}/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/plasma/look-and-feel
%dir %{_datadir}/plasma/plasmoids
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
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
%{_libdir}/kconf_update_bin/krunnerglobalshortcuts
%{_libdir}/libexec/plasma-sourceenv.sh
%{_bindir}/kcolorschemeeditor
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/lookandfeeltool
%{_libdir}/libexec/kauth/fontinst*
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_libdir}/libexec/kfontprint
%{_libdir}/libexec/plasma-changeicons
%{_libdir}/libexec/plasma-dbus-run-session-if-needed
%{_userunitdir}/*.service
%{_userunitdir}/*.target
%{_libdir}/kconf_update_bin/krunnerhistory
%{_datadir}/applications/org.kde.kcolorschemeeditor.desktop
%{_datadir}/applications/org.kde.kfontview.desktop
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/icons/hicolor/*/mimetypes/fonts-package.*
%{_datadir}/icons/hicolor/*/apps/kfontview.*
%{_datadir}/icons/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_datadir}/kconf_update/*.pl
%{_datadir}/kconf_update/*.upd
%{_datadir}/kfontinst/icons/hicolor/*/actions/*.png
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kxmlgui6/kfontview/*.rc
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
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_style.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_users.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%{_qtdir}/qml/org/kde/plasma/lookandfeel
%{_datadir}/applications/kcm_autostart.desktop
%{_datadir}/applications/kcm_colors.desktop
%{_datadir}/applications/kcm_cursortheme.desktop
%{_datadir}/applications/kcm_feedback.desktop
%{_datadir}/applications/kcm_fontinst.desktop
%{_datadir}/applications/kcm_fonts.desktop
%{_datadir}/applications/kcm_icons.desktop
%{_datadir}/applications/kcm_lookandfeel.desktop
%{_datadir}/applications/kcm_nightcolor.desktop
%{_datadir}/applications/kcm_notifications.desktop
%{_datadir}/applications/kcm_style.desktop
%{_datadir}/applications/kcm_users.desktop
%{_datadir}/applications/org.kde.plasmawindowed.desktop
%{_datadir}/plasma/avatars
%{_bindir}/plasma-localegen-helper
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%{_datadir}/applications/kcm_regionandlang.desktop
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%{_libdir}/kconf_update_bin/plasmashell-5.27-use-panel-thickness-in-default-group
%{_qtdir}/plugins/kf6/thumbcreator/fontthumbnail.so
%{_qtdir}/qml/org/kde/plasma/private/mediacontroller
%{_datadir}/zsh/site-functions/_plasmashell
%{_datadir}/applications/kcm_desktoptheme.desktop
%{_qtdir}/plugins/plasma5support/dataengine
%{_qtdir}/plugins/kf6/kfileitemaction/wallpaperfileitemaction.so
%{_qtdir}/plugins/kf6/packagestructure/plasma_*.so
%{_qtdir}/plugins/kf6/packagestructure/wallpaper_images.so
%{_qtdir}/plugins/plasma5support/geolocationprovider
%{_datadir}/plasma5support/services/*.operations

%files x11
%{_bindir}/startplasma-x11
%{_datadir}/xsessions/plasma.desktop

%files wayland
%if %omvver >= 4050000
%{_sysconfdir}/sddm.conf.d/plasma-wayland.conf
%endif
%{_qtdir}/plugins/wayland-shell-integration/plasma-shell.so
%{_bindir}/startplasma-wayland
%{_datadir}/wayland-sessions/plasmawayland.desktop

%files -n sddm-theme-breeze
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
