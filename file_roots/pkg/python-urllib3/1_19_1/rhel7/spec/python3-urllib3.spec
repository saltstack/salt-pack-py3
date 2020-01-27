# FIXME some missing dependencies for tests of python3_other 

%bcond_with tests
%bcond_with python3_other_tests

%global pypi_name urllib3

%global _description Python 3 HTTP module with connection pooling and file POST abilities.

%global python3_pkgversion 36
%global python3_other_pkgversion 0

Name:           python3-%{pypi_name}
Version:        1.19.1
Release:        6%{?dist}
Summary:        Python 3 HTTP library with thread-safe connection pooling and file post

License:        MIT
URL:            http://%{pypi_name}.readthedocs.org/
Source0:        http://pypi.python.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
## Source0:        %%pypi_source

BuildArch:      noarch

%description
%_description

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For unittests
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-coverage
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-pysocks
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-tornado
%endif

%if 0%{?python3_other_pkgversion}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
# For unittests
%if %{with tests}
%if %{with python3_other_tests}
BuildRequires:  python%{python3_other_pkgversion}-coverage
BuildRequires:  python%{python3_other_pkgversion}-mock
BuildRequires:  python%{python3_other_pkgversion}-nose
BuildRequires:  python%{python3_other_pkgversion}-pysocks
BuildRequires:  python%{python3_other_pkgversion}-six
BuildRequires:  python%{python3_other_pkgversion}-tornado
%endif
%endif
%endif

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Python %{python3_version} HTTP library with thread-safe connection pooling and file post
Requires:       ca-certificates
Requires:       python%{python3_pkgversion}-pysocks
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%_description
This package is for Python3 version %{python3_version} .

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{pypi_name}
Summary:        Python %{python3_version} HTTP library with thread-safe connection pooling and file post
Requires:       ca-certificates
Requires:       python%{python3_other_pkgversion}-pysocks
Requires:       python%{python3_other_pkgversion}-six
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}

%description -n python%{python3_other_pkgversion}-%{pypi_name}
%_description
This package is for Python3 version %{python3_other_version} .
%endif


%prep
%setup -q -n %{pypi_name}-%{version}
# Use system six
rm %{pypi_name}/packages/six.py
find -name \*.py | xargs sed -i -e 's/from .*\.six/from six/' -e 's/from .* import six/import six/'

# Drop the dummyserver tests in koji.  They fail there in real builds, but not
# in scratch builds (weird).
rm -r test/with_dummyserver/

%build
%py3_build
%if 0%{?python3_other_pkgversion}
%py3_other_build
%endif

%install
%py3_install
ln -s ../../six.py %{buildroot}%{python3_sitelib}/%{pypi_name}/packages/six.py
%if 0%{?python3_other_pkgversion}
%py3_other_install
ln -s ../../six.py %{buildroot}%{python3_other_sitelib}/%{pypi_name}/packages/six.py
%endif

%if %{with tests}
%check
nosetests-%{python3_version}
%if 0%{?python3_other_pkgversion}
%{?with python3_other_tests: nosetests-%{python3_other_version}}
%endif
%endif


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python3_other_sitelib}/%{pypi_name}/
%{python3_other_sitelib}/%{pypi_name}-*.egg-info
%endif


%changelog
* Sun Sep 22 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.19.1-6
- Made support for tests and docs optional, support for Redhat 7 Python 3.6

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 1.19.1-5
- Rebuilt to change main python from 3.4 to 3.6

* Sat Sep 29 2018 Raphael Groner <projects.rg@smart.ms> - 1.19.1-4
- add python3_other subpackage
- add BR: python3X-setuptools
- use pypi macros

* Fri Jan 6 2017 Orion Poplawski <orion@cora.nwra.com> - 1.19.1-3
- Install symlink to system six.py

* Sun Nov 27 2016 Orion Poplawski <orion@cora.nwra.com> - 1.19.1-2
- Patch to use system six
- Do not attempt change ssl handling

* Tue Nov 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.19.1-1
- Update to 1.19.1

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 1.16-1
- Initial EPEL7 package
