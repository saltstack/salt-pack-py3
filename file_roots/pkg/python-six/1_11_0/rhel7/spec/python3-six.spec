Name:           python3-six
Version:        1.11.0
Release:        3%{?dist}
Summary:        Python 2 and 3 compatibility utilities

License:        MIT
URL:            https://pypi.python.org/pypi/six/
Source0:        https://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz

BuildArch:      noarch

%bcond_without python3_other

%description
python3-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

%package -n python%{python3_pkgversion}-six
Summary:        Python 2 and 3 compatibility utilities
BuildRequires:  python%{python3_pkgversion}-devel
# For use by selftests:
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-tkinter

%description -n python%{python3_pkgversion}-six
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python %{python3_pkgversion} build of the module.


%if %{with python3_other}
%package -n python%{python3_other_pkgversion}-six
Summary:        Python 2 and 3 compatibility utilities
BuildRequires:  python%{python3_other_pkgversion}-devel
# For use by selftests:
BuildRequires:  python%{python3_other_pkgversion}-pytest
BuildRequires:  python%{python3_other_pkgversion}-tkinter

%description -n python%{python3_other_pkgversion}-six
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python %{python3_other_pkgversion} build of the module.
%endif # with python3_other


%prep
%setup -q -n six-%{version}


%build
%py3_build
%if %{with python3_other}
%py3_other_build
%endif


%install
%py3_install
%if %{with python3_other}
%py3_other_install
%endif

%check
%{__python3} -m pytest -rfsxX test_six.py
%if %{with python3_other}
%{__python3_other} -m pytest -rfsxX test_six.py
%endif


%files -n python%{python3_pkgversion}-six
%license LICENSE
%doc CHANGES README.rst documentation/index.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/six*

%if %{with python3_other}
%files -n python%{python3_other_pkgversion}-six
%license LICENSE
%doc CHANGES README.rst documentation/index.rst
%{python3_other_sitelib}/__pycache__/*
%{python3_other_sitelib}/six*
%endif


%changelog
* Wed Mar 13 2019 Orion Poplawski <orion@nwra.com> - 1.11.0-3
- Enable python3_other tests, resolve egg-info issue (bug #1688502)

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 1.11.0-2
- Rebuilt to change main python from 3.4 to 3.6

* Fri Sep 28 2018 Orion Poplawski <orion@nwra.com> - 1.11.0-1
- Update to 1.11.0

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Add python3_other subpackage

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 1.10.0-1
- Initial EPEL7 package
