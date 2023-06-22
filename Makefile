
# Makefile - build wrapper for Rt 4 on RHEL 6
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel/rt4repo

REPOBASE=file://$(PWD)

# Base subdirectories for RPM deployment
REPOS+=rt4repo/el/8
REPOS+=rt4repo/el/9
REPOS+=rt4repo/fedora/38

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

MOCKCFGS+=rt4repo-8-x86_64.cfg
MOCKCFGS+=rt4repo-9-x86_64.cfg
MOCKCFGS+=rt4repo-f38-x86_64.cfg

CFGS+=centos-stream+epel-8-x86_64.cfg
CFGS+=centos-stream+epel-9-x86_64.cfg
CFGS+=fedora-38-x86_64.cfg

REPOBASEDIR:=`/bin/pwd`/../rt4repo

# These build with normal mock "epel-*" setups
#EPELPKGS+=google-droid-sans-fonts-srpm
#EPELPKGS+=perl-Authen-Simple-srpm
EPELPKGS+=perl-CGI-PSGI-srpm
#EPELPKGS+=perl-Cache-Simple-TimedExpiry-srpm
#EPELPKGS+=perl-Calendar-Simple-srpm
EPELPKGS+=perl-Capture-Tiny-srpm
EPELPKGS+=perl-Carp-Assert-srpm
EPELPKGS+=perl-Class-Accessor-Chained-srpm
#EPELPKGS+=perl-Class-Accessor-Lite-srpm
#EPELPKGS+=perl-Class-Accessor-srpm
EPELPKGS+=perl-Class-Container-srpm
#EPELPKGS+=perl-Class-ReturnValue-srpm
EPELPKGS+=perl-CSS-Minifier-srpm
#EPELPKGS+=perl-Crypt-Eksblowfish-srpm
#EPELPKGS+=perl-DBIx-DBschema-srpm
#EPELPKGS+=perl-Devel-StackTrace-AsHTML-srpm
#EPELPKGS+=perl-Devel-StackTrace-srpm
EPELPKGS+=perl-Digest-JHash-srpm
#EPELPKGS+=perl-Encode-srpm
EPELPKGS+=perl-Expect-Simple-srpm
#EPELPKGS+=perl-ExtUtils-Installed-srpm
#EPELPKGS+=perl-GnuP{G-Interface-srpm
EPELPKGS+=perl-Guard-srpm
EPELPKGS+=perl-Hash-MoreUtils-srpm
EPELPKGS+=perl-HTTP-Entity-Parser-srpm
EPELPKGS+=perl-HTTP-Headers-ActionPack-srpm
EPELPKGS+=perl-HTTP-Server-Simple-srpm
EPELPKGS+=perl-Lingua-EN-Sentence-srpm
#EPELPKGS+=perl-List-UtilsBy-srpm
EPELPKGS+=perl-Locale-Maketext-Fuzzy-srpm
EPELPKGS+=perl-Log-Any-srpm
EPELPKGS+=perl-Log-Dispatch-Perl-srpm
EPELPKGS+=perl-Mail-POP3Client-srpm
#EPELPKGS+=perl-Module-Util-srpm
EPELPKGS+=perl-Moox-Types-MooseLike-Numeric-srpm
#EPELPKGS+=perl-PadWalker-srpm
EPELPKGS+=perl-PerlIP-eol-srpm
EPELPKGS+=perl-Proc-Wait3-srpm
EPELPKGS+=perl-Regexp-Common-net-CIDR-srpm
EPELPKGS+=perl-Regexp-IPv6-srpm
EPELPKGS+=perl-Role-Basic-srpm
#EPELPKGS+=perl-Scope-Guard-srpm
EPELPKGS+=perl-Set-Tiny-srpm
EPELPKGS+=perl-Set-IntSpan-srpm
EPELPKGS+=perl-String-RewritePrefix-srpm
EPELPKGS+=perl-Symbol-Global-Name-srpm
#EPELPKGS+=perl-Test-CheckManifest-srpm
EPELPKGS+=perl-Test-DiagINC-srpm
EPELPKGS+=perl-Test-Log-Dispatch-srpm
#EPELPKGS+=perl-Test-Simple-srpm
EPELPKGS+=perl-Text-Haml-srpm
EPELPKGS+=perl-Text-Password-Pronounceable-srpm
EPELPKGS+=perl-Text-Quoted-srpm
EPELPKGS+=perl-Text-WikiFormat-srpm
EPELPKGS+=perl-Text-WordDiff-srpm
EPELPKGS+=perl-Text-Wrapper-srpm
EPELPKGS+=perl-Text-WikiFormat-srpm
EPELPKGS+=perl-Time-Duration-Parse-srpm
EPELPKGS+=perl-Tree-Simple-srpm
#EPELPKGS+=perl-URI-srpm
EPELPKGS+=perl-XML-RSS-srpm
#EPELPKGS+=perl-capitalization-srpm

