Summary:	NetworkManager VPN integration for vpnc
Summary(pl.UTF-8):	Integracja NetworkManagera z vpnc
Name:		NetworkManager-vpnc
Version:	1.2.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-vpnc/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	4c16379738264a117d09c171c645ff23
Patch0:		%{name}-binary_path.patch
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	NetworkManager-gtk-lib >= 1.2.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.4
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
	--disable-more-warnings \
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-vpnc.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpnc-properties.so
%attr(755,root,root) %{_libdir}/nm-vpnc-auth-dialog
%attr(755,root,root) %{_libdir}/nm-vpnc-service
%attr(755,root,root) %{_libdir}/nm-vpnc-service-vpnc-helper
%{_prefix}/lib/NetworkManager/VPN/nm-vpnc-service.name
%{_sysconfdir}/NetworkManager/VPN/nm-vpnc-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-vpnc-service.conf
%{_datadir}/appdata/network-manager-vpnc.metainfo.xml
%{_datadir}/gnome-vpn-properties/vpnc
