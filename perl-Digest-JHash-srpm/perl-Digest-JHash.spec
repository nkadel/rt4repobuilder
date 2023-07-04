Name:           perl-Digest-JHash
Version:        0.07
Release:        5%{?dist}
Summary:        Perl extension for 32 bit Jenkins Hashing Algorithm
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest-JHash/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/Digest-JHash-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

# For improved testing
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Provides: perl(Digest::JHash) = %{version}

%{?perl_default_filter}

%description
The Digest::JHash module allows you to use the fast JHash hashing algorithm
developed by Bob Jenkins from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 32-bit
"message digest" of the input in the form of an unsigned long integer.

%prep
%setup -q -n Digest-JHash-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test RELEASE_TESTING=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*
%{_mandir}/man3/*

%changelog
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.07-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-2
- Perl mass rebuild

* Sat Feb 05 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.07-1
- Specfile autogenerated by cpanspec 1.78.
