Name: 		perl-Text-Quoted
Version: 	2.05
#Release: 	4%{?dist}
Release: 	0.4%{?dist}
Summary: 	Extract the structure of a quoted mail message
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Text-Quoted/
Source0: 	http://www.cpan.org/modules/by-module/Text/Text-Quoted-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Text::Autoformat)

%description
Text::Quoted examines the structure of some text which may contain multiple
different levels of quoting, and turns the text into a nested data structure.

%prep
%setup -q -n Text-Quoted-%{version}

# Shipped +x in perl-Text-Quoted-1.8/1.10
chmod -x Quoted.pm

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
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 2.05-0.4
- Port to RHEL 7, roll back release to avoid upstream conflicts

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.05-2
Rebuild for new perl

* Fri Jan 25 2008 Ralf Corsépius <rc040203@freenet.de> - 2.05-1
- Upstream update.

* Tue Nov 13 2007 Ralf Corsépius <rc040203@freenet.de> - 2.03-1
- Upstream update.

* Fri Aug 31 2007 Ralf Corsépius <rc040203@freenet.de> - 2.02-3
- BR: perl(Test::More).
- Update license tag.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 2.02-2
- BR: perl(ExtUtils::MakeMaker).

* Fri Mar 02 2007 Ralf Corsépius <rc040203@freenet.de> - 2.02-1
- Upstream update.

* Fri Feb 16 2007 Ralf Corsépius <rc040203@freenet.de> - 1.10-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.8-5
- Mass rebuild.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 1.8-4
- Rebuild for perl-5.8.8.

* Thu Aug 19 2005 Ralf Corsepius <ralf@links2linux.de> - 1.8-3
- chmod -x Quote.pm.

* Thu Aug 19 2005 Ralf Corsepius <ralf@links2linux.de> - 1.8-2
- Spec cleanup.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 1.8-1
- FE submission.
