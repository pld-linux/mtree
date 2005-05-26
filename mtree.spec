Summary:	mtree utility
Name:		mtree
Version:	2005Q1
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-install.patch
URL:		http://www.netbsd.org/
BuildRequires:	autoconf
BuildRequires:	libnbcompat >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mtree utility compares the file hierarchy rooted in the current di-
rectory against a specification read from the standard input.  Messages
are written to the standard output for any files whose characteristics do
not match the specification, or which are missing from either the file
hierarchy or the specification.

%prep
%setup -q -c -n %{name}-%{version}
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
#%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/mtree
%{_mandir}/man8/*