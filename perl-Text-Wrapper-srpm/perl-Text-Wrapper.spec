Name: 		perl-Text-Wrapper
Version: 	1.02
Release: 	3%{?dist}
Summary:	Simple word wrapping perl module
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Text-Wrapper/
Source0: 	http://www.cpan.org/modules/by-module/Text/Text-Wrapper-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(Module::Build::Compat)
BuildRequires:	perl(Test::More)
# For improved tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: 	noarch

%description
This module provides simple word wrapping.  It breaks long lines, but does
not alter spacing or remove existing line breaks.  If you're looking for
more sophisticated text formatting, try the Text::Format module.

%prep
%setup -q -n Text-Wrapper-%{version}
sed -i -e 's,^\([[:blank:]]*PREOP\),#\1,' Makefile.PL

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
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue May 20 2008 Ralf Corsépius <rc040203@freenet.de> - 1.02-1
- Upstream update.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-4
- Rebuild for new perl.

* Mon Feb 04 2008 Ralf Corsépius <rc040203@freenet.de> - 1.01-3
- Add BR: perl(Test::Pod), perl(Test::Pod::Coverage) (BZ: 431411)

* Thu Aug 30 2007 Ralf Corsépius <rc040203@freenet.de> - 1.01-2
- BR: perl(Test::More).
- Update License tag.

* Mon Mar 27 2007 Ralf Corsépius <rc040203@freenet.de> - 1.01-1
- Upstream update.
- BR: perl(Module::Build::Compat).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.000-4
- Mass rebuild.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 1.000-3
- Rebuild for perl-5.8.8.

* Mon Aug 22 2005 Ralf Corsepius <rc040203@freenet.de> - 1.000-2
- Spec cleanup.

* Thu Aug 18 2005 Ralf Corsepius <ralf@links2linux.de> - 1.000-1
- FE submission.
