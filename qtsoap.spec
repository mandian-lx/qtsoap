%define debug_package %nil

%define commit 1fca9c330d8548d84fccb66407fbaf3aae122d17
%define shortcommit %(c=%{commit}; echo ${c:0:7})

%define project_name qt-solutions

%define major 2.7.0
%define libname %mklibname qtsoap %{major}
%define devname %mklibname -d qtsoap

Summary:	The Simple Object Access Protocol Qt-based client side library
Name:		qtsoap
Version:	%{major}
Release:	4
Group:		Development/KDE and Qt
License:	BSD
Url:		https://github.com/qtproject/qt-solutions/
Source0:	https://github.com/qtproject/qt-solutions/archive/%{commit}/%{project_name}-%{commit}.tar.gz
# headers are not installed for shared library
Patch0:		qtsoap-2.7_1-opensource-install-pub-headers.patch
Patch1:		qtsoap-2.7_1-port-to-qt5.patch

BuildRequires:	qt5-devel

%description
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	The Simple Object Access Protocol Qt-based client side library
Group:		System/Libraries

%description -n %{libname}
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.

%files -n %{libname}
%doc README.TXT
%{_qt5_libdir}/libqtsoap.so.*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%doc README.TXT
%doc doc examples
%{_qt5_libdir}/libqtsoap.so
%{_qt5_includedir}/QtSoap/

#--------------------------------------------------------------------

%prep
%setup -q -n %{project_name}-%{commit}/%{name}
%apply_patches

sed -i 's:$$DESTDIR:%{_libdir}:g' buildlib/buildlib.pro

%build
# we want shared library
echo "SOLUTIONS_LIBRARY = yes" > config.pri

echo "QTSOAP_LIBNAME = \$\$qt5LibraryTarget(qtsoap)" >> common.pri
echo "VERSION=%{version}" >> common.pri

%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

