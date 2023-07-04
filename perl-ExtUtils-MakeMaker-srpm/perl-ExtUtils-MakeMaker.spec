Name:           perl-ExtUtils-MakeMaker
Version:        6.64
Release:        0.1%{?dist}
Summary:        Create a module Makefile

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/ExtUtils::MakeMaker
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHWERN/ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Version from perl SRPM has arch
#BuildArch:      noarch

# Provide needed config.h files.
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Harness)

%description
Create a module Makefile.

%prep
%setup -q -n ExtUtils-MakeMaker-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

for file in Changes; do
  iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
  mv -f "${file}_" "$file"
done


%check
make test


%clean 
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/instmodsh
%{perl_vendorlib}/*
%{_mandir}/man1/instmodsh.1*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/*

%changelog
* Mon Mar 11 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 6.64-0.1
- Update to 6.64, to install alongside built-in version from perl SRPM.
