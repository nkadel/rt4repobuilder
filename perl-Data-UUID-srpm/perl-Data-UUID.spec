Name:		perl-Data-UUID
Version:	1.219
#Release:	3%{?dist}
Release:	0.2%{?dist}
Summary:	Globally/Universally Unique Identifiers (GUIDs/UUIDs) 
Group:		Development/Libraries
# Upstream says BSD but LICENSE file looks more like MIT
# https://lists.fedoraproject.org/pipermail/legal/2013-August/002226.html
License:	BSD and MIT
URL:		http://search.cpan.org/dist/Data-UUID/
Source0:	http://www.cpan.org/modules/by-module/Datga/Data-UUID-%{version}.tar.gz

BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod) >= 1.14
BuildRequires:	perl(Test::Pod::Coverage) >= 1.06
BuildRequires:	perl(threads)
BuildRequires:	perl(warnings)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Avoid provides for private shared objects
%{?perl_default_filter}

%description
This module provides a framework for generating v3 UUIDs (Universally Unique
Identifiers, also known as GUIDs (Globally Unique Identifiers). A UUID is 128
bits long, and is guaranteed to be different from all other UUIDs/GUIDs
generated until 3400 CE.

UUIDs were originally used in the Network Computing System (NCS) and later in
the Open Software Foundation's (OSF) Distributed Computing Environment.
Currently many different technologies rely on UUIDs to provide unique identity
for various software components. Microsoft COM/DCOM for instance, uses GUIDs
very extensively to uniquely identify classes, applications and components
across network-connected systems.

The algorithm for UUID generation, used by this extension, is described in the
Internet Draft "UUIDs and GUIDs" by Paul J. Leach and Rich Salz (see RFC 4122).
It provides a reasonably efficient and reliable framework for generating UUIDs
and supports fairly high allocation rates - 10 million per second per machine -
and therefore is suitable for identifying both extremely short-lived and very
persistent objects on a given system as well as across the network.

This module provides several methods to create a UUID. In all methods,
<namespace> is a UUID and <name> is a free form string.

%prep
%setup -q -n Data-UUID-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test AUTHOR_TESTING=1
perl smp-test/collision.t

%files
%doc Changes LICENSE README
%{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/Data/
%{_mandir}/man3/Data::UUID.3pm*

%changelog
* Sun Feb  8 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 1.219-0.1
- Change Source to URL usable for wget

* Fri Aug 23 2013 Paul Howarth <paul@city-fan.org> - 1.219-3
- Change license to "BSD and MIT"
  https://lists.fedoraproject.org/pipermail/legal/2013-August/002226.html
- Drop EL-5 compatibility (#998143)

* Sat Aug 17 2013 Paul Howarth <paul@city-fan.org> - 1.219-2
- Sanitize for Fedora submission

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 1.219-1
- Initial RPM version
