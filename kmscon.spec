Name:           kmscon
Version:        10.1.1
Release:        1
Summary:        Userspace KMS/DRM virtual console terminal emulator
License:        MIT AND LGPL-2.1-or-later AND OFL-1.1
Group:          Terminals
URL:            https://github.com/kmscon/kmscon
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:    meson
BuildOption:    -Dlibseat=enabled
BuildOption:    -Dtests=false
# pango font backend; the freetype one needs fontconfig >= 2.16
BuildOption:    -Dfont_pango=enabled
BuildOption:    -Dfont_freetype=disabled

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  python
BuildRequires:  ncurses
BuildRequires:  xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(libtsm) >= 4.8.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(systemd)

%description
Kmscon is a simple terminal emulator based on Linux kernel mode setting
(KMS). It replaces the in-kernel VT console with a userspace one, with
DRM/GL rendering, unicode, multi-monitor and font support.

%install
%meson_install
# upstream installs the PAM file to %%{_libdir}/pam.d, PAM reads /etc/pam.d
install -Dm644 %{buildroot}%{_libdir}/pam.d/kmscon %{buildroot}%{_sysconfdir}/pam.d/kmscon
rm -r %{buildroot}%{_libdir}/pam.d

%files
%license COPYING
%doc NEWS.md README.md
%dir %{_sysconfdir}/kmscon
%config(noreplace) %{_sysconfdir}/kmscon/kmscon.conf.example
%config(noreplace) %{_sysconfdir}/pam.d/kmscon
%{_bindir}/kmscon
%{_bindir}/kmscon-launch-gui
%{_libdir}/kmscon/
%{_unitdir}/kmscon.service
%{_unitdir}/kmsconvt@.service
%{_datadir}/terminfo/k/kmscon
%{_mandir}/man1/kmscon.1*
%{_mandir}/man5/kmscon.conf.5*
