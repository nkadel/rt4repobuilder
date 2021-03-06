Name:           perl-HTML-RewriteAttributes
Version:        0.05
Release:        0.1%{?dist}
Summary:        Concise attribute rewriting
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-RewriteAttributes/
Source0:        http://www.cpan.org/authors/id/T/TS/TSIBLEY/HTML-RewriteAttributes-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(URI)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML attribute
rewriting.

%prep
%setup -q -n HTML-RewriteAttributes-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> 0.05-0.1
- Add BuildRequires: perl(Test::Harness) to allow mock compilation.

* Tue Nov 13 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.05-1
- Upstream update.
- Spec file cleanup.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.04-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 06 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.04-1
- Upstream update.

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Specfile autogenerated by cpanspec 1.77.
