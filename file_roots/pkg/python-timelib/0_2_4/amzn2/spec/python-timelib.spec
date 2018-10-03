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
%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global __os_install_post %{__python27_os_install_post}
%endif

%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%endif

%define debug_package %{nil}

%global _description \
timelib is a short wrapper around phps internal timelib modules \
It currently only provides a few functions: \
\
timelib.strtodatetime \
timelib.strtotime

%global srcname timelib

Name:           python%{?__python_ver}-%{srcname}
Version:        0.2.4
Release:        4%{?dist}
Summary:        Parse English textual date descriptions
Group:          Development/Languages/Python

## License:        PHP and zlib
License:        MIT

URL:            http://pypi.python.org/pypi/timelib/
Source0:        http://pypi.python.org/packages/source/t/%{srcname}/%{srcname}-%{version}.zip

BuildRoot:      %{_tmppath}/%{srcname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch


BuildRequires:  python%{?__python_ver}-devel
BuildRequires:  python%{?__python_ver}-setuptools


# We don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%if 0%{?with_python3}
%filter_provides_in %{python3_sitearch}/.*\.so$
%endif
%filter_setup
}

%description    %{_description} 

%package    -n  python2-%{srcname}
Summary:        %{summary}
Group:          %{group}
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
%endif
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.


%if 0%{?with_python3}
%package    -n  python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Group:          %{group}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?with_amzn2}
BuildRequires:  python%{python3_pkgversion}-rpm-macros
%endif
Provides:       python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-%{srcname} %{_description} 
Python 3 version.
%endif

%prep
##%%autosetup -n %{srcname}-%{version}
%setup -n %{srcname}-%{version}

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
%py3_install
%endif

%clean
rm -rf %{buildroot}


%files -n python2-%{srcname}
%defattr(-,root,root,-)
%{python2_sitearch}/%{srcname}*.so
%{python2_sitearch}/%{srcname}*.egg-info
%exclude %{_libdir}/debug/
%exclude %{_libdir}/../src/debug/

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
%{python3_sitearch}/%{srcname}*.so
%{python3_sitearch}/%{srcname}*.egg-info
%endif

%changelog
* Tue Oct 02 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.2.4-4
- Ported to support Python 3 on Amazon Linux 2

* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.2.4-3
- Add support for Python 3

* Tue Jan 16 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.2.4-2
- Support for Python 3 on RHEL 7 & 6
- Updated to use Python 2.7 on Redhat 6
- Removed support for RHEL 5

* Fri Aug  7 2015 Packaging <packaging@saltstack.com> - 0.2.4-1
- Initial build 0.2.4 for Salt implementation

