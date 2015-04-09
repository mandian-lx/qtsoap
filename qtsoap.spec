%define major 2.7.0
%define libname %mklibname qtsoap %{major}
%define devname %mklibname -d qtsoap

Name:           qtsoap
Version:        2.7
Release:        1
Summary:        The Simple Object Access Protocol Qt-based client side library

Group:          Development/C
License:        LGPLv2 with exceptions or GPLv3
URL:            http://qt.nokia.com/products/appdev/add-on-products/catalog/4/Utilities/qtsoap/
Source0:        http://get.qt.nokia.com/qt/solutions/lgpl/qtsoap-%{version}_1-opensource.tar.gz
Patch0:         qtsoap-2.7_1-opensource-install-pub-headers.patch


BuildRequires:  qt4-devel

%description
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.

%package -n     %{libname}
Summary:        The Simple Object Access Protocol Qt-based client side library
Group:          System/Libraries

%description -n %{libname}
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to invoke web
services and get responses from Qt-based applications.

%package        %devname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}

%description    %{devname}
Development files for %{name}.

%prep
%setup -q -n qtsoap-%{version}_1-opensource

# headers are not installed for shared library
%patch0 -p1 -b .install-pub-headers

sed -i 's:$$DESTDIR:%{_libdir}:g' buildlib/buildlib.pro

%build
# we want shared library
echo "SOLUTIONS_LIBRARY = yes" > config.pri

echo "QTSOAP_LIBNAME = \$\$qtLibraryTarget(qtsoap)" >> common.pri
echo "VERSION=%{version}" >> common.pri

qmake PREFIX=%{_prefix}
make %{?_smp_mflags}


%install
make INSTALL_ROOT=%{buildroot} install


%files -n %libname
%doc README.TXT LGPL_EXCEPTION.txt LICENSE.GPL3 LICENSE.LGPL
%{_qt_libdir}/libqtsoap.so.*

%files -n %devname
%doc LGPL_EXCEPTION.txt LICENSE.GPL3 LICENSE.LGPL
%{_qt_libdir}/libqtsoap.so
%{_qt_includedir}/QtSoap/

