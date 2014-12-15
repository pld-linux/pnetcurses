%define		pnet_ver	0.8.0
Summary:	Portable.NET curses library binding
Summary(pl.UTF-8):	Wiązania Portable.NET do biblioteki curses
Name:		pnetcurses
Version:	0.0.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/dotgnu-pnet/%{name}-%{version}.tar.gz
# Source0-md5:	29021d1f966bbed5a3e7c1f86507eaaa
Patch0:		%{name}-pnetlib.patch
URL:		http://www.gnu.org/software/dotgnu/pnet.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
# required tools: cscc [pnet-]resgen ilrun
BuildRequires:	pnet-compiler-csharp >= %{pnet_ver}
BuildRequires:	pnet-interpreter >= %{pnet_ver}
BuildRequires:	pnetlib-base >= %{pnet_ver}
Requires:	pnetlib-base >= %{pnet_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains a library that wraps up the Unix curses
functionality for use by C# applications.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę obudowującą funkcjonalność uniksowej
biblioteki curses do wykorzystania w aplikacjach C#.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	RESGEN=/usr/bin/pnet-resgen \
	--disable-static \
	--with-pnetlib=%{_libdir}/cscc/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D src/Curses.dll $RPM_BUILD_ROOT%{_libdir}/cscc/lib/Curses.dll

# dlopened module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libcsharpcurses.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcsharpcurses.so.0
%attr(755,root,root) %{_libdir}/libcsharpcurses.so
%{_libdir}/cscc/lib/Curses.dll
