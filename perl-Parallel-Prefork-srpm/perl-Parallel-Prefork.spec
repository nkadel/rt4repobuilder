Name:           perl-Parallel-Prefork
Version:        0.13
Release:        0.1%{?dist}
Summary:        Simple prefork server framework
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Parallel-Prefork/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Parallel-Prefork-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(Class::Accessor::Lite) >= 0.04
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Proc::Wait3) >= 0.03
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Parallel::Scoreboard)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Parallel::Prefork is much like Parallel::ForkManager, but supports graceful
shutdown and run-time reconfiguration.

%prep
%setup -q -n Parallel-Prefork-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com>
- 0.13-0.1
- Rollback release number to avoid update confusion.
- Add BuildRequires: perl(Test::Harness) for mock cimpilation.
- Add BuildRequires: perl(Time::HiRes) for RHEL: 6 compatibility.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.13-1
- Upstream update.
- Spec file cleanup.
- BR: perl(Test::SharedFork).

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.11-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-2
- Add BR: perl(Parallel::Scoreboard).

* Thu Jan 20 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-1
- Upstream update.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-1
- Initial Fedora package.
