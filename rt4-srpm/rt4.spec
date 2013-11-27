#
# Copyright (c) 2005-2012, Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# Supported rpmbuild options:
#
# --with gd/--without gd 
#	enable/disable gd support
#	Default: --with (had been default in rt < 3.8.0)
%bcond_without gd 

# --with graphviz/--without graphviz
#	enable/disable graphiz support
#	Default: --without (missing deps)
%bcond_with graphviz

# --with devel_mode/--without devel_mode
#	enable/disable building/installing devel files
#	Default: --with
#%if 0%{?fedora}
%bcond_without devel_mode
#%else
#%bcond_with devel_mode
#%endif

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

# Make sure perl_testdir is defined 
%{!?perl_testdir:%global perl_testdir %{_libexecdir}/perl5-tests}

Name:		rt4
Version:	4.0.17
Release:	0.2%{?dist}
Summary:	Request tracker 3

Group:		Applications/Internet
License:	GPLv2+
URL:		http://www.bestpractical.com/rt
Source0:	http://download.bestpractical.com/pub/rt/release/rt-%{version}.tar.gz
Source1:        README.tests
Source3:	rt4.conf.in
Source4:	README.fedora.in
Source5:	rt4.logrotate.in

#Patch0:		rt-%{version}-config.diff
Patch0:		rt-4.0.12-config.diff
#Patch1:		rt-%{version}-shebang.diff
#Patch2:		rt-%{version}-Makefile.diff
Patch2:		rt-4.0.12-Makefile.diff
#Patch3:		rt-%{version}-test-dependencies.diff

BuildArch:	noarch

# For Debian compatibility
Provides:	request-tracker3 = %{version}-%{release}

# Manage perl macro filtering
BuildRequires: ghc-rpm-macros

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
BuildRequires: perl(DBD::mysql) >= 2.1018
BuildRequires: perl(DBI) >= 1.37
BuildRequires: perl(DBIx::SearchBuilder) >= 1.59
BuildRequires: perl(Devel::GlobalDestruction)
BuildRequires: perl(Devel::StackTrace) >= 1.19
BuildRequires: perl(Digest::base)
BuildRequires: perl(Digest::MD5) >= 2.27
%{?with_devel_mode:BuildRequires: perl(Email::Abstract)}
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
#%{?with_devel_mode:BuildRequires: perl(IPC::Run3)}
BuildRequires: perl(IPC::Run3)
%{?with_graphviz:BuildRequires: perl(IPC::Run::SafeHandles)}
BuildRequires: perl(JSON)
BuildRequires: perl(Locale::Maketext) >= 1.06
BuildRequires: perl(Locale::Maketext::Fuzzy)
BuildRequires: perl(Locale::Maketext::Lexicon) >= 0.32
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
%{?with_devel_mode:BuildRequires: perl(Plack::Middleware::Test::StashWarnings)}
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Regexp::Common::net::CIDR)
BuildRequires: perl(Regexp::IPv6)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable) >= 2.08
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Term::ReadLine)
%{?with_devel_mode:BuildRequires: perl(Test::Builder) >= 0.77}
%{?with_devel_mode:BuildRequires: perl(Test::Deep)}
%{?with_devel_mode:BuildRequires: perl(Test::Email)}
%{?with_devel_mode:BuildRequires: perl(Test::Expect) >= 0.31}
%{?with_devel_mode:BuildRequires: perl(Test::HTTP::Server::Simple) >= 0.09}
%{?with_devel_mode:BuildRequires: perl(Test::HTTP::Server::Simple::StashWarnings)}
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
%{?with_devel_mode:BuildRequires: perl(WWW::Mechanize)}
BuildRequires: perl(XML::RSS) >= 1.05
%{?with_devel_mode:BuildRequires: perl(XML::Simple)}

