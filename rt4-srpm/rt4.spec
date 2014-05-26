#
# Copyright (c) 2005-2013, Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# Supported rpmbuild options:
#
# --with gd/--without gd 
#	enable/disable gd support
#	Default: --with (had been default in rt < 3.8.0)
#%if 0%{?fedora}
%bcond_without gd 
#%else
#%bcond_with devel_mode
#%endif

# --with graphviz/--without graphviz
#	enable/disable graphiz support
#	Default: --without (missing deps)
%bcond_with graphviz

# --with devel_mode/--without devel_mode
#	enable/disable building/installing devel files
#	Default: --with
%bcond_without devel_mode

# --with gpg/--without gpg
#	enable/disable building gpg support
#	Default: --without
%bcond_with gpg

# --with runtests
#	run testsuite when building the rpm
#	Default: without (doesn't work in chroots.)
%bcond_with runtests

%global RT4_BINDIR		%{_sbindir}
%global RT4_LIBDIR		%{perl_vendorlib}
%global RT4_WWWDIR		%{_datadir}/rt4/html
%global RT4_LEXDIR		%{_datadir}/rt4/po
%global RT4_LOGDIR		%{_localstatedir}/log/rt4
%global RT4_CACHEDIR		%{_localstatedir}/cache/rt4
%global RT4_LOCALSTATEDIR	%{_localstatedir}/lib/rt4

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Make sure perl_testdir is defined 
%{!?perl_testdir:%global perl_testdir %{_libexecdir}/perl5-tests}

Name:		rt4
Version:	4.0.19
Release:	0.1%{?dist}
Summary:	Request tracker 4

Group:		Applications/Internet
License:	GPLv2+
URL:		http://www.bestpractical.com/rt
Source0:	http://www.bestpractical.com/pub/rt/release/rt-%{version}.tar.gz
Source1:	README.tests
Source3:	rt4.conf.in
Source4:	README.fedora.in
Source5:	rt4.logrotate.in

#Patch1: 0001-Remove-configure-time-generated-files.patch
Patch2: 0002-Add-Fedora-configuration.patch
Patch3: 0003-Add-missing-shebangs.patch
Patch4: 0004-Remove-fixperms-font-install.patch
Patch5: 0005-Broken-test-dependencies.patch
Patch6: 0006-Use-usr-bin-perl-instead-of-usr-bin-env-perl.patch
# No longer needed with rt-4.0.19
#Patch7: 0007-Fix-permissions.patch

BuildArch:	noarch

# For Debian compatibility
Provides:	request-tracker3 = %{version}-%{release}
# For RHEL dependencies
Provides:	rt = %{version}-%{release}

# Manage perl macro filtering
BuildRequires: ghc-rpm-macros

# Needed for filert-requires "/d" syntax
%if 0%{?rhel}
BuildRequires: redhat-rpm-config
%endif

# Obsoletes:	rt3 < %{version}-%{release}
Conflicts:	rt3

