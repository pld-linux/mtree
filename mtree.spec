Summary:	mtree utility
Summary(pl.UTF-8):   Narzędzie mtree
Name:		mtree
Version:	2005Q1
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	4ef4df775b876962a785f165df3a5eb2
Patch0:		%{name}-install.patch
URL:		http://www.netbsd.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnbcompat >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mtree utility compares the file hierarchy rooted in the current
directory against a specification read from the standard input.
Messages are written to the standard output for any files whose
characteristics do not match the specification, or which are missing
from either the file hierarchy or the specification.

%description -l pl.UTF-8
Narzędzie mtree porównuje hierarchię plików poczynając od bieżącego
katalogu ze specyfikacją czytaną ze standardowego wejścia. Na
standardowe wyjście wypisywane są komunikaty o wszystkich plikach,
których cechy nie pasują do specyfikacji, albo których brakuje w
hierarchii plików lub w specyfikacji.

%prep
%setup -q -c
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
LIBS="-lnbcompat" \
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/mtree
%{_mandir}/man8/*
