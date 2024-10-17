Name: 	 	libopensync-plugin-file
Summary: 	File plugin for OpenSync synchronization framework
Version: 	0.22
Epoch:		1
Release: 	%{mkrel 3}
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
URL:		https://www.opensync.org
License:	LGPLv2+
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	fam-devel
Requires:	libopensync >= %{epoch}:%{version}
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
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*


