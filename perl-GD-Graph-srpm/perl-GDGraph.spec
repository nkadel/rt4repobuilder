Name:           perl-GDGraph
Version:        1.48
Release:        0.1%{?dist}
Epoch:          1
Summary:        GDGraph Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/GDGraph/
Source0:        http://www.cpan.org/authors/id/R/RU/RUZ/GDGraph-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(GD) >= 1.18
BuildRequires:  perl(GD::Text) >= 0.80
Requires:       perl(GD) >= 1.18
Requires:       perl(GD::Text) >= 0.80
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
perl 5.6.0 GD >= 1.19 (recommended >= 1.23) GD::Text::Align (part of the
GDTextUtils package)

%prep
%setup -q -n GDGraph-%{version}

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
%doc CHANGES Dustismo.LICENSE Dustismo_Sans.ttf META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Feb 08 2015 Nico Kadel-Garcia <nkadel@gmail.com> 1.48-1
- Specfile autogenerated by cpanspec 1.78.
- Force Epoch to 1.

