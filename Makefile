#
# Makefile - build wrapper for Rt 4 on RHEL 6
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel/rt4repo

# Base directory for yum repository
REPOBASEDIR="`/bin/pwd`"
# Base subdirectories for RPM deployment
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/6/SRPMS
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/6/x86_64
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/7/SRPMS
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/7/x86_64

# These build with normal mock "epel-*" setups
EPELPKGS+=google-droid-sans-fonts-srpm
EPELPKGS+=perl-Authen-Simple-srpm
EPELPKGS+=perl-CGI-PSGI-srpm
EPELPKGS+=perl-Cache-Simple-TimedExpiry-srpm
EPELPKGS+=perl-Calendar-Simple-srpm
EPELPKGS+=perl-Capture-Tiny-srpm
EPELPKGS+=perl-Carp-Assert-More-srpm
EPELPKGS+=perl-Class-Accessor-Chained-srpm
EPELPKGS+=perl-Class-Accessor-Lite-srpm
EPELPKGS+=perl-Class-Accessor-srpm
EPELPKGS+=perl-Class-Container-srpm
EPELPKGS+=perl-Class-ReturnValue-srpm
EPELPKGS+=perl-Crypt-Eksblowfish-srpm
EPELPKGS+=perl-Crypt-X509-srpm
EPELPKGS+=perl-DBIx-DBSchema-srpm
EPELPKGS+=perl-DBIx-DBschema-srpm
EPELPKGS+=perl-Data-UUID-srpm
EPELPKGS+=perl-Devel-StackTrace-AsHTML-srpm
EPELPKGS+=perl-Devel-StackTrace-srpm
EPELPKGS+=perl-Digest-JHash-srpm
EPELPKGS+=perl-EV-srpm
EPELPKGS+=perl-Encode-srpm
EPELPKGS+=perl-Expect-Simple-srpm
EPELPKGS+=perl-ExtUtils-Manifest-srpm
EPELPKGS+=perl-GD-Graph-srpm
EPELPKGS+=perl-GnuPG-Interface-srpm
EPELPKGS+=perl-GnuP{G-Interface-srpm
EPELPKGS+=perl-HTML-FormatText-WithLinks-srpm
EPELPKGS+=perl-HTML-Lint-srpm
EPELPKGS+=perl-IO-Socket-IP-srpm
EPELPKGS+=perl-IPC-Run-SafeHandles-srpm
EPELPKGS+=perl-List-UtilsBy-srpm
EPELPKGS+=perl-Locale-Maketext-Fuzzy-srpm
EPELPKGS+=perl-Locale-Maketext-Lexicon-srpm
EPELPKGS+=perl-Log-Any-srpm
EPELPKGS+=perl-Log-Dispatch-Perl-srpm
EPELPKGS+=perl-MIME-tools-srpm
EPELPKGS+=perl-Mail-POP3Client-srpm
EPELPKGS+=perl-MailTools-srpm
EPELPKGS+=perl-Module-Util-srpm
EPELPKGS+=perl-PadWalker-srpm
EPELPKGS+=perl-PerlIO-eol-srpm
EPELPKGS+=perl-Proc-Wait3-srpm
EPELPKGS+=perl-Regexp-Common-Net-CIDR-srpm
EPELPKGS+=perl-Role-Basic-srpm
EPELPKGS+=perl-Scope-Guard-srpm
EPELPKGS+=perl-Set-Tiny-srpm
EPELPKGS+=perl-String-RewritePrefix-srpm
EPELPKGS+=perl-Symbol-Global-Name-srpm
EPELPKGS+=perl-Test-CheckManifest-srpm
EPELPKGS+=perl-Test-HTTP-Server-Simple-srpm
EPELPKGS+=perl-Test-Log-Dispatch-srpm
EPELPKGS+=perl-Test-Simple-srpm
EPELPKGS+=perl-Text-Haml-srpm
EPELPKGS+=perl-Text-Password-Pronounceable-srpm
EPELPKGS+=perl-Text-Quoted-srpm
EPELPKGS+=perl-Text-WikiFormat-srpm
EPELPKGS+=perl-Text-Wrapper-srpm
EPELPKGS+=perl-Time-Duration-Parse-srpm
EPELPKGS+=perl-Tree-Simple-srpm
EPELPKGS+=perl-URI-srpm
EPELPKGS+=perl-boolean-srpm
EPELPKGS+=perl-capitalization-srpm

# Require customized rt4repo local repository for dependencies
# Needed by various packages

RT4PKGS+=perl-Authen-Simple-Passwd-srpm

# Dependencies for perl-Test-TCP-srpm
RT4PKGS+=perl-Test-SharedFork-srpm
RT4PKGS+=perl-Test-TCP-srpm

# Dependencies for perl-Date-Extract-srpm
RT4PKGS+=perl-DateTime-Format-Natural-srpm
RT4PKGS+=perl-Date-Extract-srpm

# Deendencies for perl-CHI
## Dependency for perl-Log-Any-Adapter-Dispatch
RT4PKGS+=perl-Hash-MoreUtils-srpm
RT4PKGS+=perl-Log-Any-Adapter-srpm
RT4PKGS+=perl-Log-Any-Adapter-Dispatch-srpm
RT4PKGS+=perl-Module-Mask-srpm
# Previously included for perl-Shared-Fonts-srpm
RT4PKGS+=perl-CHI-srpm

RT4PKGS+=perl-Convert-Color-srpm

# Dependency for perl-Data-ICal-srpm
RT4PKGS+=perl-Text-vFile-asData-srpm
RT4PKGS+=perl-Data-ICal-srpm

RT4PKGS+=perl-Data-GUID-srpm
RT4PKGS+=perl-DBIx-SearchBuilder-srpm
RT4PKGS+=perl-Devel-StackTrace-WithLexicals-srpm
RT4PKGS+=perl-Email-Address-List-srpm
RT4PKGS+=perl-HTML-FormatText-WithLinks-AndTables-srpm

# Dependency for perl-HTML-Mason-PSGIHandler-srpm
RT4PKGS+=perl-HTML-Mason-srpm
RT4PKGS+=perl-HTML-Mason-PSGIHandler-srpm

RT4PKGS+=perl-HTML-Quoted-srpm
RT4PKGS+=perl-HTML-RewriteAttributes-srpm
RT4PKGS+=perl-HTTP-Server-Simple-Mason-srpm
RT4PKGS+=perl-Locale-Maketext-Lexicon-srpm
RT4PKGS+=perl-Mojolicious-srpm

# Dependency for perl-Parallel-Prefork-srpm
RT4PKGS+=perl-Parallel-Scoreboard-srpm
RT4PKGS+=perl-Parallel-Prefork-srpm

# Depdnencies for perl-Starlet-srpm
RT4PKGS+=perl-Regexp-IPv6-srpm
RT4PKGS+=perl-Server-Starter-srpm
RT4PKGS+=perl-Starlet-srpm

RT4PKGS+=perl-Test-Email-srpm
RT4PKGS+=perl-Test-Expect-srpm

# Needed for rt-Test building
RT4PKGS+=perl-Test-WWW-Mechanize-srpm
RT4PKGS+=perl-Test-WWW-Mechanize-PSGI-srpm
RT4PKGS+=perl-Plack-Middleware-Test-StashWarnings-srpm

# Binary target
RT4PKGS+=rt4-srpm

# Add-on utilities, can be compiled with rt3 from EPEL,
# but use rt4 from local builds
RT4PKGS+=perl-RT-Extension-CommandByMail-srpm
RT4PKGS+=perl-RT-Extension-MandatoryFields-srpm



# Populate rt4repo with packages compatible with just EPEL
all:: epel-install

# Populate rt4repo with packages that require rt4repo
all:: rt4-install

install:: epel-install rt4-install

rt4repo-6-x86_64.cfg:: rt4repo-6-x86_64.cfg.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

rt4repo-6-x86_64.cfg:: FORCE
	@cmp -s $@ /etc/mock/$@ || \
		(echo Warning: /etc/mock/$@ does not match $@, exiting; exit 1)

rt4repo-7-x86_64.cfg:: rt4repo-7-x86_64.cfg.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

rt4repo-7-x86_64.cfg:: FORCE
	@cmp -s $@ /etc/mock/$@ || \
		(echo Warning: /etc/mock/$@ does not match $@, exiting; exit 1)

rt4repo.repo:: rt4repo.repo.in
	sed "s|@@@REPOBASEDIR@@@|$(REPOBASEDIR)|g" $? > $@

rt4repo.repo:: FORCE
	@cmp -s $@ /etc/yum.repos.d/$@ || \
		(echo Warning: /etc/yum.repos.d/$@ does not match $@, exiting; exit 1)

epel:: $(EPELPKGS)

$(REPOBASESUBDIRS)::
	mkdir -p $@

epel-install:: $(REPOBASESUBDIRS)

epel-install:: FORCE
	@for name in $(EPELPKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

rt4:: epel-install
rt4:: $(RT4PKGS)

rt4-install:: FORCE
	@for name in $(RT4PKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

# Dependencies

perl-Authen-Simple-Passwd-srpm:: perl-Authen-Simple-srpm
perl-CHI-srpm:: perl-Digest-JHash-srpm
perl-CHI-srpm:: perl-Hash-MoreUtils-srpm
perl-CHI-srpm:: perl-Log-Any-Adapter-Dispatch-srpm
perl-CHI-srpm:: perl-Log-Any-Adapter-srpm
perl-CHI-srpm:: perl-Module-Mask-srpm
perl-CHI-srpm:: perl-String-RewritePrefix-srpm
perl-CHI-srpm:: perl-Test-Log-Dispatch-srpm
perl-CHI-srpm:: perl-Time-Duration-Parse-srpm
perl-Convert-Color-srpm:: perl-List-UtilsBy-srpm
perl-DBIx-SearchBuilder-srpm:: perl-Cache-Simple-TimedExpiry-srpm
perl-DBIx-SearchBuilder-srpm:: perl-Class-ReturnValue-srpm
perl-DBIx-SearchBuilder-srpm:: perl-capitalizaton-srpm
perl-Data-GUID-srpm:: perl-Data-UUID-srpm
perl-Data-ICal-srpm:: perl-Class-ReturnValue-srpm
perl-Data-ICal-srpm:: perl-Text-vFile-asData-srpm
perl-Date-Extract-srpm:: perl-DateTime-Format-Natural-srpm
perl-Devel-StackTrace-WithLexicals-srpm:: perl-Devel-StackTrace-srpm
perl-Devel-StackTrace-WithLexicals-srpm:: perl-PadWalker-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-Test-Log-Dispatch-srpm
perl-Hash-MoreUtils-srpm:: perl-Test-CheckManifest-srpm
perl-Log-Any-Aapter-srpm:: perl-Log-Any-srpm
perl-Log-Any-Adapter-Dispatch-srpm:: perl-Log-Any-Adapter-srpm
perl-Module-Mask-srpm:: perl-Module-Util-srpm
perl-Mojolicious-srpm:: perl-IO-Socket-IP-srpm
perl-Parallel-Prefork-srpm:: perl-Class-Accessor-Lite-srpm
perl-Parallel-Prefork-srpm:: perl-Parallel-Scoreboard-srpm
perl-Parallel-Scoreboard-srpm:: perl-Class-Accessor-Lite-srpm
perl-Regexp-IPv6-srpm:: perl-Devel-StackTrace-srpm
perl-Server-Starter-srpm:: perl-Encode-srpm
perl-Server-Starter-srpm:: perl-Proc-Wait3-srpm
perl-Starlet-srpm:: perl-Parallel-Prefork-srpm
perl-Starlet-srpm:: perl-Server-Starter-srpm
perl-Test-Email-srpm:: perl-Mail-POP3Client-srpm
perl-Test-TCP-srpm:: perl-Test-SharedFork-srpm
perl-Test-TCP-srpm:: perl-Test-Simple-srpm
perl-Test-WWW-Mechanize-PSGI-srpm:: perl-Test-WWW-Mechanize-srpm
perl-Test-WWW-Mechanize-srpm:: perl-Carp-Assert-More-srpm
perl-Test-WWW-Mechanize-srpm:: perl-Test-WWW-Mechanize-srpm
perl-Text-vFile-asData-srpm:: perl-Class-Accessor-Chained-srpm
perl-Test-Expect-srpm:: perl-Class-Accessor-Chained-srpm
perl-Test-Expect-srpm:: perl-Expect-Simple-srpm


rt4:: google-droid-sans-fonts-srpm
rt4:: perl-CGI-PSGI-srpm
rt4:: perl-Class-Accessor-srpm
rt4:: perl-Convert-Color-srpm
rt4:: perl-Crypt-X509-srpm
rt4:: perl-Data-ICal-srpm
rt4:: perl-Date-Extract-srpm
rt4:: perl-Devel-StackTrace-srpm
rt4:: perl-EV-srpm
rt4:: perl-Email-Address-List-srpm
rt4:: perl-Encode-srpm
rt4:: perl-GD-Graph-srpm
rt4:: perl-HTML-FormatText-WithLinks-AndTables-srpm
rt4:: perl-HTML-FormatText-WithLinks-srpm
rt4:: perl-HTML-Mason-PSGIHandler-srpm
rt4:: perl-HTML-Mason-srpm
rt4:: perl-HTML-Quoted-srpm
rt4:: perl-HTML-RewriteAttributes-srpm
rt4:: perl-IPC-Run-SafeHandles-srpm
rt4:: perl-Locale-Maketext-Fuzzy-srpm
rt4:: perl-Locale-Maketext-Lexicon-srpm
rt4:: perl-Log-Dispatch-Perl-srpm
rt4:: perl-MIME-tools-srpm
rt4:: perl-MailTools-srpm
rt4:: perl-PerlIO-eol-srpm
rt4:: perl-Plack-Middleware-Test-StashWarnings-srpm
rt4:: perl-Regexp-IPv6-srpm
rt4:: perl-Role-Basic-srpm
rt4:: perl-Set-Tiny-srpm
rt4:: perl-Symbol-Global-Name-srpm
rt4:: perl-Test-Email-srpm
rt4:: perl-Test-Expect-srpm
rt4:: perl-Text-Haml-srpm
rt4:: perl-Text-Password-Pronounceable-srpm
rt4:: perl-Text-Quoted-srpm
rt4:: perl-Tree-Simple-srpm

perl-RT-Extension-CommandByMail:: rt4-srpm
perl-RT-Extension-MandatoryFields:: rt4-srpm

# Git clone operations, not normally required
# Targets may change

# Build EPEL compatible softwaer in place
$(EPELPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

#$(RT4PKGS):: rt4repo-6-x86_64.cfg
$(RT4PKGS):: rt4repo-7-x86_64.cfg

$(RT4PKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

# Needed for local compilation, only use for dev environments
build:: rt4repo.repo

build clean realclean distclean:: FORCE
	@for name in $(EPELPKGS) $(RT4PKGS); do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done

realclean distclean:: clean

clean::
	find . -name \*~ -exec rm -f {} \;

# Use this only to build completely from scratch
# Leave the rest of rt4repo alone.
maintainer-clean:: clean
	@echo Clearing local yum repository
	find rt4repo -type f ! -type l -exec rm -f {} \; -print

# Leave a safe repodata subdirectory
maintainer-clean:: FORCE

safe-clean:: maintainer-clean FORCE
	@echo Populate rt4repo with empty, safe repodata
	find rt4repo -noleaf -type d -name repodata | while read name; do \
		createrepo -q $$name/..; \
	done


# This is only for upstream repository publication.
# Modify for local use as needed, but do try to keep passwords and SSH
# keys out of the git repository fo this software.
RSYNCTARGET=rsync://localhost/rt4repo
RSYNCOPTS=-a -v --ignore-owner --ignore-group --ignore-existing
RSYNCSAFEOPTS=-a -v --ignore-owner --ignore-group
publish:: all
publish:: FORCE
	@echo Publishing RPMs to $(RSYNCTARGET)
	rsync $(RSYNCSAFEOPTS) --exclude=repodata $(RSYNCTARGET)/

publish:: FORCE
	@echo Publishing repodata to $(RSYNCTARGET)
	find repodata/ -type d -name repodata | while read name; do \
	     rsync $(RSYNCOPTS) $$name/ $(RSYNCTARGET)/$$name/; \
	done

FORCE::