# This list is alpha sorted
BuildRequires: perl(Apache::DBI)
BuildRequires: perl(Apache::Session) >= 1.53
BuildRequires: perl(Cache::Simple::TimedExpiry)
BuildRequires: perl(Calendar::Simple)
BuildRequires: perl(CGI::Cookie) >= 1.20
BuildRequires: perl(CGI::Emulate::PSGI)
BuildRequires: perl(CGI::PSGI)
BuildRequires: perl(Class::Accessor) >= 0.34
BuildRequires: perl(Class::ReturnValue) >= 0.40
BuildRequires: perl(Convert::Color)
BuildRequires: perl(CPAN)
BuildRequires: perl(CSS::Squish) >= 0.06
BuildRequires: perl(Data::ICal)
BuildRequires: perl(Date::Format)
BuildRequires: perl(DateTime) >= 0.44
BuildRequires: perl(DateTime::Locale) >= 0.40
BuildRequires: perl(DBD::mysql) >= 2.1018
BuildRequires: perl(DBI) >= 1.37
BuildRequires: perl(DBIx::SearchBuilder) >= 1.59
BuildRequires: perl(Devel::GlobalDestruction)
BuildRequires: perl(Devel::StackTrace) >= 1.19
BuildRequires: perl(Digest::base)
BuildRequires: perl(Digest::MD5) >= 2.27
BuildRequires: perl(Email::Address)
BuildRequires: perl(Encode) >= 2.39
BuildRequires: perl(Errno)
%{?with_devel_mode:BuildRequires: perl(File::Find)}
BuildRequires: perl(File::Glob)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(File::Temp) >= 0.19
%{?with_gd:BuildRequires: perl(GD)}
%{?with_gd:BuildRequires: perl(GD::Graph)}
%{?with_gd:BuildRequires: perl(GD::Text)}
%{?with_gpg:BuildRequires: perl(GnuPG::Interface)}
%{?with_graphviz:BuildRequires: perl(GraphViz)}
BuildRequires: perl(Getopt::Long) >= 2.24
BuildRequires: perl(HTML::Entities)
%{?with_devel_mode:BuildRequires: perl(HTML::Form)}
BuildRequires: perl(HTML::FormatText)
BuildRequires: perl(HTML::Mason) >= 1.43
#BuildRequires: perl(HTML::Mason::PSGIHandler) >= 1.43
BuildRequires: perl(HTML::Mason::PSGIHandler) >= 0.52
BuildRequires: perl(HTML::Quoted)
BuildRequires: perl(HTML::RewriteAttributes) >= 0.05
BuildRequires: perl(HTML::Scrubber) >= 0.08
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(HTTP::Server::Simple) >= 0.34
BuildRequires: perl(HTTP::Server::Simple::Mason) >= 0.09
%{?with_graphviz:BuildRequires: perl(IPC::Run)}
BuildRequires: perl(IPC::Run3)
%{?with_graphviz:BuildRequires: perl(IPC::Run::SafeHandles)}
BuildRequires: perl(JavaScript::Minifier)
BuildRequires: perl(JSON)
BuildRequires: perl(JSON::PP)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Locale::Maketext) >= 1.06
BuildRequires: perl(Locale::Maketext::Fuzzy)
BuildRequires: perl(Locale::Maketext::Lexicon) >= 0.32
BuildRequires: perl(Locale::PO)
BuildRequires: perl(Log::Dispatch) >= 2.0
%{?with_devel_mode:BuildRequires: perl(Log::Dispatch::Perl)}
BuildRequires: perl(LWP)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mail::Mailer) >= 1.57
BuildRequires: perl(MIME::Entity) >= 5.425
BuildRequires: perl(MIME::Types)
%{?with_devel_mode:BuildRequires: perl(Module::Refresh) >= 0.03}
BuildRequires: perl(Module::Versions::Report) >= 1.05
BuildRequires: perl(Net::CIDR)
BuildRequires: perl(Net::Server)
BuildRequires: perl(Net::Server::PreFork)
BuildRequires: perl(Net::SMTP)
%{?with_gpg:BuildRequires: perl(PerlIO::eol)}
BuildRequires: perl(Plack)
BuildRequires: perl(Plack::Handler::Starlet)
%{?with_devel_mode:BuildRequires: perl(Plack::Middleware::Test::StashWarnings) >= 0.06}
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Regexp::Common::net::CIDR)
BuildRequires: perl(Regexp::IPv6)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable) >= 2.08
%{?with_devel_mode:BuildRequires: perl(String::ShellQuote)}
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Term::ReadLine)
%{?with_devel_mode:BuildRequires: perl(Email::Abstract)}
%{?with_devel_mode:BuildRequires: perl(Test::Builder) >= 0.77}
%{?with_devel_mode:BuildRequires: perl(Test::Deep)}
%{?with_devel_mode:BuildRequires: perl(Test::Email)}
%{?with_devel_mode:BuildRequires: perl(Test::Expect) >= 0.31}
%{?with_devel_mode:BuildRequires: perl(Test::HTTP::Server::Simple) >= 0.09}
%{?with_devel_mode:BuildRequires: perl(Test::MockTime)}
%{?with_devel_mode:BuildRequires: perl(Test::NoWarnings)}
%{?with_devel_mode:BuildRequires: perl(Test::Warn)}
%{?with_devel_mode:BuildRequires: perl(Test::WWW::Mechanize)} >= 1.30
%{?with_devel_mode:BuildRequires: perl(Test::WWW::Mechanize::PSGI)}
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(Text::Password::Pronounceable)
BuildRequires: perl(Text::Quoted) >= 2.02
BuildRequires: perl(Text::Template)
BuildRequires: perl(Text::WikiFormat) >= 0.76
BuildRequires: perl(Text::Wrapper)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(Tree::Simple) >= 1.04
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(URI) >= 1.60
#%{?with_devel_mode:BuildRequires: perl(Web::Scraper)}
%{?with_devel_mode:BuildRequires: perl(WWW::Mechanize)}
BuildRequires: perl(XML::RSS) >= 1.05
%{?with_devel_mode:BuildRequires: perl(XML::Simple)}

