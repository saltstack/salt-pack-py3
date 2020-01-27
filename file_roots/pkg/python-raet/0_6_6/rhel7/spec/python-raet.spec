%bcond_with python2 
%bcond_without python3

%{!?python3_pkgversion:%global python3_pkgversion 3}


%global _description \
A high level, stack based communication protocol for network and IPC communication

%global srcname raet

Name:       python-%{srcname}
Version:    0.6.6
Release:    7%{?dist}
Summary:    Reliable Asynchronous Event Transport Protocol

License:    ASL 2.0
URL:        https://github.com/RaetProtocol/raet
Source0:    http://pypi.python.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
## Patch0:     raet-0.6.6.patch

BuildArch:  noarch

%description    %{_description}


%if %{with python2}
# We don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_setup
}
%endif


%if %{with python2}
%package    -n  python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
BuildRequires:  python2-libnacl >= 1.4.3-1
BuildRequires:  python2-ioflo >= 1.3.8-1
Requires:  python2-six
Requires:  python2-ioflo >= 1.3.8-1
Requires:  python2-ioflo >= 1.3.8-1
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-ioflo >= 1.3.8-1
BuildRequires:  python%{python3_pkgversion}-libnacl >= 1.4.3-1
Requires:  python%{python3_pkgversion}-six
Requires:  python%{python3_pkgversion}-ioflo >= 1.3.8-1
Requires:  python%{python3_pkgversion}-libnacl >= 1.4.3-1
##%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides: python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python 3 version.
%endif


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


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


## %check
## %{__python2} setup.py test
## %{__python3} setup.py test


%if %{with python2}
%files -n python2-%{srcname}
%{_bindir}/raetflo
## %%{_bindir}/raetflo2
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py*.egg-info
%exclude %{python2_sitelib}/systest*
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%{_bindir}/raetflo
## %%{_bindir}/raetflo3
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info
%exclude %{python3_sitelib}/systest*
%endif


%changelog
* Wed Jun 05 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.6.6-7
- Removed support for Amazon and Redhat 6, made support for Python 2 packages optional

* Tue Apr 09 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.6.6-6
- Add support for Python 3.6 for RHEL 7

* Tue Apr 24 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.6.6-5
- Updated build requires for libnacl

* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.6.6-4
- Add support for Python 3

* Tue Jan 16 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.6.6-3
- Support for Python 3 on RHEL 7 & 6
- Removed support for RHEL 5

* Mon Jul 17 2017 SaltStack Packaging Team <packaging@saltstack.com> - 0.6.6-2
- Updated to use Python 2.7 on Redhat 6

* Tue Jan 17 2017 Packaging <packaging@saltstack.com> - 0.6.6-1
- Patched fix to overcome lack of kwargs support with decode in python2.6

* Wed Dec  7 2016 Packaging <packaging@saltstack.com> - 0.6.5-1
- Build 0.6.5 for Salt implementation on various versions Redhat

* Thu Aug  6 2015 Packaging <packaging@saltstack.com> - 0.6.3-2
- Build 0.6.3 for Salt implementati
on on various versions Redhat


