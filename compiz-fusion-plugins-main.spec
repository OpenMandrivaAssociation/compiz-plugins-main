%define name compiz-fusion-plugins-main
%define newname compiz-plugins-main
%define version 0.8.6
%define rel 3
%define git 0

%if %{git}
%define srcname plugins-main-%{git}.tar.lzma
%define distname plugins-main
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{newname}-%{version}.tar.bz2
%define distname %{newname}-%{version}
%define release %mkrel %{rel}
%endif


Summary: Compiz Fusion Main Plugin Set for compiz
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{srcname}
Patch1:  0001-Use-appropriate-animation-for-screenlets.patch
Patch2:  0002-Use-a-more-Mandriva-y-blue-for-expo.patch
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{newname}-%{version}-%{release}-buildroot
BuildRequires: dbus-devel
BuildRequires: compiz-devel >= %{version}
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: compiz-bcop
BuildRequires: libGConf2-devel
BuildRequires: MesaGLU-devel
BuildRequires: jpeg-devel
BuildRequires: pango-devel
Requires: compiz

Obsoletes: compiz-extra
Obsoletes: beryl-plugins
#Obsoletes: compiz-fusion-plugins-main
#Provides: compiz-fusion-plugins-main

%description
This is the main plugin set from the Compiz Fusion community.

This is a combination of the Compiz Extras and Beryl communities

#----------------------------------------------------------------------------

%package devel
Summary: Development files for Compiz Fusion Main Plugin Set for compiz
Group: Development/X11
#Obsoletes: compiz-fusion-plugins-main-devel
#Provides: compiz-fusion-plugins-main-devel

%description devel
Development files for Compiz Fusion Main Plugin Set for compiz

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}
%patch1 -p1
%patch2 -p1

%build
%if %{git}
  # This is a CVS snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la -exec rm -f {} \;
%find_lang %{newname}

%clean
rm -rf %{buildroot}

#----------------------------------------------------------------------------

%files -f %{newname}.lang
%defattr(-,root,root)
%{_libdir}/compiz/lib*.a
%{_libdir}/compiz/lib*.so
%{_datadir}/compiz/*.xml
%dir %{_datadir}/compiz/filters
%{_datadir}/compiz/filters/*
%{_datadir}/compiz/*/*.png


%files devel
%{_includedir}/compiz/*.h
%{_libdir}/pkgconfig/*.pc



