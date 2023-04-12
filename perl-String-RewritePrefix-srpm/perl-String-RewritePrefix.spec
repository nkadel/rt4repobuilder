Name:           perl-String-RewritePrefix 
Summary:        Rewrite strings based on a set of known prefixes 
Version:        0.005
#Release:        1%{?dist}
Release:        0.1%{?dist}
License:        GPL+ or Artistic 
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/String-RewritePrefix-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/String-RewritePrefix
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.47

Requires:       perl(Sub::Exporter)


%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
%{summary}.


%prep
%setup -q -n String-RewritePrefix-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.xom> -  0.005-0.1
- Port for RHEL 7, roll back number to avoid upstream version conflict

* Sun Mar 14 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.005-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.005)
- added a new br on perl(Sub::Exporter) (version 0)
- added a new req on perl(Sub::Exporter) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.004-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.004-1
- submission

* Wed Jul 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.004-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
