Name:           perl-PerlIO-eol
Version:        0.14
#Release:        6%{?dist}
Release:        0.6%{?dist}
Summary:        PerlIO layer for normalizing line endings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PerlIO-eol/
Source0:        http://www.cpan.org/modules/by-module/PerlIO/PerlIO-eol-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 1:5.7.3
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This layer normalizes any of CR, LF, CRLF and Native into the designated
line ending. It works for both input and output handles.

%prep
%setup -q -n PerlIO-eol-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PerlIO*
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.14-4
- rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.14-3
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Ian Burrell <ianburrell@gmail.com> - 0.14-2
- Fix BuildRequires

* Sat Dec 16 2006 Ian Burrell <ianburrell@gmail.com> - 0.14-1
- Update to 0.14

* Mon Sep 11 2006 Ian M. Burrell <ianburrell@gmail.com> - 0.13-4
- Rebuild for FC6

* Tue Jun 27 2006 Ian Burrell <ianburrell@gmail.com> - 0.13-3
- Fix rpmlint warnings

* Thu Mar 30 2006 Ian Burrell <ianburrell@gmail.com> 0.13-1
- Specfile autogenerated by cpanspec 1.64.
