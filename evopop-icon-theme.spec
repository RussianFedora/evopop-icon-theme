%global theme	EvoPop
%global daterev	20150601git290909

Summary:	Default icon theme for OzonOS
Name:		evopop-icon-theme
Version:	0.6
Release:	0.4.%{?daterev}%{?dist}

License:	GPLv3
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

touch $RPM_BUILD_ROOT%{_datadir}/icons/%{theme}/icon-theme.cache


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
* Wed Jul 15 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.4.20150601git290909.R
- update to last snapshot

* Mon May 18 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.3.20150515gitcf6f39.R
- update to 20150515gitcf6f39
- drop ghost tag

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.2.20150501gitfacf86.R
- update %files section

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.1.20150501gitfacf86.R
- update to last snapshot 20150501gitfacf86

* Sat Apr 11 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.3-0.1.20150411gitb97c1b.R
- initial build
