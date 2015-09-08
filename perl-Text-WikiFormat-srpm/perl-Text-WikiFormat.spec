Name:           perl-Text-WikiFormat
Version:        0.79
#Release:        4%{?dist}
Release:        0.4%{?dist}
Summary:        Translate Wiki formatted text into other formats

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Text-WikiFormat/
Source0:        http://www.cpan.org/authors/id/C/CH/CHROMATIC/Text-WikiFormat-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The original Wiki web site had a very simple interface to edit and to
add pages.  Its formatting rules are simple and easy to use.  They are
also easy to translate into other, more complicated markup languages
with this module.  It creates HTML by default, but can produce valid
POD, DocBook, XML, or any other format imaginable.


%prep
%setup -q -n Text-WikiFormat-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*


%check
PERL_RUN_ALL_TESTS=1 ./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ARTISTIC Changes GPL README
%{perl_vendorlib}/Text/
%{_mandir}/man3/*.3pm*


%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nakdel@gmail.com> - 0.29-0.4
- Port to RHEL 7, roll back release to avoid upstream repository conflict

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.79-2
Rebuild for new perl

* Fri Jun 29 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.79-1
- Update to 0.79.

* Fri Mar 31 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.78-1
- Update to 0.78.

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.77-2
- Rebuild for FC5 (perl 5.8.8).

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.77-1
- Update to 0.77.

* Thu Sep  1 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.76-2
- Disabled the signature test.

* Fri Aug 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.76-1
- First build.
