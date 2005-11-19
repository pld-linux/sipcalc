Summary:	Sipcalc is an "advanced" console based IP subnet calculator
Summary(pl):	Sipcalc jest "zaawansowanym" konsolowym kalkulatorem podsieci IP
Name:		sipcalc
Version:	1.1.3
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.routemeister.net/projects/sipcalc/files/%{name}-%{version}.tar.gz
# Source0-md5:	dc73614a08cae479942ca882b7318452
URL:		http://www.routemeister.net/projects/sipcalc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sipcalc, in it's simplest form takes an ip-address and a subnet mask
on the commandline and outputs information about the subnet. Sipcalc
has support for both IPv4 and IPv6 addresses.

%description -l pl
Sipcalc, w podstawowym trybie dzia�ania czyta adres IP i mask�
podsieci z linii polece� i wypisuje informacje na temat podsieci.
Sipcalc wspiera zar�wno adresy IPv4, jak i IPv6.

%prep
%setup -q

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/sipcalc.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
