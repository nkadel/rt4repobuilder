Name:           perl-Convert-Color
Version:        0.08
Release:        0.1%{?dist}
Summary:        Color space conversions and named lookups
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Convert-Color/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/Convert-Color-%{version}.tar.gz
Patch0:         Convert-Color-0.07.diff
BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# For improved testing
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  /usr/share/X11/rgb.txt

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Provides: perl(Convert::Color) = %{version}

%description
This module provides conversions between commonly used ways to express
colors. It provides conversions between color spaces such as RGB and HSV,
and it provides ways to look up colors by a name.

%prep
%setup -q -n Convert-Color-%{version}
%patch0 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 0.80-0.2
- Roll back release number to avoid updgrade conflicts.
- Add BuildRequires: perl(Test::Harness).

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.08-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.08-2
- Perl mass rebuild

* Thu Apr 28 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.08-1
- Upstream update.
- Spec cleanup.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.07-2
- Add Convert-Color-0.07.diff (Remove comment, confusing rpm's dep tracking).

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.07-1
- Initial Fedora package.
