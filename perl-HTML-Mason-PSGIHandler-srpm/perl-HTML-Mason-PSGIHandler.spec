Name:           perl-HTML-Mason-PSGIHandler
Version:        0.52
Release:        0.1%{?dist}
Summary:        PSGI handler for HTML::Mason
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-Mason-PSGIHandler/
Source0:        http://www.cpan.org/authors/id/A/AB/ABH/HTML-Mason-PSGIHandler-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(CGI::PSGI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Mason)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HTML::Mason::PSGIHandler is a PSGI handler for HTML::Mason. It's based on
HTML::Mason::CGIHandler and allows you to process Mason templates on any
web servers that support PSGI.

%prep
%setup -q -n HTML-Mason-PSGIHandler-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com>
- 0.562-0.1
- Rollback release number to avoid update confusion.
- Add 'BuildRequires: perl(Test::Harness)' for mock compilation.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Petr Pisar <ppisar@redhat.com> - 0.52-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.52-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.52-1
- Initial Fedora package.
