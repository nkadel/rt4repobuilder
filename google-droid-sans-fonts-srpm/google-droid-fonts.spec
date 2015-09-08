%global fontname google-droid

%global download_root http://android.git.kernel.org/?p=platform/frameworks/base.git;a=blob_plain;f=data/fonts/

%global common_desc \
The Droid typeface family was designed in the fall of 2006 by Ascender's \
Steve Matteson, as a commission from Google to create a set of system fonts \
for its Android platform. The goal was to provide optimal quality and comfort \
on a mobile handset when rendered in application menus, web browsers and for \
other screen text.

Name:    %{fontname}-fonts
# No sane versionning upstream, use the most recent file datestamp
Version: 20100409
#Release: 1%{?dist}
Release: 0.1%{?dist}
Summary: General-purpose fonts released by Google as part of Android

Group:     User Interface/X
License:   ASL 2.0
URL:       http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
Source0:   %{download_root}NOTICE
Source1:   %{download_root}README.txt
Source10:  %{download_root}DroidSans.ttf
Source11:  %{download_root}DroidSans-Bold.ttf
Source12:  %{download_root}DroidSansJapanese.ttf
#DroidSansFallbackLegacy.ttf is an old version with less coverage
Source13:  %{download_root}DroidSansFallback.ttf
Source14:  %{download_root}DroidSansArabic.ttf
Source15:  %{download_root}DroidSansHebrew.ttf
Source16:  %{download_root}DroidSansThai.ttf
Source20:  %{download_root}DroidSansMono.ttf
Source30:  %{download_root}DroidSerif-Regular.ttf
Source31:  %{download_root}DroidSerif-Bold.ttf
Source32:  %{download_root}DroidSerif-Italic.ttf
Source33:  %{download_root}DroidSerif-BoldItalic.ttf
Source41:  %{name}-sans-fontconfig.conf
Source42:  %{name}-sans-mono-fontconfig.conf
Source43:  %{name}-serif-fontconfig.conf


BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc


%package -n %{fontname}-sans-fonts
Summary:   A humanist sans serif typeface
Requires:  fontpackages-filesystem
Obsoletes: %{name}-common <= 20090906-5.fc12

%description -n %{fontname}-sans-fonts
%common_desc

Droid Sans is a humanist sans serif typeface designed for user interfaces and
electronic communication.

%_font_pkg -n sans -f ??-%{fontname}-sans.conf DroidSans.ttf DroidSans-Bold.ttf DroidSansArabic.ttf DroidSansHebrew.ttf DroidSansJapanese.ttf DroidSansThai.ttf DroidSansFallback.ttf
%doc *.txt

%package -n %{fontname}-sans-mono-fonts
Summary:  A humanist monospace sans serif typeface
Requires: fontpackages-filesystem

%description -n %{fontname}-sans-mono-fonts
%common_desc

Droid Sans Mono is a humanist monospace sans serif typeface designed for user
interfaces and electronic communication.

%_font_pkg -n sans-mono -f ??-%{fontname}-sans-mono.conf DroidSansMono.ttf
%doc *.txt

%package -n %{fontname}-serif-fonts
Summary:  A contemporary serif typeface
Requires: fontpackages-filesystem

%description -n %{fontname}-serif-fonts
%common_desc

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.

%_font_pkg -n serif -f ??-%{fontname}-serif.conf DroidSerif*ttf
%doc *.txt

%prep
%setup -q -c -T
install -m 0644 -p %{SOURCE0} notice.txt
install -m 0644 -p %{SOURCE1} readme.txt


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p  %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
                    %{SOURCE14} %{SOURCE15} %{SOURCE16} \
                    %{SOURCE20} \
                    %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33}\
                    %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE41} \
        %{buildroot}%{_fontconfig_templatedir}/65-%{fontname}-sans.conf
install -m 0644 -p %{SOURCE42} \
        %{buildroot}%{_fontconfig_templatedir}/60-%{fontname}-sans-mono.conf
install -m 0644 -p %{SOURCE43} \
        %{buildroot}%{_fontconfig_templatedir}/59-%{fontname}-serif.conf

for fontconf in 65-%{fontname}-sans.conf \
                60-%{fontname}-sans-mono.conf \
                59-%{fontname}-serif.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done


%clean
rm -fr %{buildroot}


%changelog
* Sat Sep  5 2015 Nico Kadel-Garcia <nkadel@gmail.com> - 20100409-0.1
- Port to RHEL 7, roll back release to avoid upstream repository

* Sun Jul 25 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20100409-1
— Update to upstream's latest data dump
— Add Arabic, Hebrew, Thai coverage to Sans

* Mon Sep 28 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-5
— Tweak the fontconfig fixing

* Sun Sep 13 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-4
— follow the fontpackages template more closely
- 20090906-3
— more Behdad-suggested fontconfig tweaks

* Sun Sep  7 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-2
— first-level CJK fixes (as suggested by Behdad in bug #517789, complete fix
   needs the rpm changes traced in bug #521697)

* Sun Sep  6 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090906-1
— upstream stealth update

* Sat Jul 25 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20090320-3
— try to fit Japanese in

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- 1.0.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.112-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-5
— prepare for F11 mass rebuild, new rpm and new fontpackages

* Sat Jan 31 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-4
⬨ fix-up fontconfig installation for sans and mono

* Fri Jan 16 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-3
⁉ Workaround RHEL5 rpmbuild UTF-8 handling bug
- 1.0.112-2
⁍ Convert to new naming guidelines
⁍ Do strange stuff with Sans Fallback (CJK users please check)

* Tue Dec  9 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.112-1
փ Licensing bit clarified in bug #472635
շ Fedora submission

* Sun Nov 23 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.0.107-1
Ϫ Initial built using “fontpackages”