%{?with_runtests:BuildRequires: perl(DBD::SQLite)}
# %{?with_runtests:BuildRequires: perl(DBD::mysql)}
# %{?with_runtests:BuildRequires: perl(DBD::Pg)}
%{?with_runtests:BuildRequires: perl(Test::Warn)}
%{?with_runtests:BuildRequires: perl(Test::MockTime)}
%{?with_runtests:BuildRequires: perl(String::ShellQuote)}
%{?with_runtests:BuildRequires: perl(Test::Pod) >= 1.14}
%{?with_runtests:BuildRequires: perl(PerlIO::eol)}
%{?with_runtests:BuildRequires: perl(Test::Expect)}

BuildRequires:	/usr/bin/pod2man
BuildRequires:	/usr/sbin/apachectl

# the original sources carry bundled versions of these ...
BuildRequires:  google-droid-sans-fonts
Requires:  /usr/share/fonts/google-droid/DroidSansFallback.ttf
Requires:  /usr/share/fonts/google-droid/DroidSans.ttf
# ... we use symlinks to the system-wide versions ...
BuildRequires:  /usr/share/fonts/google-droid/DroidSansFallback.ttf
BuildRequires:  /usr/share/fonts/google-droid/DroidSans.ttf

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Requires(postun): %{__rm}

# rpm doesn't catch these:
Requires: perl(Apache::Session)
Requires: perl(Calendar::Simple)
Requires: perl(CSS::Squish)
Requires: perl(Data::ICal)
Requires: perl(Data::ICal::Entry::Event)
Requires: perl(Email::Address)
Requires: perl(File::Find)
%{?with_gd:Requires: perl(GD::Text)}
%{?with_gd:Requires: perl(GD::Graph::bars)}
%{?with_gd:Requires: perl(GD::Graph::pie)}
%{?with_gpg: Requires: perl(GnuPG::Interface)}
#Requires: perl(HTML::Quoted)
#Requires: perl(HTTP::Server::Simple::Mason)
#Requires: perl(HTML::Mason::Request)
Requires: perl(I18N::LangTags::List)
Requires: perl(Locale::Maketext::Fuzzy)
#Requires: perl(IPC::Run3)
Requires: perl(LWP::MediaTypes)
Requires: perl(mod_perl2)
Requires: perl(Module::Versions::Report)
Requires: perl(Net::Server::PreFork)
Requires: perl(Plack::Middleware::Test::StashWarnings) >= 0.06
Requires: perl(Plack::Handler::Starlet)
Requires: perl(Net::Server::PreFork)
Requires: perl(Plack::Middleware::Test::StashWarnings) >= 0.06
Requires: perl(Plack::Handler::Starlet)
Requires: perl(Text::Quoted)
Requires: perl(Text::WikiFormat)
Requires: perl(URI) >= 1.60
Requires: perl(XML::RSS)

# rpm fails to add these:
Provides: perl(RT::Shredder::Exceptions)
Provides: perl(RT::Shredder::Record)
Provides: perl(RT::SQL)
Provides: perl(RT::Shredder::Transaction)
Provides: perl(RT::Tickets::SQL)
Provides: perl(RT::Tickets_Overlay_SQL)
Provides: perl(RT::Tickets_SQL)
Conflicts:	rt3
Conflicts:	rt3-mailgate

# Split out. Technically, not actually necessary, but ... let's keep it for now.
Requires: rt4-mailgate

%{?perl_default_filter}