## Require customized rt4repo local repository for dependencies
## Needed by various packages
#
RT4PKGS+=perl-Locale-Maketext-Lexicon-srpm

#RT4PKGS+=perl-Authen-Simple-Passwd-srpm
RT4PKGS+=perl-Business-Hours-srpm

# Requires HTTP::Headers::ActionPack
RT4PKGS+=perl-Web-Machine-srpm

# Requires HTTP::Server::Simple
RT4PKGS+=perl-Test-HTTP-Server-Simple-srpm

## Now requires perl-Cache-Simple-TimedExpiry-srpm
#RT4PKGS+=perl-DBIx-SearchBuilder-srpm
#
## Dependencies for perl-Test-ShardFork-srpm and perl-CHI
#RT4PKGS+=perl-ExtUtils-MakeMaker-srpm
#
## Dependencies for perl-Test-TCP-srpm
#RT4PKGS+=perl-Test-SharedFork-srpm
#RT4PKGS+=perl-Test-TCP-srpm
#
# Dependencies for perl-CHI
# Dependency for perl-Log-Any-Adapter-Dispatch
# Reuqires perl-Log-Any-srpm
RT4PKGS+=perl-Log-Any-Adapter-srpm
#RT4PKGS+=perl-Log-Any-Adapter-Dispatch-srpm
RT4PKGS+=perl-Module-Mask-srpm
RT4PKGS+=perl-CHI-srpm
#
#RT4PKGS+=perl-Convert-Color-srpm
#
## Dependency for perl-Data-ICal-srpm
#RT4PKGS+=perl-Text-vFile-asData-srpm
#RT4PKGS+=perl-Data-ICal-srpm
#
#RT4PKGS+=perl-Devel-StackTrace-WithLexicals-srpm
#
## Dependency for perl-HTML-Mason-PSGIHandler-srpm
#RT4PKGS+=perl-Plack-srpm
RT4PKGS+=perl-HTML-Mason-srpm
#RT4PKGS+=perl-HTML-Mason-PSGIHandler-srpm
#
RT4PKGS+=perl-HTML-Quoted-srpm
#RT4PKGS+=perl-HTML-RewriteAttributes-srpm
#
# Requires perl-HTTP-Server-Simple-srpm
RT4PKGS+=perl-HTTP-Server-Simple-Mason-srpm
#
# Dependency for perl-Parallel-Prefork-srpm
RT4PKGS+=perl-Parallel-Scoreboard-srpm
RT4PKGS+=perl-Parallel-Prefork-srpm
#
RT4PKGS+=perl-Server-Starter-srpm
RT4PKGS+=perl-Starlet-srpm
#
RT4PKGS+=perl-Test-Expert-srpm
#
# Dependencies for perl-Test-Email-srpm
RT4PKGS+=perl-Test-Email-srpm
#
# Requires perl-Carp-Assert
RT4PKGS+=perl-Carp-Assert-More-srpm

#RT4PKGS+=perl-Test-HTTP-Server-Simple-StashWarnings-srpm
#
RT4PKGS+=perl-Test-WWW-Mechanize-srpm
#
# Requiresperl-CSS-MinifieS-srpm
RT4PKGS+=perl-CSS-Minifier-XS-srpm

## Needed for rt4-Test building
RT4PKGS+=perl-Test-WWW-Mechanize-PSGI-srpm
RT4PKGS+=perl-Plack-Middleware-Test-StashWarnings-srpm
#
## Add-on utilities, can be compiled with rt3 from EPEL,
## but use rt4 from local builds
#RT4PKGS+=perl-RT-Extension-CommandByMail-srpm
#RT4PKGS+=perl-RT-Extension-MandatoryFields-srpm

RT4PKGS+=perl-Business-Hours-srpm

# Final product
RT4PKGS+=rt-srpm

# Populate rt4repo with packages compatible with just EPEL
all:: epel-install

# Populate rt4repo with packages that require rt4repo
all:: rt4-install

install:: $(CFGS)
install:: $(MOCKCFGS)
install:: $(REPODIRS)
install:: $(RT4PKGS)

repodirs: $(REPOS) $(REPODIRS)
repos: $(REPOS) $(REPODIRS)
$(REPOS):
	install -d -m 755 $@