%{?with_runtests:BuildRequires: perl(DBD::SQLite)}
%{?with_runtests:BuildRequires: perl(DBD::mysql)}
%{?with_runtests:BuildRequires: perl(DBD::Pg)}
%{?with_runtests:BuildRequires: perl(Log::Dispatch::Perl)}
%{?with_runtests:BuildRequires: perl(Test::WWW::Mechanize)}
%{?with_runtests:BuildRequires: perl(Test::Expect)}
%{?with_runtests:BuildRequires: perl(Test::Harness)}

BuildRequires:	/usr/bin/pod2man
BuildRequires:	/usr/sbin/apachectl

# the original sources carry bundled versions of these ...
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
Requires: perl(Data::ICal)
Requires: perl(Data::ICal::Entry::Event)
Requires: perl(Email::Address)
Requires: perl(File::Find)
%{?with_gd:Requires: perl(GD::Text)}
%{?with_gd:Requires: perl(GD::Graph::bars)}
%{?with_gd:Requires: perl(GD::Graph::pie)}
%{?with_gpg: Requires: perl(GnuPG::Interface)}
Requires: perl(I18N::LangTags::List)
Requires: perl(Locale::Maketext::Fuzzy)
Requires: perl(LWP::MediaTypes)
Requires: perl(mod_perl2)
Requires: perl(Module::Versions::Report)
Requires: perl(Text::Quoted)
Requires: perl(Text::WikiFormat)
#Requires: perl(URI) >= 1.99
Requires: perl(URI) >= 1.60
Requires: perl(URI::URL)
Requires: perl(XML::RSS)

# rpm fails to add these:
Provides: perl(RT::Shredder::Exceptions)
Provides: perl(RT::Shredder::Record)
Provides: perl(RT::Shredder::Transaction)
Provides: perl(RT::Tickets_Overlay_SQL)
Provides: perl(RT::SQL)
Provides: perl(RT::Tickets::SQL)
Provides: perl(RT::Tickets_SQL)
Conflicts:	rt3
Conflicts:	rt3-mailgate

# Split out. Technically, not actually necessary, but ... let's keep it for now.
Requires: rt4-mailgate

%if 0%{?fedora}
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
%endif

