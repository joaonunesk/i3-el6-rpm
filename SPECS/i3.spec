Name:          	i3

Version:       	4.2
URL: 		http://i3wm.org
Group:         	Unspecified
Summary:       	Improved tiling window manager

Release:	1.el6
Source: 	%{name}-%{version}.tar.gz
Packager:  	João Nunes <joaonunesk@gmail.com>

Distribution:  	Centos Project
BuildArch:     	x86_64

License:       	BSD

BuildRequires: 	epel-release xcb-util-devel libxcb-devel xcb-proto libev-devel libxkbfile-devel libXcursor-devel libX11-devel yajl-devel bison flex asciidoc rxvt-unicode xorg-x11-apps dmenu xorg-x11-fonts-misc dzen2 startup-notification-devel pcre-devel alsa-lib-devel wireless-tools-devel libconfuse-devel tar xcb-util-keysyms-devel xcb-util-wm-devel  

%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code.

Please be aware that i3 is primarily targeted at advanced users and developers. 

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/etc/i3/config
/etc/i3/config.keycodes
/etc/i3/welcome
/usr/bin/i3
/usr/bin/i3-config-wizard
/usr/bin/i3-dump-log
/usr/bin/i3-input
/usr/bin/i3-migrate-config-to-v4
/usr/bin/i3-msg
/usr/bin/i3-nagbar
/usr/bin/i3-sensible-editor
/usr/bin/i3-sensible-pager
/usr/bin/i3-sensible-terminal
/usr/bin/i3bar
/usr/include/i3/ipc.h
/usr/share/applications/i3.desktop
/usr/share/xsessions/i3.desktop

%changelog
* Mon Mar 30 2015 João Nunes <joaonunesk@gmail.com> - 1.0.0-1
- initial revision
