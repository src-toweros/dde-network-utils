Name:           dde-network-utils
Version:        5.3.0.3
Release:        1
Summary:        Deepin desktop-environment - network utils
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-network-utils
Source0:        %{name}_%{version}.orig.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  dde-qt-dbus-factory-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(gsettings-qt)

%description
Deepin desktop-environment - network utils.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{name}-%{version}
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/lib$|/%{_lib}|' dde-network-utils.pro

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%{_libdir}/lib*.so.1
%{_libdir}/lib*.so.1.*
%{_datadir}/%{name}/

%files devel
%{_includedir}/libddenetworkutils/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Thu Jul 08 2021 weidong <weidong@uniontech.com> - 5.3.0.3-1
- Update 5.3.0.3

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.4-1
- Package init
