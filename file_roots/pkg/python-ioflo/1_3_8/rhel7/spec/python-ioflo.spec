%global with_python3 1

%{!?__python2: %global __python2 /usr/bin/python%{?pybasever}}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%if 0%{?rhel} == 6
%global with_explicit_python27 1
%global pybasever 2.7
%global __python_ver 27
%global __python %{_bindir}/python%{?pybasever}
%global __python2 %{_bindir}/python%{?pybasever}
%global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global __os_install_post %{__python27_os_install_post}
%endif

%global _description \
Ioflo is a flow-based programming automated reasoning engine and automation \
operation system, written in Python.

%{!?python3_pkgversion:%global python3_pkgversion 3}

%global srcname ioflo

Name:           python-%{srcname}
Version:        1.3.8
Release:        3%{?dist}
Summary:        Flow-based programming interface

Group:          Development/Libraries
License:        MIT
URL:            http://ioflo.com
Source0:        http://pypi.python.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{srcname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python%{?__python_ver}-devel
BuildRequires:  python%{?__python_ver}-setuptools

%if 0%{?with_explicit_python27}
Requires: python%{?__python_ver}  >= 2.7.9-1
Provides: python-%{srcname}
%endif

%description    %{_description}

%package    -n  python2-%{srcname}
Summary:        %{summary}
Group:          Development/Libraries
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.



%if 0%{?with_python3}
%package    -n  python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Group:          Development/Libraries
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
## %{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides: python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python 3 version.
%endif


%prep
%setup -q -n %{srcname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
rm -rf %{buildroot}

%py2_install

%if 0%{?with_python3}
sed -i '1s|^#!%{__python3}|#!%{__python2}|' %{buildroot}/usr/bin/ioflo
%py3_install
%endif

%clean
rm -rf %{buildroot}

%files -n python2-%{srcname}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}2

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/%{srcname}3
%endif


%changelog
* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 1.3.8-3
- Add support for Python 3


* Fri Jan 12 2018 SaltStack Packaging Team <packaging@saltstack.com> - 1.3.8-2
- Support for Python 3 on RHEL 7 & 6
- Updated to use Python 2.7 on Redhat 6
- Removed support for Redhat 5

* Wed Aug  5 2015 Packaging <packaging@saltstack.com> - 1.3.8-1
- Build 1.3.8 for Salt implementation

* Tue May 26 2015 Erik Johnson <erik@saltstack.com> - 1.0.2-2
- Fix python dependency for Python 2 package

* Wed Nov 19 2014 Erik Johnson <erik@saltstack.com> - 1.0.2-1
- Updated to 1.0.2

* Thu Oct  2 2014 Erik Johnson <erik@saltstack.com> - 1.0.1-1
- Updated to 1.0.1

* Thu Aug 14 2014 Erik Johnson <erik@saltstack.com> - 0.9.39-2
- Fix dual deployment of ioflo executable

* Thu Jul 24 2014 Erik Johnson <erik@saltstack.com> - 0.9.39-1
- Updated to 0.9.39

* Wed Jul 23 2014 Erik Johnson <erik@saltstack.com> - 0.9.38-1
- Updated to 0.9.38

* Fri Jun 20 2014 Erik Johnson <erik@saltstack.com> - 0.9.35-1
- Initial build
