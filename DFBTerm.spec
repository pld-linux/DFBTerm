Summary:	DFBTerm - terminal application for DirectFB
Summary(pl.UTF-8):	DFBTerm - emulator terminala dla DirectFB
Name:		DFBTerm
Version:	0.8.15
Release:	1
License:	MIT
Group:		Applications/Graphics
Source0:	http://www.directfb.org/downloads/Programs/%{name}-%{version}.tar.gz
# Source0-md5:	0e554bbb65052289d01415f7042d72d2
Patch0:		%{name}-font.patch
URL:		http://www.directfb.org/index.php?path=Development/Projects/DFBTerm
BuildRequires:	DirectFB-devel >= 0.9.14
BuildRequires:	LiTE-devel >= 0.4.2
BuildRequires:	automake
BuildRequires:	pkgconfig
Requires:	DirectFB-font-ft2
Requires:	DirectFB-image-png
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DFBTerm is a terminal application for DirectFB. It uses LiTE (LiTE is
a Toolkit Engine) and has a very nice anti aliased fixed width font.
 
%description -l pl.UTF-8
DFBTerm to emulator terminala dla DirectFB. Korzysta z toolkitu LiTE i
ma bardzo ładny font o stałej szerokości znaków z antyaliasingiem.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/dfbterm
%attr(755,root,root) %{_sbindir}/dfbterm-pty-helper
