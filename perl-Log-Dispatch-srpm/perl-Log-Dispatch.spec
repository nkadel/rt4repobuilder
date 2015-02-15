# Supported rpmbuild options:
#
# --with network/--without network
#    include/exclude networked tests, which work in mock, but don't work in koji
#    Default: --without (Exclude tests, which don't work in koji)
%bcond_with	network

# --with release_tests ... also check "RELEASE_TESTS".
#     Default: --without (Exclude tests)
%bcond_with	release_tests

Name:           perl-Log-Dispatch
Version:        2.41
#Release:        1%{?dist}.1
Release:        0.1%{?dist}.1
Summary:        Dispatches messages to one or more outputs
Group:          Development/Libraries
License:        Artistic 2.0
URL:            http://search.cpan.org/dist/Log-Dispatch/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/Log-Dispatch-%{version}.tar.gz

# Hacks to make spell checking tests work with hunspell
Patch0:         Log-Dispatch-2.38.diff
BuildArch:      noarch

BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Mail::Send)
BuildRequires:  perl(Mail::Sender)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(MIME::Lite)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Params::Validate) >= 0.15
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog) >= 0.25
BuildRequires:  perl(warnings)

# testsuite
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  /usr/sbin/sendmail

%if %{with release_tests} 
# for improved tests
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Spelling)
BuildRequires:  hunspell-en
BuildRequires:  perl(Test::CPAN::Changes)

%if %{with network}
BuildRequires:  perl(Test::Pod::No404s)
# Required by t/release-pod-no404s.t
# Likely a bug underneath of Test::Pod::No404s
BuildRequires:  perl(LWP::Protocol::https)
%endif
%endif

# Ouch - Introduced by upstream in 2.40
Conflicts:	perl(Log::Dispatch::File::Stamped) >= 0.10

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level.  It is designed to be easily subclassed, both for creating a
new dispatcher object and particularly for creating new outputs.

%prep
%setup -q -n Log-Dispatch-%{version}
%patch0 -p1
sed -i -e "s,set_spell_cmd(.*),set_spell_cmd(\'hunspell -l\')," t/release-pod-spell.t

%build
%{__perl} Makefile.PL installdirs=vendor
make

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test %{?with_release_tests:RELEASE_TESTING=1} LOG_DISPATCH_TEST_EMAIL="root@localhost.localdomain"

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Log/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Feb 10 2015 Nico Kadel-Garcia <nkadel@gmail.com > - 2.41-0.1
- Roll back release number for RHEL 6 compilation.

* Thu Jan 23 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.41-1.1
- sendmail needed for tests

* Fri Aug 16 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.41-1
- Upstream update.
- Spec cleanup.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 2.40-2
- Perl 5.18 rebuild

* Fri Jul 12 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.40-1
- Upstream update.
- Add Conflicts: perl(Log::Dispatch::File::Stamped) >= 0.10.
- Add %%bcond_with release_tests (Default to without, because RELEASE_TESTING
  is currently broken).

* Wed Apr 17 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.38-1
- Upstream update.

* Mon Feb 04 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.35-1
- Upstream update.

* Wed Dec 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.34-3
- Add %%bcond_with network (Test::Pod::No404 based tests fail in koji).

* Wed Dec 12 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.34-2
- Fix broken condition to BR: perl(Test::Pod::No404s).
- Conditionally BR: perl(LWP::Protocol::https).

* Tue Dec 11 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.34-1
- Upstream update.
- Update BR:s.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 2.29-2
- Perl 5.16 rebuild

* Mon Feb 06 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.29-1
- Upstream update.
- Remove --with mailtests build option (unnecessary).
- Remove Log-Dispatch-2.11-enable-mail-tests.patch (rotten, obsolete).
- Rework spec.
- Enable release tests.
- Make hunspell checks working.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.27-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 03 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.27-1
- update to 2.27

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.22-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.22-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.22-2
- BR: perl(Test::Kwalitee).

* Wed Nov 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.22-1
- Upstream update.

* Fri Mar 14 2008 Ralf Corsépius <rc040203@freenet.de> - 2.21-1
- Upstream update.
- BR: perl(Apache2::Log) instead of mod_perl.
- Add BR: Test::Pod::Coverage, activate IS_MAINTAINER checks.

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.20-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.20-1
- bump to 2.20

* Sat Jun  9 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.18-1
- Update to 2.18.

* Wed Dec 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.16-1
- Update to 2.16.
- Removed perl(IO::String) from the BR list (no longer needed).

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.15-2
- New build requirement: perl(IO::String).

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.15-1
- Update to 2.15.

* Sat Nov 25 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.14-2
- Log-Dispatch-2.11-mod_perl2.patch no longer needed.

* Sat Nov 25 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.14-1
- Update to 2.14.

* Tue Sep 26 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.13-1
- Update to 2.13.

* Wed Aug  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.12-1
- Update to 2.12.

* Wed Feb 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.11-4
- Rebuild for FC5 (perl 5.8.8).

* Thu Sep 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.11-3
- Exclude mod_perl from the requirements list
  (overkill for most applications using Log::Dispatch).

* Mon Sep 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.11-2
- Better mod_perl handling.

* Fri Sep 09 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.11-1
- First build.
