# spec file for package python-more-itertools
# https://fedoraproject.org/wiki/Packaging:Python#Example_common_spec
%global srcname more-itertools
%global _description \
Opensource python library wrapping around itertools. Package also includes \
implementations of the recipes from the itertools documentation.\
\
See https://pythonhosted.org/more-itertools/index.html for documentation.\
%global sum Python library for efficient use of itertools utility

%bcond_with python2
%bcond_without python3
%bcond_without tests

%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%endif

Name:           python-%{srcname}
Version:        4.1.0
Release:        6%{?dist}
Summary:        %{sum}
License:        MIT
URL:            https://github.com/erikrose/more-itertools
Source0:        https://pypi.io/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

# https://github.com/erikrose/more-itertools/commit/e38574428c952b143fc4e0e42cb99b242c7b7977
Patch0:         python37.patch

%description %_description

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{sum}
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel
%endif
BuildRequires:  python2-nose
BuildRequires:  python2-six
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %_description
Support Python 2 version.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description
Support Python 3 version.
%endif

%prep
%autosetup -n %{srcname}-%{version} -p1

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

%if %{with tests}
%check
%if %{with python2}
%{__python2} ./setup.py test
%endif
%if %{with python3}
%{__python3} ./setup.py test
%endif

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python2_sitelib}/more_itertools/
%exclude %{python2_sitelib}/more_itertools/tests
%{python2_sitelib}/more_itertools-%{version}-py%{python2_version}.egg-info
%endif

%if %{with python2}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python3_sitelib}/more_itertools/
%exclude %{python3_sitelib}/more_itertools/tests
%{python3_sitelib}/more_itertools-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Tue Jun 11 2019 SaltStack Packaging Team <packaging@saltstack.com> - 4.1.0-6
- Made support for Python 2 optional

* Wed Oct 10 2018 SaltStack Packaging Team <packaging@saltstack.com> - 4.1.0-5
- Support for Python 3 on Amazon Linux 2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.7

* Tue May 22 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Backport upstream fix for Python 3.7

* Sat Mar 24 2018 Thomas Moschny <thomas.moschny@gmx.de> - 4.1.0-1
- Update to 4.1.0.
- Do not package tests.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 aarem AT fedoraproject DOT org - 2.3-1
- update to 2.3
* Fri Oct 14 2016 aarem AT fedoraproject DOT org - 2.2-4
- fixed missing sum in line 9 of spec file, per BZ #138195
* Sat Oct 8 2016 aarem AT fedoraproject DOT org - 2.2-3
- renamed spec file to match package as per BZ #1381029
-fixed bug (incorrect python3_provides) as per BZ #1381029
- use common macro for description as per suggestion in BZ #1381029

* Wed Oct 05 2016 aarem AT fedoraproject DOT org - 2.2-2
- separated python and python3 cases as per BZ #1381029

* Sun Oct 02 2016 aarem AT fedoraproject DOT org - 2.2-1
- initial packaging of 2.2 version