# Keep SpamAssassin optional
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::SpamAssassin\\)
# Keep FCGI optional
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(FCGI::ProcManager\\)
# Filter bogus requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(\\)
# Work-around rpm's depgenerator defect: 
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DBIx::SearchBuilder::Handle::\\)

# Filter redundant provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(RT\\)$
# Filter bogus provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(HTML::Mason
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(IO::Handle::CRLF\\)$


%description
RT is an enterprise-grade ticketing system which enables a group of people
to intelligently and efficiently manage tasks, issues, and requests submitted
by a community of users.


%package mailgate
Summary: rt4's mailgate utility
Group:   Applications/Internet
# rpm doesn't catch these:
Requires:	perl(Pod::Usage)
Requires:	perl(HTML::TreeBuilder)
Requires:	perl(HTML::FormatText)
Conflicts:	rt3
Conflicts:	rt3-mailgate
Provides:	rt-mailgate = %{version}-%{release}

%description mailgate
%{summary}


%if %{with devel_mode}
%package tests
Summary:	Test suite for package rt4
Group:		Development/Debug
Requires:	%{name} = %{version}-%{release}
Requires(postun): %{__rm}
Requires:	/usr/bin/prove
Requires:	perl(RT::Test)
# rpm doesn't catch these:
Requires:	perl(DBD::SQLite)
Requires:	perl(GnuPG::Interface)
# Bug: The testsuite unconditionally depends upon perl(GraphViz)
Requires:	perl(GraphViz)
Requires:	perl(PerlIO::eol)
Requires:	perl(Plack::Handler::Apache2)
Requires:       perl(String::ShellQuote)
Requires:       perl(Test::Deep)
Requires:	perl(Test::MockTime)
Conflicts:	rt3-tests

%description tests
%{summary}

%postun tests
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{perl_testdir}/%{name}
fi


%package -n perl-RT-Test
Summary: rt4's test utility module
Group:   Applications/Internet
Requires:	rt4 = %{version}-%{release}
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# rpm doesn't catch these:
Requires:       perl(Test::WWW::Mechanize::PSGI)

%description -n perl-RT-Test
%{summary}

%endif # devel_mode

%prep
%setup -q -n rt-%{version}

sed -e 's,@RT4_CACHEDIR@,%{RT4_CACHEDIR},' %{SOURCE4} \
  > README.fedora
sed -e 's,@RT4_LOGDIR@,%{RT4_LOGDIR},' %{SOURCE5} \
  > rt4.logrotate

# Fixup the tarball shipping with broken permissions
find \( -type f -a -executable \) -exec chmod a-x {} \;
chmod +x configure install-sh

# Upstream tarball contains configure-time generated files
# find bin sbin etc -name '*.in' | while read a; do d=$(echo "$a" | sed 's,\.in$,,'); rm "$d"; done

#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
#%patch7 -p1

# Propagate rpm's directories to config.layout
cat << \EOF >> config.layout

#   Fedora directory layout.
<Layout Fedora>
  bindir:		%{RT4_BINDIR}
  sysconfdir:		%{_sysconfdir}/rt4
  libdir:		%{RT4_LIBDIR}
  manualdir:		%{_pkgdocdir}/docs
  lexdir:		%{RT4_LEXDIR}
  localstatedir:	%{RT4_LOCALSTATEDIR}
  htmldir:		%{RT4_WWWDIR}
  fontdir:		%{_datadir}/rt4/fonts
  logfiledir:		%{RT4_LOGDIR}
  masonstatedir:	%{RT4_CACHEDIR}/mason_data
  sessionstatedir:	%{RT4_CACHEDIR}/session_data
  customdir:		%{_prefix}/local/lib/rt4
  custometcdir:		%{_prefix}/local/etc/rt4
  customhtmldir:	${customdir}/html
  customlexdir:		${customdir}/po
  customlibdir:		${customdir}/lib
</Layout>
EOF

# Comment out the Makefile trying to change groups/owners
# Fix DESTDIR support
sed -i \
	-e 's,	chgrp,	: chrgp,g' \
	-e 's,	chown,	: chown,g' \
	-e 's,$(DESTDIR)/,$(DESTDIR),g' \
	-e 's,-o $(BIN_OWNER) -g $(RTGROUP),,g' \
