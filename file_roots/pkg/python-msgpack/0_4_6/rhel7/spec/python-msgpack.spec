%global srcname msgpack

%if 0%{?fedora} || %{rhel} >= 7
%global with_python3 1
%endif

%global _description \
MessagePack is a binary-based efficient data interchange format that is \
focused on high performance. It is like JSON, but very fast and small.  \
This is a Python (de)serializer for MessagePack.

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           python-%{srcname}
Version:        0.4.6
Release:        2%{?dist}
Summary:        A Python MessagePack (de)serializer

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/msgpack-python/
Source0:        http://pypi.python.org/packages/source/m/%{srcname}-python/%{srcname}-python-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  pytest

# We don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%if 0%{?with_python3}
%filter_provides_in %{python3_sitearch}/.*\.so$
%endif
%filter_setup
}

%description %{_description}

%package -n     python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}

%if 0%{?with_python3}
%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary} 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
## %{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
%endif

%prep
%setup -q -n %{srcname}-python-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3


%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif


%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
export PYTHONPATH=$(pwd)

py.test-%{python_version} -v test

%if 0%{?with_python3}
pushd %{py3dir}
py.test-%{python3_version} -v test
popd
%endif # with_python3


%files -n python2-%{srcname}
%doc COPYING README.rst
%{python2_sitearch}/%{srcname}/
%{python2_sitearch}/%{srcname}*.egg-info

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc COPYING README.rst
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}*.egg-info
%endif

%changelog
* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.4.6-2
- Add support for Python 3

* Fri Mar 13 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.6-1
- Update to latest upstream version 0.4.6 (RHBZ #1201568)

* Fri Jan 30 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.5-2
- Correct python3 subpackage Summary

* Sun Jan 25 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.5-1
- Update to latest upstream version 0.4.5

* Fri Jan 23 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.4-2
- Patch test suite for EL6 and EL7 compatibility (RHBZ #1182808)
- Add python2 macros for EL6 compatibility (RHBZ #1182808)

* Thu Jan 15 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.4-1
- Update to latest upstream version 0.4.4 (RHBZ #1180507)
- Add tests in %%check

* Wed Sep 10 2014 Nejc Saje <nsaje@redhat.com> - 0.4.2-4
- Introduce python3- subpackage

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream version 0.4.2

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream version 0.4.1

* Tue Jan 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Update to latest upstream version 0.4.0

* Mon Jan 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.13-5
- Update spec file and python macros

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.13-1
- Update to new upstream version 0.1.13

* Tue Jan 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.12-1
- Update to new upstream version 0.1.12

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.10-1
- Updated to new upstream version 0.1.10
- README is gone

* Tue Jul 12 2011 Dan Horák <dan[at]danny.cz> - 0.1.9-3
- Fix build on big endian arches

* Fri Jun 24 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.9-2
- Tests are failing, they are not active at the moment
- Filtering added

* Sat Mar 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.9-1
- Initial package
