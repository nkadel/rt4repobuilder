Name:           perl-PadWalker
Version:        1.96
Release:        0.2%{?dist}
Summary:        Play with other peoples' lexical variables
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PadWalker/
Source0:        http://www.cpan.org/authors/id/R/RO/ROBIN/PadWalker-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Data::Dumper)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Harness)

%description
PadWalker is a module which allows you to inspect (and even change!)
lexical variables in any subroutine which called you. It will only show
those variables which are in scope at the point of the call.

%prep
%setup -q -n PadWalker-%{version}

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
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PadWalker*
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 1.96-0.2
- Add BuildRequires: perl(Data::Dumper)

* Mon Mar 11 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 1.96-0.1
- new upstream version
- Add BuildRequires: perl-devel to get CORE/config.h dependency.
- Add BuildRequires: perl(Test::Harness)to build under mock.

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 1.9-1
- new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.7-2
- Rebuild for perl 5.10 (again)

* Thu Feb 21 2008 Steven Pritchard <steve@kspei.com> 1.7-1
- Update to 1.7.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6-2
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 1.6-1
- Update to 1.6.
- Use fixperms macro instead of our own chmod incantation.
- Reformat to match cpanspec output.

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-2
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Jan  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5-1
- Update to 1.5.

* Thu Jan  4 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.3-1
- Update to 1.3.

* Wed Nov 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.2-1
- Update to 1.2.

* Mon Oct 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.1-1
- Update to 1.1.

* Sun Sep 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-2
- Rebuild for FC6.

* Fri May 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.0-1
- First build.
