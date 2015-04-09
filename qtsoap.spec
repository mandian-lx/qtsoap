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

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
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


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.TXT LGPL_EXCEPTION.txt LICENSE.GPL3 LICENSE.LGPL
%{_qt4_libdir}/libqtsoap.so.*

%files devel
%doc LGPL_EXCEPTION.txt LICENSE.GPL3 LICENSE.LGPL
%{_qt4_libdir}/libqtsoap.so
%{_qt4_includedir}/QtSoap/



%changelog
* Wed Oct 15 2014 umeabot <umeabot> 2.7-7.mga5
+ Revision: 739199
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 2.7-6.mga5
+ Revision: 688560
- Mageia 5 Mass Rebuild

* Fri Oct 18 2013 umeabot <umeabot> 2.7-5.mga4
+ Revision: 517906
- Mageia 4 Mass Rebuild

* Sun Jan 13 2013 umeabot <umeabot> 2.7-4.mga3
+ Revision: 380055
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Jun 17 2012 shlomif <shlomif> 2.7-3.mga3
+ Revision: 261300
- Got to build + rpmlint fixes
- Imported from Fedora RawHide


* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Jaroslav Reznik <jreznik@redhat.com> - 2.7-2
- libqtsoap library name

* Thu May 19 2011 Jaroslav Reznik <jreznik@redhat.com> - 2.7-1
- fix version

* Tue Oct 26 2010 Jaroslav Reznik <jreznik@redhat.com> - 1.7-1
- Initial spec file
