Name:           perl-Starlet
Version:        0.24
Release:        0.1%{?dist}
Summary:        Simple, high-performance PSGI/Plack HTTP server
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Starlet/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Starlet-%{version}.tar.gz
BuildArch:      noarch

# start_server comes ftom perl_Server_Starter_start_Server package
BuildRequires:  /usr/bin/start_server
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::UserAgent) >= 5.8
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Parallel::Prefork) >= 0.13
BuildRequires:  perl(Plack) >= 0.992
BuildRequires:  perl(Server::Starter) >= 0.06
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::TCP) >= 0.15
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Starlet is a standalone HTTP/1.1 web server, formerly known as
Plack::Server::Standalone::Prefork and
Plack::Server::Standalone::Prefork::Server::Starter.

%prep
%setup -q -n Starlet-%{version}

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
%doc Changes MYMETA.json MYMETA.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 0.16-0.1
- Rollback release number for update compatibility.
- Add BuildRequires: perl(Test::Harness) for mock compilation.
- Note souree of /usr/bin/start_server

* Mon Sep 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.16-1
- Upstream update.

* Tue Aug 14 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.15-1
- Upstream update.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 0.14-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.14-1
- Spec file cleanup.
- Abandon fedora < 15.
- Upstream update.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.13-3
- Perl mass rebuild

* Sun Feb 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.13-2
- Add Requires: Fedora < 15's rpm misses.
- Add package reviewer's package description.
- Cosmetic spec cleanups.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.13-1
- Initial Fedora package.
