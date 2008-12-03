Summary:	NetworkManager VPN integration for vpnc
Summary(pl.UTF-8):	Integracja NetworkManagera z vpnc
Name:		NetworkManager-vpnc
Version:	0.7.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/NetworkManager-vpnc/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	35b2df5e7f4e091087990193dd742b55
Patch0:		%{name}-binary_path.patch
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 0.7.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires:	NetworkManager >= 0.7.0
Requires:	vpnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for vpnc.

%description -l pl.UTF-8
Integracja NetworkManagera z vpnc.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpnc-properties.so
%attr(755,root,root) %{_libdir}/nm-vpnc-auth-dialog
%attr(755,root,root) %{_libdir}/nm-vpnc-service
%attr(755,root,root) %{_libdir}/nm-vpnc-service-vpnc-helper
%{_sysconfdir}/NetworkManager/VPN/nm-vpnc-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-vpnc-service.conf
%{_desktopdir}/nm-vpnc.desktop
%dir %{_datadir}/gnome-vpn-properties
%{_datadir}/gnome-vpn-properties/vpnc
%{_iconsdir}/hicolor/*/*/*.png
