Name:           perl-Text-Haml
Version:        0.990116
#Release:        2%{?dist}
Release:        0.22%{?dist}
Summary:        Haml Perl implementation
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Haml/
Source0:        http://www.cpan.org/authors/id/V/VT/VTI/Text-Haml-%{version}.tar.gz

# --with pod_tests ... whether to excercise pod tests
#       Currently broken, therefore default to --without.
%bcond_with pod_tests

BuildArch:      noarch
BuildRequires:  perl(constant)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Data::Section::Simple)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%if %{with pod_tests}
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Text::Haml implements the Haml 
http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html
specification.

%prep
%setup -q -n Text-Haml-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?with_pod_tests:TEST_POD=1} ./Build test

%files
%doc LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Feb 16 2015 Nico Kadel-Garcia <nkdel@gmail.com>
- Add perl(CPAN::Meta) build dependency
- Roll back release number to avoid system overlap

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.990116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.990116-1
- Upstream update.
- Add %%bcond_with pod_tests.

* Mon Jan 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.990115-1
- Upstream update.

* Fri Jan 17 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.990114-1
- Fedora submission.
