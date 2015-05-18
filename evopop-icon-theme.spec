%global theme	EvoPop
%global daterev	20150515gitcf6f39

Summary:	Default icon theme for OzonOS
Name:		evopop-icon-theme
Version:	0.6
Release:	0.3.%{?daterev}%{?dist}

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


%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_datadir}/icons/%{theme}/scalable/apps/*.svg
%{_datadir}/icons/%{theme}/scalable/devices/*.svg
%{_datadir}/icons/%{theme}/scalable/places/*.svg
%{_datadir}/icons/%{theme}/scalable/emblems/*.svg
%{_datadir}/icons/%{theme}/??x??/*
%{_datadir}/icons/%{theme}/???x???/*
%{_datadir}/icons/EvoPop/symbolic
%{_datadir}/icons/EvoPop/index.theme


%changelog
* Mon May 18 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.3.20150515gitcf6f39.R
- update to 20150515gitcf6f39
- drop ghost tag

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.2.20150501gitfacf86.R
- update %files section

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.6-0.1.20150501gitfacf86.R
- update to last snapshot 20150501gitfacf86

* Sat Apr 11 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.3-0.1.20150411gitb97c1b.R
- initial build
