Name: 		perl-Tree-Simple
Version: 	1.18
Release: 	4%{?dist}
Summary: 	Tree::Simple Perl module
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Tree-Simple/
Source0: 	http://www.cpan.org/modules/by-module/Tree/Tree-Simple-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: 	noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(Test::Exception) >= 0.15 
BuildRequires:  perl(Test::Pod) >=  1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Memory::Cycle)

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A simple tree object.

%prep
%setup -q -n Tree-Simple-%{version}

# Shipped executable with 1.15
chmod -x lib/Tree/Simple.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Tree
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.18-2
- rebuild for new perl

* Mon Nov 19 2007 Ralf Corsépius <rc040203@freenet.de> - 1.18-1
- Upstream bugfix.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.17-2
- Update license tag.

* Fri Nov 03 2006 Ralf Corsépius <rc040203@freenet.de> - 1.17-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.16-2
- Mass rebuild.

* Tue Apr 04 2006 Ralf Corsépius <rc040203@freenet.de> - 1.16-1
- Upsteam update.
- BR: Scalar::Util >= 1.18.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 1.15-3
- Rebuild for perl-5.8.8.

* Thu Aug 20 2005 Ralf Corsepius <ralf@links2linux.de> - 1.15-2
- Spec cleanup.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 1.15-1
- Upstream update.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 1.14-1
- FE submission.