Makefile.in

# Make scripts executable
# find t \( -name '*.t' -o -name '*.pl' \) -exec chmod +x {} \;
# chmod +x t/web/passthrough-jsmin

# make *.ins non-executable
# chmod -x bin/*.in sbin/*.in

%build
%configure \
--with-apachectl=/usr/sbin/apachectl \
--with-web-user=apache --with-web-group=apache \
--with-db-type=mysql \
--enable-layout=Fedora \
--with-web-handler=modperl2 \
--libdir=%{RT4_LIBDIR} \
%{?with_graphviz:--enable-graphviz}%{!?with_graphviz:--disable-graphviz} \
%{?with_gd:--enable-gd}%{!?with_gd:--disable-gd} \
%{?with_gpg:--enable-gpg}%{!?with_gpg:--disable-gpg}

make %{?_smp_mflags}

# Explicitly check for devel-mode deps
%{?with_devel_mode:%{__perl} ./sbin/rt-test-dependencies --verbose --with-mysql --with-modperl2 --with-dev}

# Generate man-pages
for file in \
bin/rt \
bin/rt-crontool \
bin/rt-mailgate \
sbin/rt-attributes-viewer \
sbin/rt-clean-sessions \
sbin/rt-dump-metadata \
sbin/rt-email-dashboards \
sbin/rt-email-digest \
sbin/rt-email-group-admin \
sbin/rt-fulltext-indexer \
sbin/rt-preferences-viewer \
sbin/rt-server \
sbin/rt-server.fcgi \
sbin/rt-session-viewer \
sbin/rt-setup-database \
sbin/rt-setup-fulltext-index \
sbin/rt-shredder \
sbin/rt-validator \
sbin/standalone_httpd \
; do
/usr/bin/pod2man $file > $file.1
done


%install
make install DESTDIR=${RPM_BUILD_ROOT}

# We don't want CPAN
rm -f ${RPM_BUILD_ROOT}%{_sbindir}/rt-test-dependencies

# Install apache configuration
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
sed -e 's,@RT4_WWWDIR@,%{RT4_WWWDIR},g' \
  -e 's,@RT4_BINDIR@,%{RT4_BINDIR},g' \
  %{SOURCE3} > ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/rt4.conf

mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
for file in bin/*.1 sbin/*.1; do
install -m 0644 $file ${RPM_BUILD_ROOT}%{_mandir}/man1
done

if [ "%{_bindir}" != "%{RT4_BINDIR}" ]; then
  mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
  mv ${RPM_BUILD_ROOT}%{RT4_BINDIR}/rt \
    ${RPM_BUILD_ROOT}%{_bindir}
fi

install -d -m755 ${RPM_BUILD_ROOT}%{_prefix}/local/etc/rt4
install -d -m755 ${RPM_BUILD_ROOT}%{_prefix}/local/lib/rt4
install -d -m755 ${RPM_BUILD_ROOT}%{_prefix}/local/lib/rt4/html
install -d -m755 ${RPM_BUILD_ROOT}%{_prefix}/local/lib/rt4/po
install -d -m755 ${RPM_BUILD_ROOT}%{_prefix}/local/lib/rt4/lib

install -d -m755 ${RPM_BUILD_ROOT}%{RT4_LOGDIR}

# install log rotation stuff
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 rt4.logrotate ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/rt4

install -d -m755 ${RPM_BUILD_ROOT}%{RT4_LOCALSTATEDIR}

install -d -m755 ${RPM_BUILD_ROOT}%{_sysconfdir}/rt4/upgrade
cp -R etc/upgrade/* ${RPM_BUILD_ROOT}%{_sysconfdir}/rt4/upgrade
rm -f ${RPM_BUILD_ROOT}%{_sysconfdir}/rt4/upgrade/*.in

install -d -m755 ${RPM_BUILD_ROOT}%{_datadir}/rt4/fonts
ln -s /usr/share/fonts/google-droid/DroidSans.ttf ${RPM_BUILD_ROOT}%{_datadir}/rt4/fonts
ln -s /usr/share/fonts/google-droid/DroidSansFallback.ttf ${RPM_BUILD_ROOT}%{_datadir}/rt4/fonts

install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
cp -R t ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
cp %{SOURCE1} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}

# pod.t can't be run outside of the source-tree
rm -rf ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/t/pod.t

# Some of the tests want t/../share/html
install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share
ln -s %{RT4_WWWDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share/html

# This file should not be installed
rm ${RPM_BUILD_ROOT}%{RT4_LEXDIR}/*.pot

# Fix permissions
find ${RPM_BUILD_ROOT}%{RT4_WWWDIR} \
  -type f -exec chmod a-x {} \;

%check
# The tests don't work in buildroots, they
# - require to be run as root
# - require an operational rt4 system
%{?with_runtests:make test}

%postun
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{RT4_CACHEDIR}
fi


%files
%defattr(-,root,root,-)
%doc COPYING README README.fedora
%{_bindir}/*
%{_sbindir}/*
%exclude %{_sbindir}/rt-mailgate
%{_mandir}/man1/*
%exclude %{_mandir}/man1/rt-mailgate*
%{RT4_LIBDIR}/*
%exclude %{RT4_LIBDIR}/RT/Test*
%attr(0700,apache,apache) %{RT4_LOGDIR}

%dir %{_sysconfdir}/rt4
%attr(-,root,root)%{_sysconfdir}/rt4/upgrade
%attr(-,root,root)%{_sysconfdir}/rt4/acl*
%attr(-,root,root)%{_sysconfdir}/rt4/schema*
%attr(-,root,root)%{_sysconfdir}/rt4/init*
%config(noreplace) %attr(0640,apache,apache) %{_sysconfdir}/rt4/RT_*

%config(noreplace) %{_sysconfdir}/logrotate.d/rt4

%dir %{_datadir}/rt4
%{RT4_WWWDIR}
%{RT4_LEXDIR}
%{_datadir}/rt4/fonts

%config(noreplace) %{_sysconfdir}/httpd/conf.d/rt4.conf

%dir %{RT4_CACHEDIR}
%attr(0770,apache,apache) %{RT4_CACHEDIR}/mason_data
%attr(0770,apache,apache) %{RT4_CACHEDIR}/session_data

%if "%{RT4_LOCALSTATEDIR}" != "%{RT4_CACHEDIR}"
%dir %{RT4_LOCALSTATEDIR}
%endif

%ghost %{_prefix}/local/lib/rt4
%ghost %{_prefix}/local/etc/rt4

%files mailgate
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/rt-mailgate
%{_mandir}/man1/rt-mailgate*

%if %{with devel_mode}
%files tests
%defattr(-,root,root,-)
%{perl_testdir}/%{name}

%files -n perl-RT-Test
%defattr(-,root,root,-)
%dir %{RT4_LIBDIR}/RT
%{RT4_LIBDIR}/RT/Test*
%endif

%changelog
* Sun Dec 08 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.18-0.20131208.0
- Upgrade to rt-4.0.18.
- BR: perl(Locale::PO).

* Mon Sep 23 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.17-0.20130923.0
- Let rt4-tests R: perl(Test::MockTime), perl(String::ShellQuote), perl(Test::Deep).
- Let perl-RT-Tests R: perl(Test::WWW::Mechanize::PSGI).

* Sun Sep 22 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.17-0.20130922.0
- Upgrade to rt-4.0.17.
- Adjust BRs.
- Reflect UnversionedDocDir changes.

* Mon Dec 31 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.8-0.20121231.0
- Require: perl(HTML::Quoted).
- Minor spec cleanup.

* Fri Dec 28 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.8-0.20121228.0
- Add mod_authz_core.c support to rt4.conf.

* Sat Dec 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.8-0.20121222.0
- Update to rt-4.0.8.
- Let rt4 conflict with rt3 instead of obsolete it.
- Rebase patches.

* Thu Feb 09 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.5-0.20120209.1
- Conditionally define %%perl_testdir.
- Comment out duplicate Requires:.

* Mon Feb 06 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.5-0.20120206.1
- Let *-tests unconditionally R: perl(GraphViz).

* Sun Feb 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.5-0.20120205.1
- Reflect upstream having stopped to ship autom4te.cache, config.log, config.status.

* Sat Feb 04 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.0.5-0.20120204.1
- First public release.
