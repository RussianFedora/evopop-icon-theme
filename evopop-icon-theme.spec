%global theme	EvoPop
%global daterev	20150411gitb97c1b

Summary:	Default icon theme for OzonOS
Name:		evopop-icon-theme
Version:	0.3
Release:	0.1.%{?daterev}%{?dist}

License:	GPLv3
Group:		User Interface/Desktops
URL:		https://github.com/solus-project/evopop-icon-theme
Source0:	%{name}-%{version}-%{daterev}.tar.xz

BuildRequires:	git

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
%{_datadir}/icons/%{theme}


%changelog
* Sat Apr 11 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.3-0.1.20150411gitb97c1b.R
- initial build
