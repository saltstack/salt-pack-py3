%bcond_with python2
%bcond_without python3
%bcond_with tests


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
Release:        5%{?dist}
Summary:        Parse English textual date descriptions
Group:          Development/Languages/Python

## License:        PHP and zlib
License:        MIT

URL:            http://pypi.python.org/pypi/timelib/
Source0:        http://pypi.python.org/packages/source/t/%{srcname}/%{srcname}-%{version}.zip

BuildRoot:      %{_tmppath}/%{srcname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch


# We don't want to provide private python extension libs
%{?filter_setup:
%if %{with python2}
%filter_provides_in %{python2_sitearch}/.*\.so$
%endif
%if %{with python3}
%filter_provides_in %{python3_sitearch}/.*\.so$
%endif
%filter_setup
}

%description    %{_description}

%if %{with python2}
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
%endif


%if %{with python3}
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

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%clean
rm -rf %{buildroot}


%if %{with python2}
%files -n python2-%{srcname}
%defattr(-,root,root,-)
%{python2_sitearch}/%{srcname}*.so
%{python2_sitearch}/%{srcname}*.egg-info
%exclude %{_libdir}/debug/
%exclude %{_libdir}/../src/debug/
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
%{python3_sitearch}/%{srcname}*.so
%{python3_sitearch}/%{srcname}*.egg-info
%endif

%changelog
* Tue Jun 11 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.2.4-5
- Made support for Python 2 optional

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

