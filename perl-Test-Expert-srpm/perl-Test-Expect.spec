Name:           perl-Test-Expect
Version:        0.31
#Release:        3%{?dist}
Release:        0.3%{?dist}
Summary:        Automated driving and testing of terminal-based programs

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Expect/
Source0:        http://www.cpan.org/authors/id/L/LB/LBROCARD/Test-Expect-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Expect::Simple)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Builder)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Test::Expect is a module for automated driving and testing of
terminal-based programs. It is handy for testing interactive programs
which have a prompt, and is based on the same concepts as the Tcl Expect
tool. As in Expect::Simple, the Expect object is made available for
tweaking.

Test::Expect is intended for use in a test script.


%prep
%setup -q -n Test-Expect-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*


%check
./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.31-0.3
- Port to RHEL 7, roll back release to avoid upstream repositories.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 16 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.31-1
- Upgrade to 0.31 (Required by rt3's testsuite, BZ 462440).

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.30-3
Rebuild for new perl

* Tue Dec 11 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-2
- BR: perl(Test::More), perl(Test::Builder) (BZ 419631).

* Wed May 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30-1
- First build.
