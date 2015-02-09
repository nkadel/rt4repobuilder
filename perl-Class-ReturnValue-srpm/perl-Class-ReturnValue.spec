Name:      	perl-Class-ReturnValue
Summary:   	Class::ReturnValue Perl module
Version:   	0.55
Release:   	4%{?dist}
License:   	GPL+ or Artistic
Group: 		Development/Libraries
URL:       	http://search.cpan.org/dist/Class-ReturnValue
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: 	noarch
Source:    	http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/Class-ReturnValue-%{version}.tar.gz
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)

%description
A return-value object that lets you treat it as as a boolean, array or object.

%prep
%setup -q -n Class-ReturnValue-%{version} 

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
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Class
%{_mandir}/man3/*

%changelog
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.55-2
- rebuild for new perl

* Thu Sep 06 2007 Ralf Corsépius <rc040203@freenet.de> - 0.55-1
- Upstream update.
- Spec cleanup.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 0.54-1
- Upstream update.

* Mon Aug 22 2005 Ralf Corsepius <rc040203@freenet.de> - 0.53-1
- Upstream update.
- FE submission.
