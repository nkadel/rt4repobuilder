Name: 		perl-Cache-Simple-TimedExpiry
Version: 	0.27
#Release: 	6%{?dist}
Release: 	0.6%{?dist}
Summary: 	A lightweight cache with timed expiration
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Cache-Simple-TimedExpiry/
Source0: 	http://www.cpan.org/authors/id/J/JE/JESSE/Cache-Simple-TimedExpiry-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: 	noarch

BuildRequires:	perl(Test::More)
BuildRequires:	perl(ExtUtils::MakeMaker)
Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A lightweight cache with timed expiration

%prep
%setup -q -n Cache-Simple-TimedExpiry-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/Cache
%{_mandir}/man3/*

%changelog
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.27-4
- rebuild for new perl

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 0.27-3
- BR: perl(Test::More).

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 0.27-2
- Update license tag.
- BR: perl(ExtUtils::MakeMaker).

* Mon Nov 27 2006 Ralf Corsépius <rc040203@freenet.de> - 0.27-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.26-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.23-4
- Mass rebuild.

* Fri Feb 24 2006 Ralf Corsépius <rc040203@freenet.de> - 0.23-3
- Rebuild for perl-5.8.8.

* Fri Aug 26 2005 Ralf Corsepius <rc040203@freenet.de> - 0.23-2
- Spec cleanup.

* Mon Aug 22 2005 Ralf Corsepius <rc040203@freenet.de> - 0.23-1
- Spec cleanup.
- FE submission.
