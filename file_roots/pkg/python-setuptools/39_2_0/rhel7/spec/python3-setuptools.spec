# This package is for EPEL only
# Dependencies for check and wheel introduce circular dependencies
# Set this to 0 after we've bootstrapped.
%{!?_with_bootstrap: %global bootstrap 1}

%if ! 0%{?bootstrap}
%global with_check 1
%global build_wheel 1
%else
%global with_check 0
%global build_wheel 0
%endif

## %%bcond_without python3_other

%global srcname setuptools
%if 0%{?build_wheel}
%global python3_wheelname %{srcname}-%{version}-py2.py3-none-any.whl
%global python3_record %{python3_sitelib}/%{srcname}-%{version}.dist-info/RECORD
%if %{with python3_other}
%global python3_other_record %{python3_other_sitelib}/%{srcname}-%{version}.dist-info/RECORD
%endif
%endif

%if %{with python3_other} && (0%{?build_wheel} || 0%{?with_check})
  %{error:Not supported}
%endif

# SaltStack 
%global python3_pkgversion 36
%global with_check 0
%global build_wheel 0
%bcond_with python3_other


Name:           python3-setuptools
Version:        39.2.0
Release:        4%{?dist}
Summary:        Easily build and distribute Python 3 packages
License:        MIT
URL:            https://github.com/pypa/setuptools
Source0:        http://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.zip
## Source0:        %%pypi_source %%{srcname} %%{version} zip

# In Fedora, sudo setup.py install installs to /usr/local/lib/pythonX.Y/site-packages
# But pythonX doesn't own that dir, that would be against FHS
# We need to create it if it doesn't exist
# https://bugzilla.redhat.com/show_bug.cgi?id=1576924
Patch0:         create-site-packages.patch

BuildArch:      noarch

%description
Setuptools is a collection of enhancements to the Python 3 distutils that allow
you to more easily build and distribute Python 3 packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.


%package -n python%{python3_pkgversion}-setuptools
Summary:        Easily build and distribute Python %{python3_pkgversion} packages
Group:          Applications/System
BuildRequires:  python%{python3_pkgversion}-devel
%if 0%{?with_check}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-mock
%endif # with_check
%if 0%{?build_wheel}
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
%endif # build_wheel
%{?python_provide:%python_provide python%{python3_pkgversion}-setuptools}

%description -n python%{python3_pkgversion}-setuptools
Setuptools is a collection of enhancements to the Python %{python3_pkgversion} distutils that allow
you to more easily build and distribute Python %{python3_pkgversion} packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.


%if %{with python3_other}
%package -n python%{python3_other_pkgversion}-setuptools
Summary:        Easily build and distribute Python %{python3_other_pkgversion} packages
Group:          Applications/System
BuildRequires:  python%{python3_other_pkgversion}-devel
%{?python_provide:%%python_provide python%{python3_other_pkgversion}-setuptools}

%description -n python%{python3_other_pkgversion}-setuptools
Setuptools is a collection of enhancements to the Python %{python3_other_pkgversion} distutils that allow
you to more easily build and distribute Python %{python3_other_pkgversion} packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}

# We can't remove .egg-info (but it doesn't matter, since it'll be rebuilt):
#  The problem is that to properly execute setuptools' setup.py,
#   it is needed for setuptools to be loaded as a Distribution
#   (with egg-info or .dist-info dir), it's not sufficient
#   to just have them on PYTHONPATH
#  Running "setup.py install" without having setuptools installed
#   as a distribution gives warnings such as
#    ... distutils/dist.py:267: UserWarning: Unknown distribution option: 'entry_points'
#   and doesn't create "easy_install" and .egg-info directory
# Note: this is only a problem if bootstrapping wheel or building on RHEL,
#  otherwise setuptools are installed as dependency into buildroot