.PHONY: $(REPODIRS)
$(REPODIRS): $(REPOS)
	@install -d -m 755 `dirname $@`
	/usr/bin/createrepo_c -q `dirname $@`

.PHONY: cf
cfg:: cfgs

.PHONY: cfg
cfgs:: $(MOCKCFGS)
cfgs:: $(CFGS)

$(CFGS)::
	@echo Generating $@ from $?
	@echo "include('/etc/mock/$@')" | tee $@

rt4repo-8-x86_64.cfg: /etc/mock/centos-stream+epel-8-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['root'] = 'rt4repo-{{ releasever }}-{{ target_arch }}'" | tee -a $@
	@echo "# Disable best" | tee -a $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[rt4repo]' | tee -a $@
	@echo 'name=rt4repo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/rt4repo/el/8/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '' | tee -a $@
	@echo '[packages-microsoft-com-prod]' | tee -a $@
	@echo 'name=packages-microsoft-com-prod' | tee -a $@
	@echo 'baseurl=https://packages.microsoft.com/rhel/8/prod/' | tee -a $@
	@echo 'enabled=0' | tee -a $@
	@echo 'gpgcheck=1' | tee -a $@
	@echo 'gpgkey=https://packages.microsoft.com/keys/microsoft.asc' | tee -a $@
	@echo '"""' | tee -a $@

rt4repo-9-x86_64.cfg: /etc/mock/centos-stream+epel-9-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['root'] = 'rt4repo-{{ releasever }}-{{ target_arch }}'" | tee -a $@
	@echo "# Disable best" | tee -a $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[rt4repo]' | tee -a $@
	@echo 'name=rt4repo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/rt4repo/el/9/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '' | tee -a $@
	@echo '[packages-microsoft-com-prod]' | tee -a $@
	@echo 'name=packages-microsoft-com-prod' | tee -a $@
	@echo 'baseurl=https://packages.microsoft.com/rhel/9/prod/' | tee -a $@
	@echo 'enabled=0' | tee -a $@
	@echo 'gpgcheck=1' | tee -a $@
	@echo 'gpgkey=https://packages.microsoft.com/keys/microsoft.asc' | tee -a $@
	@echo '"""' | tee -a $@

rt4repo-f38-x86_64.cfg: /etc/mock/fedora-38-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['root'] = 'rt4repo-f{{ releasever }}-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[rt4repo]' | tee -a $@
	@echo 'name=rt4repo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/rt4repo/fedora/38/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '"""' | tee -a $@

rt4repo-rawhide-x86_64.cfg: /etc/mock/fedora-rawhide-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['root'] = 'rt4repo-rawhide-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[rt4repo]' | tee -a $@
	@echo 'name=rt4repo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/rt4repo/fedora/rawhide/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '"""' | tee -a $@

# Used for make build with local components
rt4repo.repo:: rt4repo.repo.in
	sed "s|@@@REPOBASE@@@|$(REPOBASE)|g" $? > $@

.PHONY: rt4repo.rep
rt4repo.repo::
	@cmp -s $@ /etc/yum.repos.d/$@ || \
		(echo Warning: /etc/yum.repos.d/$@ does not match $@, exiting; exit 1)

epel:: $(EPELPKGS)

$(REPOBASESUBDIRS)::
	mkdir -p $@

epel-install:: $(REPOBASESUBDIRS)

.PHONY: epel-install
epel-install::
	@for name in $(EPELPKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

rt4:: $(RT4PKGS)

.PHONY: rt4-install
rt4-install::
	@for name in $(RT4PKGS); do \
		(cd $$name && $(MAKE) all install) || exit 1; \
	done

# Git clone operations, not normally required
# Targets may change

# Build EPEL compatible softwaer in place
.PHONY: $(EPELPKGS)
$(EPELPKGS)::
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

.PHONY: $(RT4PKGS)
$(RT4PKGS)::
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

# Needed for local compilation, only use for dev environments
build:: rt4repo.repo

.PHONY: build clean realclean distclean
build clean realclean distclean::
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
.PHONY: maintainer-clean
maintainer-clean::

.PHONY: safe-clean
safe-clean:: maintainer-clean
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
.PHONY: publish
publish:: all
	@echo Publishing RPMs to $(RSYNCTARGET)
	rsync $(RSYNCSAFEOPTS) --exclude=repodata $(RSYNCTARGET)/

publish::
	@echo Publishing repodata to $(RSYNCTARGET)
	find repodata/ -type d -name repodata | while read name; do \
	     rsync $(RSYNCOPTS) $$name/ $(RSYNCTARGET)/$$name/; \
	done

