#
# Makefile - build wrapper for Rt 4 on RHEL 6
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel/[package] into designated
#	RT4PKGS below
#
#	Set up local 

# Base directory for yum repository
REPOBASEDIR="`/bin/pwd`"
# Base subdirectories for RPM deployment
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/6/SRPMS
REPOBASESUBDIRS+=$(REPOBASEDIR)/rt4repo/6/x86_64

# These build with normal mock "epel-*" setups
EPELPKGS+=perl-Authen-Simple-srpm
EPELPKGS+=perl-CGI-PSGI-srpm
EPELPKGS+=perl-Crypt-Eksblowfish-srpm
EPELPKGS+=perl-Capture-Tiny-srpm
EPELPKGS+=perl-Class-Accessor-Lite-srpm
EPELPKGS+=perl-Class-Accessor-srpm
EPELPKGS+=perl-DBIx-SearchBuilder-srpm
EPELPKGS+=perl-Devel-StackTrace-AsHTML-srpm
EPELPKGS+=perl-Devel-StackTrace-srpm
EPELPKGS+=perl-Digest-JHash-srpm
EPELPKGS+=perl-Encode-srpm
EPELPKGS+=perl-ExtUtils-Installed-srpm
EPELPKGS+=perl-ExtUtils-MakeMaker-srpm
EPELPKGS+=perl-Hash-MoreUtils-srpm
EPELPKGS+=perl-List-UtilsBy-srpm
EPELPKGS+=perl-Log-Any-srpm
EPELPKGS+=perl-Module-Util-srpm
EPELPKGS+=perl-PadWalker-srpm
EPELPKGS+=perl-Proc-Wait3-srpm
EPELPKGS+=perl-Regexp-Common-Net-CIDR-srpm
EPELPKGS+=perl-Scope-Guard-srpm
EPELPKGS+=perl-Test-Log-Dispatch-srpm
EPELPKGS+=perl-Test-WWW-Mechanize
EPELPKGS+=perl-Text-Password-Pronounceable-srpm
EPELPKGS+=perl-Time-Duration-Parse-srpm
EPELPKGS+=perl-URI-srpm

# Add-on utilities, currently compile only with rt3 from EPEL
EPELPKGS+=perl-RT-Extension-CommandByMail-srpm
EPELPKGS+=perl-RT-Extension-MandatoryFields-srpm

# Require customized rt4repo local repository for dependencies
# Needed by various packages

RT4PKGS+=perl-Authen-Simple-Passwd-srpm

# Deendencies for perl-CHI
## Dependency for perl-Log-Any-Adapter-Dispatch
RT4PKGS+=perl-Log-Any-Adapter-srpm
RT4PKGS+=perl-Log-Any-Adapter-Dispatch-srpm
RT4PKGS+=perl-Module-Mask-srpm
RT4PKGS+=perl-CHI-srpm

RT4PKGS+=perl-Convert-Color-srpm
RT4PKGS+=perl-Devel-StackTrace-WithLexicals-srpm

# Dependency for perl-HTML-Mason-PSGIHandler-srpm
RT4PKGS+=perl-Plack-srpm
RT4PKGS+=perl-HTML-Mason-PSGIHandler-srpm

RT4PKGS+=perl-HTML-Mason-srpm
RT4PKGS+=perl-HTML-Quoted-srpm
RT4PKGS+=perl-HTML-RewriteAttributes-srpm

# Dependency for perl-Parallel-Prefork-srpm
RT4PKGS+=perl-Parallel-Scoreboard-srpm
RT4PKGS+=perl-Parallel-Prefork-srpm

RT4PKGS+=perl-Regexp-IPv6-srpm
RT4PKGS+=perl-Server-Starter-srpm
RT4PKGS+=perl-Starlet-srpm

# Needed for rt4-Test building
RT4PKGS+=perl-Test-WWW-Mechanize-PSGI
RT4PKGS+=perl-Plack-Middleware-Test-StashWarnings-srpm

# Binary target
RT4PKGS+=rt4-srpm

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
perl-CHI-srpm:: perl-Test-Log-Dispatch-srpm
perl-CHI-srpm:: perl-Time-Duration-Parse-srpm
perl-Convert-Color:: perl-List-UtilsBy-srpm
perl-Devel-StackTrace-WithLexicals-srpm:: perl-Devel-StackTrace-srpm
perl-Devel-StackTrace-WithLexicals-srpm:: perl-PadWalker-srpm
perl-ExtUtils-MakeMaker-srpm:: perl-ExtUtils-Installed-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-Plack-srpm
perl-HTML-Mason-PSGIHandler-srpm:: perl-Test-Log-Dispatch-srpm
perl-Log-Any-Aapter-srpm:: perl-Log-Any-srpm
perl-Log-Any-Adapter-Dispatch-srpm:: perl-Log-Any-Adapter-srpm
perl-Module-Mask-srpm:: perl-Module-Util-srpm
perl-Parallel-Prefork-srpm:: perl-Class-Accessor-Lite-srpm
perl-Parallel-Prefork-srpm:: perl-Parallel-Scoreboard-srpm
perl-Parallel-Scoreboard-srpm:: perl-Class-Accessor-Lite-srpm
perl-Plack-srpm:: perl-Authen-Simple-Passwd-srpm
perl-Plack-srpm:: perl-Devel-StackTrace-WithLexicals-srpm
perl-Plack-srpm:: perl-URI-srpm
perl-Regexp-IPv6-srpm:: perl-Devel-StackTrace-srpm
perl-Server-Starter-srpm:: perl-Encode-srpm
perl-Server-Starter-srpm:: perl-Proc-Wait3-srpm
perl-Starlet-srpm:: perl-Parallel-Prefork-srpm
perl-Starlet-srpm:: perl-Server-Starter-srpm

rt4:: perl-CGI-PSGI-srpm
rt4:: perl-Class-Accessor-srpm
rt4:: perl-Convert-Color-srpm
rt4:: perl-Devel-StackTrace-srpm
rt4:: perl-Encode-srpm
rt4:: perl-HTML-Mason-PSGIHandler-srpm
rt4:: perl-HTML-Mason-srpm
rt4:: perl-HTML-Quoted-srpm
rt4:: perl-HTML-RewriteAttributes-srpm
rt4:: perl-Plack-Middleware-Test-StashWarnings-srpm
rt4:: perl-Plack-srpm
rt4:: perl-Regexp-IPv6-srpm
rt4:: perl-Text-Password-Pronounceable-srpm

perl-RT-Extension-CommandByMail:: rt4-srpm
perl-RT-Extension-MandatoryFields:: rt4-srpm

# Git clone operations, not normally required
# Targets may change

# Rt rellies on all the other components
# krb5-1.10 is now part of RHEL 6.4, no longer needed
#rt4-srpm:: krb5-srpm

# Build EPEL compatible softwaer in place
$(EPELPKGS):: FORCE
	(cd $@ && $(MAKE) $(MLAGS)) || exit 1

$(RT4PKGS):: rt4repo-6-x86_64.cfg

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

