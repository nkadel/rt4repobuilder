Name:           perl-Parallel-Scoreboard
Version:        0.07
#Release:        4%%{?dist}
Release:        0.4%{?dist}
Summary:        Scoreboard for monitoring status of many processes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Parallel-Scoreboard/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Parallel-Scoreboard-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Base::Filter)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Module)

# Run-time deps
BuildRequires: perl(Class::Accessor::Lite)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Path)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(JSON)
BuildRequires: perl(POSIX)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Provides: perl(Parallel::Scoreboard) = %{version}

%description
Parallel::Scoreboard is a pure-perl implementation of a process scoreboard.
By using the module it is easy to create a monitor for many worker process,
like the status module of the Apache HTTP server.

%prep
%setup -q -n Parallel-Scoreboard-%{version}

# Remove bundled modules
for f in inc/Test/More.pm inc/File/Temp.pm inc/Spiffy.pm \
    inc/Test/Base.pm inc/Test/Base/Filter.pm \
    inc/Test/Builder.pm inc/Test/Builder/Module.pm \
    inc/Test/Warn.pm; do
  pat=$(echo "$f" | sed 's,/,\\/,g;s,\.,\\.,g')
  rm $f
  sed -i -e "/$pat/d" MANIFEST
done

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.07-0.4
- Roll back buld number for RHEL use

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.22 rebuild

* Mon Mar 09 2015 Petr Pisar <ppisar@redhat.com> - 0.07-2
- Remove reflexive build-time dependency (bug #1195803)

* Mon Feb 02 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.07-1
- Upstream update.
- Rework BRs.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-1
- Upstream update.
- Remove more bundled modules.
- Rework BRs.
- Modernize spec.

* Thu Sep 12 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.04-1
- Upstream update.
- Modernize spec.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.03-9
- Perl 5.18 rebuild
- Remove bundled modules Test::Builder and Test::Builder::Module because they
  have to match Test::More (CPAN RT#87136)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 0.03-6
- Perl 5.16 rebuild

* Mon Jan 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.03-5
- Add BR: perl(Digest::MD5) (Fix gcc-4.7 FTBFS).
- Modernize spec.
- Filter out unversioned R: perl(Class::Accessor::Lite).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.03-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Upstream update.
- Add BR: perl(Class::Accessor::Lite), perl(HTML::Entities), perl(JSON).

* Wed Jan 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.02-2
- Use system-wide versions of Test/More.pm and File/Temp.pm instead of
  bundled versions.

* Thu Jan 20 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
