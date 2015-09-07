Summary:	Perl extension to create simple calendars
Name:		perl-Calendar-Simple
Version:	1.21
#Release:	1%{?dist}
Release:	0.1%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Calendar-Simple/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/Calendar-Simple-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Required by the tests
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)

%description
Perl extension to create simple calendars.

%prep
%setup -q -n Calendar-Simple-%{version}
chmod -x lib/*/Simple.pm

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
%{_bindir}/pcal
%{perl_vendorlib}/Calendar
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 1.21-0.1
- Port to RHEL 7, with release moved to 0.1 to avoid upstream conflict.

* Sun May 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.21-1
- Upstream update.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 08 2008 Ralf Corsépius <rc040203@freenet.de> - 1.20-1
- Upstream update.

* Tue Mar 11 2008 Ralf Corsépius <rc040203@freenet.de> - 1.19-1
- Upstream update.
- Reflect upstream having dropped "COPYING".

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.17-3
Rebuild for new perl

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.17-2
- Update license tag.
- Reflect perl package split.

* Thu Oct 19 2006 Ralf Corsépius <rc040203@freenet.de> - 1.17-1
- Upstream update.

* Sat Oct 07 2006 Ralf Corsépius <rc040203@freenet.de> - 1.14-2
- chmod -x files with broken permissions.

* Mon Sep 18 2006 Ralf Corsépius <rc040203@freenet.de> - 1.14-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-4
- Mass rebuild.

* Fri Jun 23 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-3
- Fix indentation.

* Fri Jun 23 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-2
- Fix Source0.

* Thu Jun 22 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-1
- FE submission.
