%define name	libopensync-plugin-file
%define version	0.20
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	File plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.gz
URL:		http://www.opensync.org
License:	GPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= %{version}
BuildRequires:	fam-devel

Obsoletes:	multisync-backup
Provides:	multisync-backup

%description
This plugin allows applications using OpenSync to synchronise to and from
files stored on disk.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*


