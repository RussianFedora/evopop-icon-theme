%global theme	EvoPop-0.7
%global daterev	20170913gitb05cfb

Summary:	Default icon theme for OzonOS
Name:		evopop-icon-theme-0.7
Version:	0.7
Release:	0.1.%{?daterev}%{?dist}

License:	CC-BY
Group:		User Interface/Desktops
URL:		https://github.com/solus-project/evopop-icon-theme
Source0:	%{name}-%{version}-%{daterev}.tar.xz

BuildRequires:	git
BuildRequires:	automake

BuildArch:  noarch

%description
%{theme} is the official icon theme for Ozon OS. This is an old theme 0.7
version. In Fedora repository now presents evopop-icon-theme 0.11 and
older.


%prep
%setup -q

%build
./autogen.sh

%install
%{make_install}


touch %{buildroot}%{_datadir}/icons/%{theme}/icon-theme.cache


%post
%{_bindir}/gtk-update-icon-cache -f --quiet %{_datadir}/icons/%{theme} || :
touch --no-create %{_datadir}/icons/%{theme} &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/%{theme} &>/dev/null
    gtk-update-icon-cache -f %{_datadir}/icons/%{theme} &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache -f %{_datadir}/icons/%{theme} &>/dev/null || :


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
* Wed Sep 13 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 0.7-0.1.20170913gitb05cfb
- rename evopop-icon-theme package to evopop-icon-theme-0.7 to provide old icons

