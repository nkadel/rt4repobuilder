Name:           perl-Email-Address
Version:        1.900
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        RFC 2822 Address Parsing and Creation

Group:          Development/Libraries
# Outdated FSF address reported, rt#86433
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Email-Address/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Email-Address-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Capture::Tiny)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This class implements a regex-based RFC 2822 parser that locates email
addresses in strings and returns a list of Email::Address objects found.
Alternatively you may construct objects manually. The goal of this software
is to be correct, and very very fast.

%prep
%setup -q -n Email-Address-%{version}
%{__perl} -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' bench/ea-vs-ma.pl


%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes LICENSE README META.json bench/
%{perl_vendorlib}/Email/
%{_mandir}/man3/*.3pm*


%changelog
* Fri Aug 16 2013 Tom Callaway <spot@fedoraproject.org> - 1.900-1
- update to 1.900

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.898-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.898-3
- Perl 5.18 rebuild

* Wed Jun 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.898-2
- Specify all dependencies
- Drop %%defattr, remove %%clean section
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Fri Feb  8 2013 Tom Callaway <spot@fedoraproject.org> - 1.898-1
- update to 1.898

* Wed Dec 19 2012 Tom Callaway <spot@fedoraproject.org> - 1.897-1
- update to 1.897

* Tue Sep 18 2012 Marcela Mašláňová <mmaslano@redhat.com> 1.896-1
- update to 1.896

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.889-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.889-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.889-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.889-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.889-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.889-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.889-6
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.889-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.889-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.889-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.889-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.889-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.888-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.888-2
- rebuild for new perl

* Sat Jun 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.888-1
- Update to 1.888.

* Thu Apr  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.887-1
- Update to 1.887.

* Sun Mar 18 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.886-1
- Update to 1.886.

* Tue Dec 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.884-1
- Update to 1.884.

* Sat Nov 25 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.883-1
- Update to 1.883.

* Wed Nov 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.882-1
- Update to 1.882.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.880-1
- Update to 1.880.

* Fri Oct 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.871-1
- Update to 1.871.

* Sat Aug 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.870-1
- Update to 1.870.

* Sat Jul 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.86-1
- Update to 1.86.

* Tue Jul 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.85-1
- Update to 1.85.

* Thu Sep 08 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.80-1
- First build.
