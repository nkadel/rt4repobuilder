Name:           perl-DBIx-DBSchema
Version:        0.38
#Release:        1%{?dist}
Release:        0.1%{?dist}
Summary:        Database-independent schema objects

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DBIx-DBSchema/
Source0:	http://www.cpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(DBI)
BuildRequires:	perl(FreezeThaw)

# Required by the tests
BuildRequires:	perl(DBD::Pg) >= 1.32

%description
DBIx::DBSchema objects are collections of DBIx::DBSchema::Table objects and 
represent a database schema.

This module implements an OO-interface to database schemas. Using this module, 
you can create a database schema with an OO Perl interface. You can read the
schema from an existing database. You can save the schema to disk and restore
it a different process. Most importantly, DBIx::DBSchema can write SQL CREATE
statements statements for different databases from a single source.

Currently supported databases are MySQL and PostgreSQL. 

%prep
%setup -q -n DBIx-DBSchema-%{version}
chmod -x README Changes
find -name '*.pm' -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.30-0.1
- Port to RHEL 7

* Mon Mar 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-1
- Upstream update.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.36-2
- rebuild for new perl

* Sat Dec 22 2007 Ralf Corsépius <rc040203@freenet.de> - 0.36-1
- Upstream update.
- Remove DBIx-DBSchema-0.28-version.diff.

* Wed Oct 31 2007 Ralf Corsépius <rc040203@freenet.de> - 0.35-1
- Upstream update.

* Thu Sep 06 2007 Ralf Corsépius <rc040203@freenet.de> - 0.34-1
- Upstream update.
- Update license tag.

* Mon Jul 02 2007 Ralf Corsépius <rc040203@freenet.de> - 0.33-1
- Upstream update.

* Thu Apr 19 2007 Ralf Corsépius <rc040203@freenet.de> - 0.32-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.31-2
- Mass rebuild.

* Sat Apr 22 2006  Ralf Corsépius <rc040203@freenet.de> - 0.31-1
- Upstream update.

* Sun Feb 19 2006  Ralf Corsépius <rc040203@freenet.de> - 0.30-1
- Upstream update.

* Wed Dec 21 2005  Ralf Corsépius <rc040203@freenet.de> - 0.28-2
- Apply work around to CPAN incompatibility (PR #175468, J.V. Dias).

* Mon Dec 05 2005  Ralf Corsépius <rc040203@freenet.de> - 0.28-1
- Upstream update.

* Sun Nov 06 2005  Ralf Corsépius <rc040203@freenet.de> - 0.27-2
- Change URL (PR #170384, Paul Howard).

* Tue Oct 10 2005  Ralf Corsépius <rc040203@freenet.de> - 0.27-1
- Initial package.
- FE submission.
 
