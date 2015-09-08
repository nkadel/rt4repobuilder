Name: 		perl-Locale-Maketext-Lexicon
Version: 	0.82
#Release: 	1%{?dist}
Release: 	0.1%{?dist}
Summary: 	Extract translatable strings from source
License:	MIT
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Locale-Maketext-Lexicon/

Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:	perl(ExtUtils::MakeMaker)
# Required by the tests
BuildRequires:  /usr/bin/msgunfmt
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(YAML)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildArch: noarch

# rpm doesn't catch this
Requires:       perl(YAML::Loader)

%description
Locale::Maketext::Lexicon provides lexicon-handling backends for
Locale::Maketext to read from other localization formats, such as PO files,
MO files, or from databases via the "Tie" interface.

%prep
%setup -q -n Locale-Maketext-Lexicon-%{version}

cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
    sed -e '/perl(My/d'

EOF
%define __perl_provides %{_builddir}/Locale-Maketext-Lexicon-%{version}/%{name}-prov
chmod +x %{__perl_provides}

# HACK: Remove bogus requires, rpm adds due to misinterpreting docs/*.hmtl
cat << \EOF > %{name}-requ
#!/bin/sh
%{__perl_requires} $* |\
    sed -e '/perl(Locale::Msgcat)/d' \
	-e '/perl(POSIX)/d' \
	-e '/perl(CGI)/d' \
	-e '/perl(Lingua::EN::Numbers::Ordinate)/d' \
	-e '/perl(Locale::gettext)/d' \
	-e '/perl(base)/d' \
	-e '/perl(Locale::Maketext::Lexicon)/d'

EOF
%define __perl_requires %{_builddir}/Locale-Maketext-Lexicon-%{version}/%{name}-requ
chmod +x %{__perl_requires}

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
%doc AUTHORS Changes README
%doc docs
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/Locale
%{_mandir}/man3/*

%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 0.82-0.1
- Roll back reloase for port to RHEL 7.
- Add BuildRequires for perl(Locale::Maketext).

* Thu May 06 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.82-1
- Upstream update.

* Wed Mar 03 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.79-1
- Upstream update.

* Tue Mar 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.78-1
- Upstream update.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 02 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.77-1
- Upstream update.

* Sat Dec 20 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.76-1
- Upstream update.

* Sat Nov 29 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.75-1
- Upstream update.
- Reflect upstream maintainer having changed.
- BR: perl(Template), BR: perl(Test::Pod).

* Fri Oct 10 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.71-1
- Upstream update.
- Spec cleanup.
- Add spec hacks to work around rpm bugs.

* Thu Aug 28 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.68-2
- Filter out bogus requires.

* Tue Aug 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.68-1
- Upstream update.
- Reflect new Source0-URL.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.66-2
- Rebuild for perl 5.10 (again)

* Thu Feb 14 2008 Ralf Corsépius <rc040203@freenet.de> - 0.66-1
- Upstream update.

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.65-2
- rebuild for new perl

* Fri Dec 28 2007 Ralf Corsépius <rc040203@freenet.de> - 0.65-1
- Upstream update.

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 0.64-2
- Update license tag.
- BR: perl(ExtUtils::MakeMaker).

* Mon Jun 11 2007 Ralf Corsépius <rc040203@freenet.de> - 0.64-1
- Upgrade to 0.64.
- Reflect source-url having changed.

* Fri Feb 16 2007 Ralf Corsépius <rc040203@freenet.de> - 0.62-1
- Upgrade to 0.62.
- Reflect licence change from Artistic/GPL to MIT.
- BR: /usr/bin/msgunfmt.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.60-2
- Mass rebuild.

* Sat Apr 22 2006 Ralf Corsépius <rc040203@freenet.de> - 0.60-1
- Upstream update.

* Sun Mar 19 2006 Ralf Corsépius <rc040203@freenet.de> - 0.54-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 0.53-2
- Rebuild for perl-5.8.8.

* Mon Dec 05 2005 Ralf Corsepius <rc040203@freenet.de> - 0.53-1
- Upstream update.
