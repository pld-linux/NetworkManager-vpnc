Summary:	NetworkManager VPN integration for vpnc
Summary(pl.UTF-8):	Integracja NetworkManagera z vpnc
Name:		NetworkManager-vpnc
Version:	0.9.8.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-vpnc/0.9/%{name}-%{version}.tar.xz
# Source0-md5:	ae7751aa3738fcd954d863d25e3720e2
Patch0:		%{name}-binary_path.patch
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 2:0.9.8.4
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	NetworkManager >= 2:0.9.8.4
Requires:	hicolor-icon-theme
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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpnc-properties.so
%attr(755,root,root) %{_libdir}/nm-vpnc-auth-dialog
%attr(755,root,root) %{_libdir}/nm-vpnc-service
%attr(755,root,root) %{_libdir}/nm-vpnc-service-vpnc-helper
%{_sysconfdir}/NetworkManager/VPN/nm-vpnc-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-vpnc-service.conf
%{_datadir}/gnome-vpn-properties/vpnc
%{_desktopdir}/nm-vpnc-auth-dialog.desktop
%{_iconsdir}/hicolor/*/*/*.png
