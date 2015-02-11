Name:           perl-HTML-Lint
Version:        2.20
Release:        8%{?dist}
Summary:        HTML::Lint Perl module
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-Lint/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/HTML-Lint-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Parser) >= 3.47
BuildRequires:  perl(HTML::Tagset) >= 3.03
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
# Optional
BuildRequires:  perl(LWP::Simple)

# For improved testing
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Convenience to users looking for weblint
Provides:       weblint = %{version}-%{release}

%description
HTML::Lint Perl module, a pure-Perl HTML parser and checker for syntactic
legitmacy.

%prep
%setup -q -n HTML-Lint-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/weblint
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 2.20-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 2.20-3
- Perl 5.16 rebuild

* Thu Apr 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.20-2
- Bump release due to typo in spec.

* Thu Apr 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.20-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 2.10-1
- License change.
- Upstream update.
- Spec file cleanup.

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.06-8
- Perl mass rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.06-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.06-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.06-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ralf Corsépius <corsepiu@fedoraproject.org> 2.06-1
- Initial Fedora submission.
