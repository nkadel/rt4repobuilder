Name:           perl-HTML-Mason
Version:        1.48
Release:        0.2%{?dist}
Epoch:          1
Summary:        Powerful Perl-based web site development and delivery engine
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://www.masonhq.com/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/HTML-Mason-%{version}.tar.gz
Source1:        perl-HTML-Mason.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(CGI)
BuildRequires:  perl(Cache::Cache) >= 1
BuildRequires:  perl(Class::Container) >= 0.07
BuildRequires:  perl(Exception::Class) >= 1.15
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate) >= 0.7
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Pod) >= 1.20
BuildRequires:  perl(mod_perl2)
Requires:       perl(Cache::Cache) >= 1
Requires:       perl(Class::Container) >= 0.07
Requires:       perl(Exception::Class) >= 1.15
Requires:       perl(HTML::Entities)
Requires:       perl(Params::Validate) >= 0.7
Requires:       perl(mod_perl2)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       %{_sysconfdir}/httpd/conf.d

# Filter perl(MasonX::Request::PlusApacheSession).
Source98:       HTML-Mason-filter-requires.sh
%global real_perl_requires %{__perl_requires}
%define __perl_requires %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)-filter-requires

# Filter perl(MyApp::Mason) and perl(MyApp::MasonPlusSession).
Source99:       HTML-Mason-filter-provides.sh
%global real_perl_provides %{__perl_provides}
%define __perl_provides %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)-filter-provides

%description
Mason is a powerful Perl-based web site development and delivery
engine. With Mason you can embed Perl code in your HTML and construct
pages from shared, reusable components.  Mason solves the common
problems of site development: caching, debugging, templating,
maintaining development and production sites, and more.

%prep
%setup -q -n HTML-Mason-%{version}

sed -e 's,@@PERL_REQ@@,%{real_perl_requires},' %{SOURCE98} > %{__perl_requires}
chmod +x %{__perl_requires}

sed -e 's,@@PERL_PROV@@,%{real_perl_provides},' %{SOURCE99} > %{__perl_provides}
chmod +x %{__perl_provides}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

rm -f $RPM_BUILD_ROOT%{_bindir}/*.README
for file in $RPM_BUILD_ROOT%{_bindir}/convert*.pl ; do
    mv -f $file $( echo $file | sed 's,/\(convert.*\)\.pl$,/mason_\1,' )
done
mv -f $RPM_BUILD_ROOT%{_bindir}/mason.pl $RPM_BUILD_ROOT%{_bindir}/mason

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/www/mason
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/mason

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT %{__perl_requires} %{__perl_provides}

%files
%defattr(-,root,root,-)
%doc Changes CREDITS LICENSE README UPGRADE
%doc htdocs/ eg/ samples/
%{_bindir}/mason*
%{perl_vendorlib}/*
%{_mandir}/man3/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/perl-HTML-Mason.conf
%dir %attr(775,root,apache) %{_localstatedir}/cache/mason
%dir %{_localstatedir}/www/mason

%changelog
* Tue Mar 12 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> 1:1.48-0.2
- Add BuildRequires: perl(Test::Harness).

* Thu Oct 04 2012 Nico Kadel-Garcia <nico.kadel@tufts.edu> - 1:1.48-0.1
- Update to 1.48

* Tue Oct 02 2012 Nico Kadel-Garcia <nico.kadel@tufts.edu> - 1:1.47-0.3
- Update to 1.47 from EPEL .spec file, instead of cpan2rpm.
- Add BuildRequires: perl(Log::Any), perl(Test::Deep)
- Add BuildRequires: perl(CGI) for RHEL 6

* Wed Jan 30 2008 Steven Pritchard <steve@kspei.com> 1:1.39-1
- Update to 1.39.

* Mon Jan 07 2008 Steven Pritchard <steve@kspei.com> 1:1.38-1
- Update to 1.38.
- Update License tag.

* Mon Sep 17 2007 Steven Pritchard <steve@kspei.com> 1:1.37-1
- Update to 1.37.

* Tue Jun 26 2007 Steven Pritchard <steve@kspei.com> 1:1.36-1
- Update to 1.36.
- BR Test::Pod.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 1:1.35-2
- Rebuild.

* Tue Oct 17 2006 Steven Pritchard <steve@kspei.com> 1:1.35-1
- Update to 1.35.
- BR Test::Memory::Cycle for better test coverage.

* Mon Oct 16 2006 Steven Pritchard <steve@kspei.com> 1:1.34-1
- Update to 1.34.
- Use fixperms macro instead of our own chmod incantation.
- Reformat a bit to more closely resemble current cpanspec output.
- Rename filter-*.sh to HTML-Mason-filter-*.sh.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1:1.33-3
- Fix find option order.

* Thu Jun 08 2006 Steven Pritchard <steve@kspei.com> 1:1.33-2
- Add explicit dependency on HTML::Entities

* Mon May 29 2006 Steven Pritchard <steve@kspei.com> 1:1.33-1
- Update to 1.33
- Switch to Module::Build-based build
- Add various bindir mason scripts

* Thu Jan 19 2006 Steven Pritchard <steve@kspei.com> 1:1.32-2
- Epoch bump to resolve rpm thinking 1.3101 > 1.32

* Tue Jan 10 2006 Steven Pritchard <steve@kspei.com> 1.32-1
- Update to 1.32

* Thu Sep 15 2005 Steven Pritchard <steve@kspei.com> 1.3101-3
- Filter bogus provides/requires introduced by eg/ and samples/

* Thu Sep 15 2005 Steven Pritchard <steve@kspei.com> 1.3101-2
- More spec cleanup (jpo)

* Mon Aug 29 2005 Steven Pritchard <steve@kspei.com> 1.3101-1
- Update to 1.3101
- Spec cleanup (jpo)
- Include sample config file from Chris Grau

* Wed Aug 24 2005 Steven Pritchard <steve@kspei.com> 1.31-3
- Use /var/www/mason instead of /var/www/comp
- Spec cleanup

* Tue Aug 23 2005 Steven Pritchard <steve@kspei.com> 1.31-2
- Add some missing dependencies

* Tue Aug 23 2005 Steven Pritchard <steve@kspei.com> 1.31-1
- Update to 1.31
- Use /var/cache/mason instead of /var/www/mason
- Fix perl-HTML-Mason.conf
- Fix URL

* Thu Aug 11 2005 Steven Pritchard <steve@kspei.com> 1.30-1
- Specfile autogenerated.
- Add perl-HTML-Mason.conf and /var/www/*
