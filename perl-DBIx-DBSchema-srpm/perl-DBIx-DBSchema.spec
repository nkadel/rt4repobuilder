Name:           perl-DBIx-DBSchema
Version:        0.44
Release:        2%{?dist}
Summary:        Database-independent schema objects

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DBIx-DBSchema/
Source0:	http://www.cpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-%{version}.tar.gz

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
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 26 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.44-1
- Upstream update.
- Spec cleanup.
- Fix bogus changelog entry.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.40-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 0.40-2
- Perl 5.16 rebuild

* Thu Jan 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.40-1
- Upstream update.
- Modernize specfile.

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.39-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.39-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 23 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.39-1
- Upstream update.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.38-2
- Mass rebuild with perl-5.12.0

* Mon Mar 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-1
- Upstream update.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.36-5
- rebuild against perl 5.10.1

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

* Mon Oct 10 2005  Ralf Corsépius <rc040203@freenet.de> - 0.27-1
- Initial package.
- FE submission.
 
