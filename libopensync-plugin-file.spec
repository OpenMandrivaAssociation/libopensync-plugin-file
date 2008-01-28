%define name	libopensync-plugin-file
%define version	0.36
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	File plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	GPLv2+
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= %{version}
BuildRequires:	fam-devel
BuildRequires:	cmake
Obsoletes:	multisync-backup
Provides:	multisync-backup

%description
This plugin allows applications using OpenSync to synchronise to and from
files stored on disk.

%prep
%setup -q

%build
%cmake
%make
										
%install
rm -rf $RPM_BUILD_ROOT
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync-1.0/plugins/*
%{_datadir}/opensync-1.0/defaults/*
