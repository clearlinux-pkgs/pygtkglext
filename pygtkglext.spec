#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pygtkglext
Version  : 1.0.1
Release  : 7
URL      : https://sourceforge.net/projects/gtkglext/files/pygtkglext/1.0.1/pygtkglext-1.0.1.tar.gz
Source0  : https://sourceforge.net/projects/gtkglext/files/pygtkglext/1.0.1/pygtkglext-1.0.1.tar.gz
Summary  : Python Bindings for GtkGLExt
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: pygtkglext-data = %{version}-%{release}
Requires: pygtkglext-license = %{version}-%{release}
Requires: pygtkglext-python = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : freetype-dev
BuildRequires : gfortran
BuildRequires : glu-dev
BuildRequires : gtk+-dev
BuildRequires : gtkglext-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(pygtk-2.0)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xt)
BuildRequires : pygtk
BuildRequires : pygtk-legacypython
BuildRequires : python-dev
BuildRequires : python3-dev
Patch1: update.patch

%description
PyGtkGLExt is Python language bindings for GtkGLExt, OpenGL Extension to GTK.
It enables Python programmers to write OpenGL applications with PyGTK2.

%package data
Summary: data components for the pygtkglext package.
Group: Data

%description data
data components for the pygtkglext package.


%package dev
Summary: dev components for the pygtkglext package.
Group: Development
Requires: pygtkglext-data = %{version}-%{release}
Provides: pygtkglext-devel = %{version}-%{release}

%description dev
dev components for the pygtkglext package.


%package legacypython
Summary: legacypython components for the pygtkglext package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pygtkglext package.


%package license
Summary: license components for the pygtkglext package.
Group: Default

%description license
license components for the pygtkglext package.


%package python
Summary: python components for the pygtkglext package.
Group: Default

%description python
python components for the pygtkglext package.


%prep
%setup -q -n pygtkglext-1.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545262835
%configure --disable-static PYTHON=/usr/bin/python2
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1545262835
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pygtkglext
cp COPYING %{buildroot}/usr/share/package-licenses/pygtkglext/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/pygtkglext/COPYING.LIB
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/pygtk/2.0/defs/gdkglext-types.defs
/usr/share/pygtk/2.0/defs/gdkglext.defs
/usr/share/pygtk/2.0/defs/gtkglext.defs

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/pygtkglext-1.0.pc

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pygtkglext/COPYING
/usr/share/package-licenses/pygtkglext/COPYING.LIB

%files python
%defattr(-,root,root,-)
