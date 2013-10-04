#%perl_module Encode 2.02 4
%global	pkgname	Encode

Name:		perl-%{pkgname}
Version:	2.49
Release:	0.1%{?dist}

Summary:       Character encodings for perl.
License:       Artistic
Group:         System Environment/Libraries
URL:           http://search.cpan.org/dist/%{pkgname}
Source:        http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/%{pkgname}-%{version}.tar.gz
Source1:       README.fedora
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The "Encode" module provides the interfaces between Perl's strings and
the rest of the system.  Perl strings are sequences of characters.

%prep
%setup -q -n %{pkgname}-%{version} 
%{__install} -m0644 %{SOURCE1} README.fedora

%build
#%perl_configure
#make
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
#Fails on RH9, RH8.0
#perl_makecheck

%install
rm -rf %{buildroot}
#%perl_makeinstall

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README* Changes AUTHORS
#%{perl_vendorarch}/Encode.pm
#%{perl_vendorarch}/encoding.pm
#%{perl_vendorarch}/Encode
#%{perl_vendorarch}/auto/Encode
#%{perl_man1dir}/piconv.1*
#%{perl_man1dir}/enc2xs.1*
#%{perl_bin}/piconv
#%{perl_bin}/enc2xs

# Avoid conflict with perl-devel on RHEL 6
%exclude %{_bindir}/piconv
%exclude %{_bindir}/enc2xs
%exclude %{_mandir}/man1/piconv.1*
%exclude %{_mandir}/man1/enc2xs.1*
%exclude %{_mandir}/man3/*

%{_mandir}/man1/*
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm
%{perl_vendorarch}/Encode
%{perl_vendorarch}/auto/Encode

%changelog
* Mon Mar 11 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com>
- Port from atrpms with funky macros to RHEL 6 native compilation.
- Update to 2.49.
- Exclude bindir and mandir components to avoid conflict with older
  components in perl-devel.
- Add BuildRequires: perl(ExtUtiuls::MakeMaker).
- Add BuildRequires: perl-devel.

* Wed Sep 29 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.02.

* Sun Aug 22 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.
