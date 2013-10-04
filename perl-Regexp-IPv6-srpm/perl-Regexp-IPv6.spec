Name:           perl-Regexp-IPv6
Version:        0.03
Release:        0.1%{?dist}
Summary:        Regular expression for IPv6 addresses
License:        GPLv2+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Regexp-IPv6/
Source0:        http://www.cpan.org/authors/id/S/SA/SALVA/Regexp-IPv6-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module exports the $IPv6_re regular expression that matches any valid
IPv6 address as described in "RFC 2373 - 2.2 Text Representation of
Addresses" but ::. Any string not compliant with such RFC will be rejected.

%prep
%setup -q -n Regexp-IPv6-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com>
- 0.03-0.1
- Rollback release number to avoid update confusion.
- Add BuildReqireqs: perl(Test::Harness) to build on mock.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.03-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Initial Fedora package.
