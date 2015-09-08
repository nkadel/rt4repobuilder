Name:           perl-Expect-Simple
Version:        0.04
#Release:        4%{?dist}
Release:        0.4%{?dist}
Summary:        Wrapper around the Expect module

Group:          Development/Libraries
License:        GPLv2+
URL:            http://search.cpan.org/dist/Expect-Simple/
Source0:        http://www.cpan.org/authors/id/D/DJ/DJERIUS/Expect-Simple-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Expect)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Expect::Simple is a wrapper around the Expect module which should
suffice for simple applications. It hides most of the Expect
machinery; the Expect object is available for tweaking if need be.


%prep
%setup -q -n Expect-Simple-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README
%{perl_vendorlib}/Expect/
%{_mandir}/man3/*.3pm*


%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.04-0.4
- Port to RHEL 7, roll back release to avoid upstream conflicts

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- update to 0.04
- add Test::More as a br

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-2
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.02-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Wed May 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.02-1
- First build.
