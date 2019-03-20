Summary:	Desktop applets for KDE Telepathy
Name:		ktp-desktop-applets
Version:	 18.12.3
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	cmake(TelepathyQt5Farstream)
BuildRequires:	cmake(TelepathyLoggerQt)
BuildRequires:	cmake(KTp)

%description
Desktop applets for KDE Telepathy

%files -f all.lang
%{_libdir}/qt5/qml/org/kde/ktpchat
%{_datadir}/kservices5/plasma-applet-org.kde.ktp-chat.desktop
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat
%{_datadir}/kservices5/plasma-applet-org.kde.ktp-contactlist.desktop
%{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist
%{_datadir}/kservices5/plasma-applet-org.kde.person.desktop
%{_datadir}/plasma/plasmoids/org.kde.person
%{_libdir}/qt5/qml/org/kde/ktpcontactlist

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang plasma_applet_org.kde.ktp-chat
%find_lang plasma_applet_org.kde.ktp-contactlist
%find_lang plasma_applet_org.kde.person
cat *.lang >all.lang
