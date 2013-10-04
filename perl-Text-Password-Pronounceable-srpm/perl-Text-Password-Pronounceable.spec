Name:       perl-Text-Password-Pronounceable 
Version:    0.30
Release:    3%{?dist}
# lib/Text/Password/Pronounceable.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Group:      Development/Libraries
Summary:    Generate pronounceable passwords 
Source0:    http://search.cpan.org/CPAN/authors/id/T/TS/TSIBLEY/Text-Password-Pronounceable-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Text-Password-Pronounceable
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:  noarch
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
This module generates pronuceable passwords, based on the English
digraphs by D. Edwards.

%prep
%setup -q -n Text-Password-Pronounceable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.30-2
- Perl 5.16 rebuild

* Fri Jan 13 2012 Petr Šabata <contyk@redhat.com> - 0.30-7
- 0.30 bump
- Spec cleanup

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.28-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.28-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.28-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.28-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.28-1
- submission

* Wed Mar 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.28-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

