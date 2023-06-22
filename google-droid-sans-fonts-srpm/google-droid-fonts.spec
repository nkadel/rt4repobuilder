# SPDX-License-Identifier: MIT
BuildArch: noarch

# No sane versionning upstream, use git clone timestamp
Version: 20200215
Release: 11%{?dist}.2
License: ASL 2.0 and OFL
## DroidSansDevanagari is licensed under OFL
URL:     https://android.googlesource.com/

%global source_name       google-droid-fonts

%global foundry           Google
%global fontlicenses      NOTICE
%global fontdocs          *.txt

%global common_description %{expand:
The Droid font family was designed in the fall of 2006 by Ascender’s Steve
Matteson, as a commission from Google to create a set of system fonts for its
Android platform. The goal was to provide optimal quality and comfort on a
mobile handset when rendered in application menus, web browsers and for other
screen text.

The family was later extended in collaboration with other designers such as
Pascal Zoghbi of 29ArabicLetters.}

%global fontfamily1       Droid Sans
%global fontsummary1      Droid Sans, a humanist sans-serif font family
%global fontpkgheader1   %{expand:
Obsoletes: google-droid-kufi-fonts < %{version}-%{release}
Suggests: font(notosans)
}
%global fonts1            DroidSans*ttf DroidKufi*ttf
%global fontsex1          DroidSansMono*ttf DroidSansFallback.ttf DroidSansHebrew.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

Droid Sans is a humanist sans serif font family designed for user interfaces and electronic communication.

The Arabic block was initially designed by Steve Matteson of Ascender under the
Droid Kufi name, with consulting by Pascal Zoghbi of 29ArabicLetters to
finalize the font family.}

%global fontfamily2       Droid Sans Mono
%global fontsummary2      Droid Sans Mono, a humanist mono-space sans-serif font family
%global fontpkgheader2    %{expand:
Suggests: font(notosansmono)
}
%global fonts2            DroidSansMono*ttf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

Droid Sans Mono is a humanist mono-space sans serif font family designed for
user interfaces and electronic communication.}

%global fontfamily3       Droid Serif
%global fontsummary3      Droid Serif, a contemporary serif font family
%global fontpkgheader3    %{expand:
Suggests: font(notoserif)
}
%global fonts3            DroidSerif*ttf DroidNaskh*ttf
%global fontsex3          DroidNaskhUI-Regular.ttf DroidNaskh-Regular-Shift.ttf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.

The Arabic block was designed by Pascal Zoghbi of 29ArabicLetters under the
Droid Naskh name.}

%global archivename google-droid-fonts-%{version}


Source0:  %{archivename}.tar.xz
# Brutal script used to pull sources from upstream git
# Needs at least 2 Gib of space in /var/tmp
Source1:  getdroid.sh
Source11: 65-%{fontpkgname1}.xml
Source12: 60-%{fontpkgname2}.xml
Source13: 65-%{fontpkgname3}.xml

Name:     google-droid-fonts
Summary:  A set of general-purpose font families released by Google as part of Android
# Added for RHEL 8 compilation
BuildRequires: fonts-rpm-macros

%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%setup -q -n %{archivename}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 20200215-11.1
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 15 2021 Akira TAGOH <tagoh@redhat.com> - 20200215-10.1
- Add OFL to License tag for DroidSansDevanagari font.
  Resolves: rhbz#1972027

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 20200215-10
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200215-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Parag Nemade <pnemade AT redhat DOT com>
- 20200215-8
- Fix this spec file to build for F33+

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-6
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-5
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-4
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-3
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20200215-1
✅ Convert to fonts-rpm-macros use

* Sun Nov 23 2008 Nicolas Mailhot <nim@fedoraproject.org>
- 1.0.107-1
✅ Initial packaging
