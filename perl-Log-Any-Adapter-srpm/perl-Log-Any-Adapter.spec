Name:           perl-Log-Any-Adapter
Version:        0.11
Release:        0.1%{?dist}
Summary:        Tell Log::Any where to send its logs
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Any-Adapter/
Source0:        http://www.cpan.org/authors/id/J/JS/JSWARTZ/Log-Any-Adapter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(Guard)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Harness)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Log-Any-Adapter distribution implements Log::Any class methods to
specify where logs should be sent. It is a separate distribution so as to
keep Log::Any itself as simple and unchanging as possible.

%prep
%setup -q -n Log-Any-Adapter-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Aug  3 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 0.11-0.1
- Update to 0.11 source.

* Tue Mar 12 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 0.10-0.1
- Rollback release number to avoid update confusion.
- Add BuildRequires:: Test::Harness.

* Thu Nov 08 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.10-1
- Upstream update.
- Minor spec file brushup.

* Mon Aug 27 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.09-1
- Upstream update.

* Mon Aug 06 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.08-1
- Upstream update.
- BR: perl(Capture::Tiny).

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.07-2
- Perl 5.16 rebuild

* Thu Mar 08 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.07-1
- Upstream update.
- BR: perl(Carp).
- Remove filter.

* Sat Jan 14 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.06-1
- Upstream update.
- Reflect upstream having abandoned using ExtUtils::AutoInstall.
- Spec cleanup.
- Add rpm-4.9 filter.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.03-2
- Perl mass rebuild

* Sun Feb 06 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Initial Fedora package.
