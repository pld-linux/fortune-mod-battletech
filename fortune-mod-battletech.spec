Summary:	Collection of fortunes from Battletech novels
Summary(pl):	Kolekcja fortunek z nowel Battletech
Name:		fortune-mod-battletech
Version:	0.1
Release:	1
License:	Free to use but restricted
Group:		Applications/Games
Source0:	http://lamer0.com/%{name}-%{version}.tar.gz
# Source0-md5:	0800619d9f1e9dcf3af05fb1ddf17ffa
URL:		http://freshmeat.net/projects/fortune-mod-battletech2/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod-battletech is a fortune database that contains a series of
quotes from various Battletech novels.

%description -l pl
Fortune-mod-battletech to baza fortunek zawieraj±ca seriê cytatów z
ró¿nych nowel Batteltech.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes
install fortune-mod-battletech $RPM_BUILD_ROOT%{_datadir}/games/fortunes/battletech
install fortune-mod-battletech.dat $RPM_BUILD_ROOT%{_datadir}/games/fortunes/battletech.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/games/fortunes/*
