Name:           perl-Server-Starter
Version:        0.11
Release:        0.2%{?dist}
Summary:        Superdaemon for hot-deploying server programs
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Server-Starter/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Server-Starter-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Proc::Wait3)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::TCP) >= 0.11
BuildRequires:  perl(Encode) >= 2.39
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%package start_server
Summary:       	perl-Server-Starter start_server script
# FIXME: This doesn't make much sense. If at all, then this should be 
# Requires: perl(Server::Starter) = perl-version(Server::Starter)
Requires:	perl-Server-Starter = %{version}-%{release}

%description
It is often a pain to write a server program that supports graceful
restarts, with no resource leaks. Server::Starter, solves the problem by
splitting the task into two. One is start_server, a script provided as a
part of the module, which works as a superdaemon that binds to zero or
more TCP ports, and repeatedly spawns the server program that actually
handles the necessary tasks (for example, responding to incoming
connections). The spawned server programs under Server::Starter call
accept(2) and handle the requests.

%description start_server
perl-Server-Starter's start_server script.

%prep
%setup -q -n Server-Starter-%{version}

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing
#   missing modules
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files start_server
%defattr(-,root,root,-)
%{_bindir}/start_server
%{_mandir}/man1/start_server.*

%changelog
* Sun Aug  4 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 0.11-0.2
- Add BuildRequires: perl(Encode) >= 2.39, undocumented dependency


* Wed Mar 13 2013 Nico Kadel-Garcia <nkadelgarcia-consultant@scholastic.com> - 0.11-0.1
- Rollback release to avoid update confusion.
- Add BuildRequires: perl(Test::Harness) for mock compilation.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.11-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-2
- Add "Requires: perl-Server-Starter = %%{version}-%%{release}"
  per reviewer's demand.

* Thu Jan 20 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.11-1
- Upstream update.
- Reflect package review.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-2
- Put start_server into separate subpackage.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-1
- Initial Fedora package.
