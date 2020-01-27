%bcond_with python2 
%bcond_without python3

%{!?python3_pkgversion:%global python3_pkgversion 3}

%global _description \
Ioflo is a flow-based programming automated reasoning engine and automation \
operation system, written in Python.

%global srcname ioflo

Name:           python-%{srcname}
Version:        1.3.8
Release:        5%{?dist}
Summary:        Flow-based programming interface

Group:          Development/Libraries
License:        MIT
URL:            http://ioflo.com
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{srcname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description    %{_description}

%if %{with python2}
%package -n     python2-%{srcname}
Summary:        %{summary}
Group:          Development/Libraries
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.
%endif


%if %{with python3}
%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Group:          Development/Libraries
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python 3 version.
%endif


%prep
%autosetup -n %{srcname}-%{version}

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
%{python2_sitelib}/*
%{_bindir}/%{srcname}
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}3
%endif


%changelog
* Wed Jun 05 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.3.8-5
- Added support for Redhat 7 Python 3.6, and support for Python 2 packages optional
- Removed Redhat 6 support, replaced pypi.python.org with files.pythonhosted.org 

* Thu Apr 04 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.3.8-4
- Add support for Python 3.6

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
