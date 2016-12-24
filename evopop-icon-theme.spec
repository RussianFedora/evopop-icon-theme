%global theme	EvoPop
%global daterev	20161224git5d0825

Summary:	Default icon theme for OzonOS
Name:		evopop-icon-theme
Version:	0.7
Release:	0.5.%{?daterev}%{?dist}

License:	CC-BY
Group:		User Interface/Desktops
URL:		https://github.com/solus-project/evopop-icon-theme
Source0:	%{name}-%{version}-%{daterev}.tar.xz

BuildRequires:	git
BuildRequires:	automake

BuildArch:  noarch

%description
%{theme} is the official icon theme for Ozon OS.


%prep
%setup -q

%build
./autogen.sh

%install
%{make_install}

touch %{buildroot}%{_datadir}/icons/%{theme}/icon-theme.cache


%post
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/%{theme} || :
touch --no-create %{_datadir}/icons/%{theme} &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/%{theme} &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/%{theme} &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/%{theme} &>/dev/null || :


%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_datadir}/icons/%{theme}/scalable/apps/*.svg
%{_datadir}/icons/%{theme}/scalable/devices/*.svg
%{_datadir}/icons/%{theme}/scalable/places/*.svg
%{_datadir}/icons/%{theme}/scalable/panel/*.svg
%{_datadir}/icons/%{theme}/??x??/*
%{_datadir}/icons/%{theme}/???x???/*
%{_datadir}/icons/%{theme}/symbolic
%{_datadir}/icons/%{theme}/index.theme
%ghost %{_datadir}/icons/%{theme}/icon-theme.cache


%changelog
* Sat Dec 24 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 0.7-0.5.20161224git5d0825
- added weather, cheese, totem, xchat, gnome-documents, clipit, calendar icons
- change license to CC-BY
- fix E: script-without-shebang

* Thu Oct  6 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 0.7-0.4.20161006git592000
- added symlinks to new org.gnome.Nautilus icon

* Thu Apr 14 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 0.7-0.3.20160414gitb2d1fb.R
- added symlinks to new org.gnome.Software icon

* Mon Jan 25 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 0.7-0.2.20160125git44eafb.R
- added logview.png, display.png, pavucontrol.png, rpmdrake.png
- create some symlinks for LibreOffice in ROSA Linux

* Mon Jan 25 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 0.7-0.1.20160125gitfd1c65.R
- change url to forked theme
- create many new symlinks

* Wed Jul 15 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.4.20150601git290909.R
- update to last snapshot

* Mon May 18 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.3.20150515gitcf6f39.R
- update to 20150515gitcf6f39
- drop ghost tag

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.2.20150501gitfacf86.R
- update %%files section

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.1.20150501gitfacf86.R
- update to last snapshot 20150501gitfacf86

* Sat Apr 11 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.3-0.1.20150411gitb97c1b.R
- initial build
