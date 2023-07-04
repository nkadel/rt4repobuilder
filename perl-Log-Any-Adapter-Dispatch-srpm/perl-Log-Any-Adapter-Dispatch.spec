Name:           perl-Log-Any-Adapter-Dispatch
Version:        0.06
Release:        6%{?dist}
Summary:        Log::Any::Adapter::Dispatch Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Any-Adapter-Dispatch/
Source0:        http://www.cpan.org/authors/id/J/JS/JSWARTZ/Log-Any-Adapter-Dispatch-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::Util)
BuildRequires:  perl(Log::Dispatch) >= 2.26
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Harness)
Requires:       perl(Log::Dispatch) >= 2.26
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This Log::Any adapter uses Log::Dispatch for logging.

%prep
%setup -q -n Log-Any-Adapter-Dispatch-%{version}

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing
%{__perl} Makefile.PL INSTALLDIRS=vendor  --skipdeps
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
* Tue Mar 12 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 0.06-0.1
- Rollback release number for update consistency.
- Add BuildRequires: perl(Test::Harness).

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 0.06-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.06-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.06-2
- Perl mass rebuild

* Sun Feb 06 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.06-1
- Initial Fedora package.
