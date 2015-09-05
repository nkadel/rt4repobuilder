Name:           perl-Test-CheckManifest
Version:        1.24
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        Check if your Manifest matches your distro
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-CheckManifest/
Source0:        http://www.cpan.org/authors/id/R/RE/RENEEB/Test-CheckManifest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This package checks whether the Manifest file matches the distro or not. To
match a distro the Manifest has to name all files that come along with the
distribution.

%prep
# Unpackage tarball in a subdirectory, otherwise the testsuite will fail.
%setup -q -c -n %{name}-%{version}
%setup -q -T -D -n %{name}-%{version} -a0

%build
cd Test-CheckManifest-%{version}
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
cd ..

%install
cd Test-CheckManifest-%{version}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
cd ..

%check
cd Test-CheckManifest-%{version}
make test
cd ..

%files
%defattr(-,root,root,-)
%doc Test-CheckManifest-%{version}/Changes Test-CheckManifest-%{version}/README Test-CheckManifest-%{version}/LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Apr 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1.24-1
- Upstream update.

* Tue Mar 29 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1.23-1
- Upstream update.
- Add LICENSE file.
- Spec cleanup.

* Tue Mar 01 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1.22-2
- Extend %%description upon reviewer's request.

* Sat Feb 05 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1.22-1
- Initial Fedora package.
