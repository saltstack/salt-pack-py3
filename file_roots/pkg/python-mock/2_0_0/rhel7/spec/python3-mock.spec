# keeping python3 subpackage as stdlib mock lives in a different namespace
# Some people may have not fixed their imports

%global mod_name mock
%global python3_pkgversion 36

Name:           python3-mock
Version:        2.0.0
Release:        3%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        https://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.


%package -n python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-six >= 1.9.0
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}
Requires:    python%{python3_pkgversion}-pbr
Requires:    python%{python3_pkgversion}-six >= 1.9.0

%description -n python%{python3_pkgversion}-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.


%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-mock
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-pbr
BuildRequires:  python%{python3_other_pkgversion}-six >= 1.9.0
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{mod_name}}
Requires:    python%{python3_other_pkgversion}-pbr
Requires:    python%{python3_other_pkgversion}-six >= 1.9.0

%description -n python%{python3_other_pkgversion}-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.
%endif


%prep
%setup -q -n %{mod_name}-%{version}
# Use builting unittest
find -name \*.py | xargs sed -i -e s/unittest2/unittest/g


%build
%{py3_build}
%if 0%{?python3_other_pkgversion}
%{py3_other_build}
%endif


%install
%{py3_install}
%if 0%{?python3_other_pkgversion}
%{py3_other_install}
%endif


%check
%{__python3} -m unittest discover
%if 0%{?python3_other_pkgversion}
%{__python3_other} -m unittest discover
%endif


%files -n python%{python3_pkgversion}-mock
%license LICENSE.txt
%doc docs/*
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{mod_name}

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-mock
%license LICENSE.txt
%doc docs/*
%{python3_other_sitelib}/*.egg-info
%{python3_other_sitelib}/%{mod_name}
%endif

%changelog
* Sun Sep 22 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2.0.0-3
- Support Redhat 7 Python 3.6 without EPEL

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com>- 2.0.0-2
- Rebuilt to change main python from 3.4 to 3.6

* Mon Nov 5 2018 Orion Poplawski <orion@nwra.com> - 2.0.0-1
- Python 3 packaging for EPEL
