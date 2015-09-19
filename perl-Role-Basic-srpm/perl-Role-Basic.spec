Name:           perl-Role-Basic
Version:        0.13
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        Just roles. Nothing else
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Role-Basic/
Source0:        http://www.cpan.org/authors/id/O/OV/OVID/Role-Basic-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
For an extended discussion, see http://blogs.perl.org/users/ovid/2010/12/rolebasic---when-you-only-want-
roles.html.

%prep
%setup -q -n Role-Basic-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes examples README xt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 07 2014 Nico Kadel-Garcia <nkadel@gmail.com> 0.13-1
- Specfile autogenerated by cpanspec 1.78.