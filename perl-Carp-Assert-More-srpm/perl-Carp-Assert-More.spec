Name:           perl-Carp-Assert-More
Version:        1.12
#Release:        6%{?dist}
Release:        0.6%{?dist}
Summary:        Convenience wrappers around Carp::Assert

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Carp-Assert-More/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Carp-Assert-More-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Assert), perl(Test::Exception)
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Provides: perl(Carp::Assert::More) = %{version}

%description
Carp::Assert::More is a set of wrappers around the Carp::Assert
functions to make the habit of writing assertions even easier.


%prep
%setup -q -n Carp-Assert-More-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/Carp/Assert/
%{_mandir}/man3/*.3pm*


%changelog
* Sat Sep  5 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-0.6
- Port to RHEL 7
- Add BuildRequires for perl(ExtUtils::MakeMaker)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.12-4
- rebuild for new perl

* Sat Sep  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-3
- Rebuild for FC6.

* Mon Feb 27 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-2
- Rebuild for FC5 (perl 5.8.8).

* Mon Oct 17 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-1
- Update to 1.12.

* Thu Aug 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.10-1
- First build.