%if 0%{?rhel}
# RPM 4.8 style:
%{?perl_default_filter:
# Keep SpamAssassin optional
%filter_from_requires /^perl(Mail::SpamAssassin)/d
# Keep FCGI optional
%filter_from_requires /^perl(FCGI::ProcManager)/d
# Filter bogus requires
%filter_from_requires /^perl()/d
# Filter redundant provides
%filter_from_provides /^perl(RT)$/d
# Filter bogus provides
%filter_from_provides /^perl(HTML::Mason/d
%filter_from_provides /^perl(IO::Handle::CRLF)$/d
# Work-around rpm's depgenerator defect:
%filter_from_requires /^perl(DBIx::SearchBuilder::Handle::)$/d
%perl_default_filter
}
%endif

%description
RT is an enterprise-grade ticketing system which enables a group of people
to intelligently and efficiently manage tasks, issues, and requests submitted
by a community of users.


%package mailgate
Summary: rt4's mailgate utility.
Group:   Applications/Internet
# rpm doesn't catch these:
Requires:	perl(Pod::Usage)
Requires:	perl(HTML::TreeBuilder)
Requires:	perl(HTML::FormatText)
Conflicts:	rt3
Conflicts:	rt3-mailgate

%description mailgate
%{summary}


%if %{with devel_mode}
%package tests
Summary:	Test suite for package rt4
Group:		Development/Debug
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/prove
Requires(postun): %{__rm}
Requires:	perl(DBD::SQLite)  
Requires:	perl(GnuPG::Interface)  
Requires:	perl(PerlIO::eol)  
Requires:	perl(strict)  
Requires:	perl(Test::HTTP::Server::Simple::StashWarnings)  

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
Requires:       perl(Log::Dispatch::Perl)

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

# Upstream tarball contains temporary autotools-files
rm -rf autom4te.cache config.log config.status

# Upstream tarball contains configure-time generated files
find bin sbin etc -name '*.in' | while read a; do d=$(echo "$a" | sed 's,\.in$,,'); rm "$d"; done

%patch0 -p1
## Add /usr/bin/perl dynamically to api tests, instead of static patch
##%patch1 -p1
#find t/api -name \*.t | sort | while read name; do
#    cp $name $name.shebang
#    echo '/usr/bin/perl' > $name
#    cat $name.shebang >> $name
#done

%patch2 -p1
#%patch3 -p1

# Propagate rpm's directories to config.layout
cat << \EOF >> config.layout

#   Fedora directory layout.
<Layout Fedora>
  bindir:		%{RT4_BINDIR}
  sysconfdir:		%{_sysconfdir}/rt4
  libdir:		%{RT4_LIBDIR}
  manualdir:		%{_defaultdocdir}/%{name}-%{version}
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

# Fix up broken shebangs
sed -i \
 -e "s,^#!/usr/bin/env perl,#!%{__perl}," \
 -e "s,^#!/opt/perl/bin/perl,#!%{__perl}," \
t/*/*.t sbin/rt-message-catalog t/shredder/utils.pl

# Make scripts executable
find t \( -name '*.t' -o -name '*.pl' \) -exec chmod +x {} \;

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
/usr/bin/pod2man bin/rt > bin/rt.1
/usr/bin/pod2man bin/rt-crontool > bin/rt-crontool.1
/usr/bin/pod2man bin/rt-mailgate > bin/rt-mailgate.1

%install
make install DESTDIR=${RPM_BUILD_ROOT}

# Cleanup the mess rt's configuration leaves behind
rm -f ${RPM_BUILD_ROOT}%{_docdir}/README

# Win32 stuff
rm -f ${RPM_BUILD_ROOT}%{RT4_BINDIR}/mason_handler.svc

# We don't want CPAN
rm -f ${RPM_BUILD_ROOT}%{_sbindir}/rt-test-dependencies

# Bogus
rm -f ${RPM_BUILD_ROOT}%{RT4_LIBDIR}/RT.pm.in

# Unsupported
rm -f ${RPM_BUILD_ROOT}%{RT4_BINDIR}/*.scgi

# Install apache configuration
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
sed -e 's,@RT4_WWWDIR@,%{RT4_WWWDIR},g' \
  -e 's,@RT4_BINDIR@,%{RT4_BINDIR},g' \
  %{SOURCE3} > ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/rt4.conf

mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m 0644 bin/rt-mailgate.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m 0644 bin/rt-crontool.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

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

%if %{with devel_mode}
install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
cp -R t ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
cp %{SOURCE1} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}

# pod.t can't be run outside of the source-tree
rm -rf ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/t/pod.t

# Some of the tests want t/../share/html
install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share
ln -s %{RT4_WWWDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share/html
%endif # with devel_mode

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
%doc COPYING README README.Oracle
%{_bindir}/*
%{_sbindir}/*
%exclude %{_sbindir}/rt-mailgate
%{_mandir}/man1/*
%exclude %{_mandir}/man1/rt-mailgate*
%{RT4_LIBDIR}/*
%exclude %{RT4_LIBDIR}/RT/Test*
%attr(0700,apache,apache) %{RT4_LOGDIR}
%dir %{_datarootdir}/rt4/po
%{_datarootdir}/rt4/po/*.po
%{_datarootdir}/rt4/po/*.pot

%dir %{_sysconfdir}/rt4
%attr(-,root,root)%{_sysconfdir}/rt4/upgrade
%attr(-,root,root)%{_sysconfdir}/rt4/acl*
%attr(-,root,root)%{_sysconfdir}/rt4/schema*
%attr(-,root,root)%{_sysconfdir}/rt4/init*
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/rt4/RT_*

%config(noreplace) %{_sysconfdir}/logrotate.d/rt4

%dir %{_datadir}/rt4
%{RT4_WWWDIR}
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
* Wed Nov 27 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 4.0.17-0.2
- Enable "with_devel_mode" for RHEL compilation, for RT addon packagtes.
- Add BuildRequires for devel mode.

* Fri Aug  2 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 4.0.17-0.1
- Update to 4.0.17

* Mon May 20 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 4.0.12-0.1
- Update to 4.0.12

* Thu Mar 07 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 4.0.3-0.1
- Update to 4.0.10.
- Add BuildRequires: perl(Test::HArness).
- Rollback perl(URI) version requiorement for RHEL 6 compatibility.
- Add Provides: perl(RT::SQL) for RHEL 6 ocmpatibility.
- Add Provides: perl(RT::Tickets_SQL) for RHEL 6 ocmpatibility.
- Edit patches for RT4, not RT3.
- Move and edit rt3.conf.in to rt4.conf.in, with unnecessary Perl
  mangling discarded.
- Add conflicts with rt3 and rt3-mailgate.

* Tue Jul 10 2012 Xavier Bachelot <xavier@bachelot.org> - 3.8.13-1.2
- Fix filtering for EL6.

* Mon Jun 04 2012 Xavier Bachelot <xavier@bachelot.org> - 3.8.13-1.1
- Default to non-devel mode for non-Fedora builds.

* Sat Jun 02 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.13-1
- Upstream update.

* Tue May 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.12-1
- Upstream update.
- Address various CVEs (BZ 824082).

* Tue Feb 02 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.11-7
- Fix shebangs.
- Make testsuite files executable (enables rpm's perl module dep tracking).
- Build *-tests, iff devel_mode was given.
- Misc. specfile massaging.

* Tue Jan 31 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.11-6
- Misc. specfile improvements.

* Tue Jan 31 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.11-5
- Rewrite *-tests package (Don't use tests macros).

* Mon Jan 30 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.11-4
- Rename rpmbuild option with_tests into with_runtests.
- Add rt4-tests subpackage.
- Add README.tests.
- Remove removal of ${RT4_LIBDIR}/t (Fixed by upstream).
- Rework R:/BR:.
- Use %%{__rm} instead of /bin/rm.
- Misc minor spec file cleanup.

* Wed Jan 18 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.11-3
- Fix typo in filter rules.
- Add lexdir, manualdir, RT4_LEXDIR.

* Mon Jan 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.11-2
- Remove redundant R: config(rt4), Remove P: config(rt4).
- Rewrite filter rules.

* Sun Jan 15 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.11-1
- Upstream update.

* Tue Jan 10 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.10-5
- Fix broken dependency filtering having been added in *-4.
- Spec file cleanup.

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 3.8.10-4
- RPM 4.9 dependency filtering added

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 3.8.10-3
- Perl mass rebuild

* Tue May 03 2011 Xavier Bachelot <xavier@bachelot.org> - 3.8.10-2.1
- Add BR: perl(Digest::SHA).

* Sat Apr 16 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.10-2
- Work-around rpm's depgenerator defect: 
  Filter Requires: perl(DBIx::SearchBuilder::Handle::).

* Sat Apr 16 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.10-1
- Upstream update.
- Rebase patches.
- Spec cleanup.

* Thu Feb 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.9-1
- Upstream update (CVE-2011-0009, BZ 672257).
- Rebase patches.
- Switch to using perl-filters
  (Work around broken deps caused by rpm dep-tracker changes).
- Spec file overhaul.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 03 2010 Mark Chappell <tremble@fedoraproject.org> - 3.8.8-3.1
- Enable GPG2 for the EPEL build

* Thu Jul 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.8-3
- Add COPYING to rt4-mailgate.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.8.8-2
- Mass rebuild with perl-5.12.0

* Fri May 07 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.8-1
- Upstream update.
- Add %%{_datadir}/rt4/fonts
- Use system-wide google-droid-fonts instead of bundled 
  Droid fonts.
- Add rt-3.8.8-Makefile.diff.
- Remove rt-3.8.6-Makefile.diff.
- Add rt-3.8.8-config.diff.
- Remove rt-3.8.4-config.diff
- Misc. spec file massaging.

* Mon Mar 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.7-2
- Make building --without devel_mode working (BZ 575780).

* Mon Dec 14 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.7-1
- Upstream update.
- Add UPGRADING.mysql, perl(Text::Quoted), R: perl(Text::WikiFormat)
  (BZ #546786; Thanks to Dale Bewley <dale@fedoraproject.org>)

* Fri Dec 04 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.6-1
- Upstream update.
- Remove rt-3.8.4-Makefile.diff, rt-3.8.4-test-dependencies.diff, 
  rt-3.8.4-rh-bz543962.diff.
- Add rt-3.8.6-Makefile.diff, rt-3.8.6-test-dependencies.diff

* Fri Dec 04 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.5-2
- Add rt-3.8.4-rh-bz543962.diff (BZ #543962).

* Mon Oct 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.5-1
- Upstream update.
- Remove rt-3.8.4-rh-bz526870.diff.

* Mon Oct 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.4-5
- Bump Release:.

* Mon Oct 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.4-4
- Add rt-3.8.4-rh-bz526870.diff (BZ #526870).

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.4-2
- Add R: perl(Data::ICal), R: perl(Data::ICal::Entry::Event) (BZ #507965).

* Fri Jun 19 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.4-1
- Upstream update.
- Rebase patches against 3.8.4.
- Abandon rt-3.4.1-I18N.diff.

* Fri Apr 24 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.2-7
- README.fedora.in: Add --dba root to rt-setup-database (BZ #488621).
- R: perl(XML::RSS) (BZ #496720).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.2-5
- Add R: perl(Class::Accessor::Fast), perl(Exception::Class::Base),
  perl(HTML::Mason::Request), perl(Net::Server::PreFork).

* Thu Feb 05 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.2-4
- Stop filtering perl(Test::Email).
- Add perl(:MODULE_COMPAT ...) to perl-RT-Test.

* Sat Jan 24 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.2-3
- Fix date in changelog entry.

* Sat Jan 24 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.2-2
- Filter out R: perl(Test::Email).
- Add perl-RT-Test package.
- Activate --with devel_mode.
- Don't pass --enable/disable-devel-mode to configure.
- Add Explicit check for devel-mode deps.

* Fri Jan 23 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.2-1
- Upstream update.
- Preps to add a perl-RT-Test package.

* Sun Nov 30 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.1-2
- Fix rt4-mailgate's %%defattr(-,root,root,-).

* Wed Oct 01 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.1-1
- 1st rawhide release.

* Mon Sep 23 2008 Ralf Corsépius <corsepiu@fedoraproject.org>
- Add Provides for perl-deps rpm doesn't catch.
- Treat Spamassassin optional

* Mon Sep 23 2008 Ralf Corsépius <corsepiu@fedoraproject.org>
- Don't package %%{_sysconfdir}/rt4/upgrade/*.in
- Cleanup Requires, __perl_requires, __perl_provides.

* Tue Sep 23 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.8.1-0
- First try at public release.
- Completely rework the spec.
- Upstream update.

* Wed Jun 26 2008 Ralf Corsépius <rc040203@freenet.de> - 3.6.7-1
- Upstream update.
- Add --with-testdeps.

* Wed Mar 26 2008 Ralf Corsépius <rc040203@freenet.de> - 3.6.6-5
- Install rt4.logrotate to /etc/logrotate.d.

* Mon Mar 17 2008 Ralf Corsépius <rc040203@freenet.de> - 3.6.6-4
- Add %%{_sysconfdir}/logrotate.d/rt4 (BZ 437100)
- Let RT4_LOGDIR be owned by user apache (BZ 437100).

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.6.6-3
- Rebuild for new perl

* Mon Feb 04 2008 Ralf Corsépius <rc040203@freenet.de> - 3.6.6-2
- R: perl(CSS::Squish).

* Sun Feb 03 2008 Ralf Corsépius <rc040203@freenet.de> - 3.6.6-1
- Upstream update.

* Wed Oct 17 2007 Ralf Corsépius <rc040203@freenet.de> - 3.6.5-1
- Upstream update.
- Split-out rt-mailgate in to rt4-mailgate (BZ 332731).

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 3.6.4-1
- Upstream update.

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 3.6.3-2
- Update license tag.

* Fri Dec 29 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.3-1
- Upstream update.
- Add perl(GD::*) deps.

* Thu Sep 07 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.1-3
- Extend /etc/RT_SiteConfig.pm (jpo, BZ 202374)

* Wed Sep 06 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.1-2
- Mass rebuild.

* Sun Aug 13 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.1-1
- Upstream update.

* Sat Jul 22 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.0-4
- Install etc/upgrade to %%{_sysconfdir}/rt4/upgrade.
- Add rt-3.6.0-Makefile.diff.

* Mon Jul 19 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.0-3
- Move /var/www/rt4 to %%{_datadir}/rt4/html

* Fri Jun 23 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.0-2
- Require perl(Calendar::Simple).

* Fri Jun 23 2006 Ralf Corsépius <rc040203@freenet.de> - 3.6.0-1
- Upstream update.

* Sun Jan 15 2006 Ralf Corsépius <rc040203@freenet.de> - 3.4.5-1
- Upstream update.

* Wed Dec 07 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-11
- Require perl(HTML::FormatText), perl(HTML::TreeBuilder) (#175176).

* Fri Nov 04 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-10
- Inline rt4-filter-provides.sh, rt4-filter-requires.sh into spec.

* Sat Oct 29 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-9
- Remove "Requires(post): /usr/bin/chcon".
- Add "Requires: perl(:MODULE_COMPAT...)".

* Fri Oct 28 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-8
- Fix typo in setting up localstatedir.
- Own %%{RT4_CACHEDIR}.

* Tue Oct 24 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-7
- Apply patch from Chris Grau to README.fedora.
- Move mason_data, session_data to /var/cache/rt4.
- Install %%{RT4_LOGDIR}.
- Replace README.fedora with README.fedora.in

* Thu Oct 13 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-6
- Remove RT4_USER, RT4_GROUP.

* Thu Oct 13 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-5
- Add Requires: perl(HTML::Mason), perl(HTTP::Server::Simple::Mason).
- Add README.fedora.
- Pass libdir to configure to silence rpmlint.
- Remove %%{_localstatedir}/lib/rt4 upon last package removal.

* Fri Oct 07 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-4
- Fix urls in spec file.

* Tue Sep 27 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-3
- Spec file cosmetics.

* Mon Sep 26 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-2
- FE submission.

* Sun Sep 25 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-1.4
- Install perl modules into %%perlvendorlib.

* Fri Sep 23 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-1.3
- Shift customdir to %%{_prefix}/local/lib/rt4 and %%{_prefix}/local/etc/rt4.
- %%ghost %%{_prefix}/local/lib/rt4 and %%{_prefix}/local/etc/rt4.
- install BIN files to %%{_sbindir}.

* Fri Sep 23 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-1.2
- Use %%RT4_WWWDIR, %%_sbindir, %%_bindir in config.layout.

* Thu Sep 17 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-1.1
- Reflect feedback from Chris Grau.
- Remove SpeedyCGI support.

* Thu Sep 16 2005 Ralf Corsépius <rc040203@freenet.de> - 3.4.4-1
- FE submission candidate.