# Strip shbang
find setuptools -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f setuptools/*.exe
# These tests require internet connection
rm setuptools/tests/test_integration.py


%build
%if 0%{?build_wheel}
%py3_build_wheel
%else
%py3_build
%endif

%if %{with python3_other}
%if 0%{?build_wheel}
%py3_other_build_wheel
%else
%py3_other_build
%endif
%endif


%install
%if 0%{?build_wheel}
%py3_install_wheel %{python3_wheelname}
sed -i '/\/usr\/bin\/easy_install,/d' %{buildroot}%{python3_record}
%else
%py3_install
%endif
rm -rf %{buildroot}%{python3_sitelib}/setuptools/tests

%if %{with python3_other}
%if 0%{?build_wheel}
%py3_other_install_wheel %{python3_wheelname}
sed -i '/\/usr\/bin\/easy_install,/d' %{buildroot}%{python3_other_record}
%else
%py3_other_install
%endif
rm -rf %{buildroot}%{python3_other_sitelib}/setuptools/tests
%endif

rm %{buildroot}%{_bindir}/easy_install

%if 0%{?build_wheel}
sed -i '/^setuptools\/tests\//d' %{buildroot}%{python3_record}
%endif

find %{buildroot}%{python3_sitelib} -type f -name '*.exe' -print -delete
%if %{with python3_other}
find %{buildroot}%{python3_other_sitelib} -type f -name '*.exe' -print -delete
%endif

# Don't ship these
rm -r docs/{Makefile,conf.py,_*}


%if 0%{?with_check}
%check
LANG=en_US.utf8 PYTHONPATH=$(pwd) py.test-%{python3_version}
%endif


%files -n python%{python3_pkgversion}-setuptools
%license LICENSE
%doc docs/* CHANGES.rst README.rst
%{python3_sitelib}/easy_install.py
%{python3_sitelib}/__pycache__/easy_install.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/pkg_resources
%{python3_sitelib}/setuptools
%{python3_sitelib}/setuptools-%{version}-py%{python3_version}.egg-info
%{_bindir}/easy_install-%{python3_version}


%if %{with python3_other}
%files -n python%{python3_other_pkgversion}-setuptools
%license LICENSE
%doc docs/* CHANGES.rst README.rst
%{python3_other_sitelib}/easy_install.py
%{python3_other_sitelib}/__pycache__/easy_install.cpython-%{python3_other_version_nodots}*.py*
%{python3_other_sitelib}/pkg_resources
%{python3_other_sitelib}/setuptools
%{python3_other_sitelib}/setuptools-%{version}-py%{python3_other_version}.egg-info
%{_bindir}/easy_install-%{python3_other_version}
%endif


%changelog
* Sun Sep 22 2019 SaltStack Packaging Team >packaging@saltstack.com> - 39.2.0-3
- Adjusted to build support for Redhat 7 Python 3.6 without EPEL

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com>
- Rebuilt to change main python from 3.4 to 3.6

* Fri Jan 11 2019 Miro Hrončok <mhroncok@redhat.com> - 39.2.0-2
- Create /usr/local/lib/pythonX.Y when needed (#1664722)

* Tue Dec 04 2018 Carl George <carl@george.computer> - 39.2.0-1
- Update to upstream 39.2.0

* Wed May 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 19.6.2-3
- Build for python3_other

* Sun Oct 09 2016 Tim Orling <ticotimo@gmail.com> - 19.6.2-2
- Fixes for EPEL6 build

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 19.6.2-1
- Update to 19.6.2
- Update license
- Fix python3 package file ownership

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 19.2-3
- Cleanup docs
- Add version info to summary and description

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 19.2-2
- Drop group tag
- Add bootstrap conditional
- Use specific pip version
- Use %%license
- Update license and license source
- Strip unneeded shbangs

* Tue Dec 29 2015 Orion Poplawski <orion@cora.nwra.com> - 19.2-1
- Update to 19.2

* Tue Dec 29 2015 Orion Poplawski <orion@cora.nwra.com> - 19.1.1-1
- Initial EPEL package
