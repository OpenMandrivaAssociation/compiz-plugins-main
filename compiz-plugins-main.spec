%define _disable_ld_no_undefined 1
%define oldname compiz-fusion-plugins-main

Summary:         Compiz Main Plugin Set for compiz
Name:            compiz-plugins-main
Version:         0.9.7.2
Release:         1
Group:           System/X11
License:         GPLv2+
URL:             http://www.compiz.org/
Source0:         http://releases.compiz.org/%{version}/%{name}-%{version}.tar.bz2
Patch1:  0001-Use-appropriate-animation-for-screenlets.patch
Patch2:  0002-Use-a-more-Mandriva-y-blue-for-expo.patch

BuildRequires:   cmake
BuildRequires:   intltool
BuildRequires:   xsltproc
BuildRequires:   boost-devel
BuildRequires:   compiz-devel compiz
BuildRequires:   jpeg-devel
BuildRequires:   mesaglu-devel
BuildRequires:   pkgconfig(cairo)
BuildRequires:   pkgconfig(gconf-2.0)
BuildRequires:   pkgconfig(gl)
BuildRequires:   pkgconfig(pango)
BuildRequires:   pkgconfig(xtst)

Requires: compiz
Obsoletes: compiz-extra
Obsoletes: beryl-plugins
%rename %{oldname}

%description
This is the main plugin set from the Compiz community. This is a 
combination of the Compiz Extras and Beryl communities

Contains: animation expo ezoom jpeg neg opacify put resizeinfo ring
scaleaddon snap text thumbnail vpswitch wall winrules workarounds.

#----------------------------------------------------------------------------
%package devel
Summary: Development files for Compiz Main Plugin Set for compiz
Group: Development/X11
Requires: %{name} = %{version}-%{release}
%rename %{oldname}-devel

%description devel
Development files for Compiz Main Plugin Set for compiz

#----------------------------------------------------------------------------
%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%cmake \
	-DCOMPIZ_INSTALL_GCONF_SCHEMA_DIR=%{_sysconfdir}/gconf/schemas \
	-DCOMPIZ_DISABLE_SCHEMAS_INSTALL=TRUE \
	-DCOMPIZ_PACKAGING_ENABLED=TRUE

%install
rm -rf %{buildroot}
%makeinstall_std -C build

#----------------------------------------------------------------------------
%files
%{_sysconfdir}/gconf/schemas/compiz*.schemas
%{_libdir}/compiz/*.so
%{_datadir}/compiz/colorfilter/
%{_datadir}/compiz/mag/
%{_datadir}/compiz/*.xml

%files devel
%{_includedir}/compiz/animation/
%{_includedir}/compiz/mousepoll/
%{_includedir}/compiz/text/
%{_libdir}/pkgconfig/*.pc

