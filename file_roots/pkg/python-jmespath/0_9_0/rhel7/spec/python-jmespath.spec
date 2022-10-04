%if 0%{?rhel}
%global with_python3 1
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?py2_build: %global py2_build %{expand: CFLAGS="%{optflags}" %{__python2} setup.py %{?py_setup_args} build --executable="%{__python2} -s"}}
%{!?py2_install: %global py2_install %{expand: CFLAGS="%{optflags}" %{__python2} setup.py %{?py_setup_args} install -O1 --skip-build --root %{buildroot}}}
%else
%global with_python3 1
%endif

%global pypi_name jmespath

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        4%{?dist}
Summary:        JSON Matching Expressions

License:        MIT
URL:            https://github.com/jmespath/jmespath.py
Source0:        https://pypi.python.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # with_python3

%description
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.

%package -n     python2-%{pypi_name}
Summary:        JSON Matching Expressions
Provides:       python-%{pypi_name} = %{version}-%{release}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        JSON Matching Expressions
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.
%endif # with_python3

%prep
%setup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3

%install
%if 0%{?with_python3}
%py3_install
cp %{buildroot}/%{_bindir}/jp.py %{buildroot}/%{_bindir}/jp.py-3
ln -sf %{_bindir}/jp.py-3 %{buildroot}/%{_bindir}/jp.py-%{python3_version}
%endif # with_python3

%py2_install
cp %{buildroot}/%{_bindir}/jp.py %{buildroot}/%{_bindir}/jp.py-2
ln -sf %{_bindir}/jp.py-2 %{buildroot}/%{_bindir}/jp.py-%{python2_version}


%files -n python2-%{pypi_name}
%{!?_licensedir:%global license %doc}
%doc README.rst
%license LICENSE.txt
%{_bindir}/jp.py
%{_bindir}/jp.py-2
%{_bindir}/jp.py-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{_bindir}/jp.py-3
%{_bindir}/jp.py-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3

%changelog
* Fri Sep 30 2022 SaltStack Packaging Team >packaging@saltstack.com> 0.9.0-4
- Re-enable Python 3 for RHEL builds

* Mon Sep 11 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.9.0-3
- Rebuilt for RHEL 7 Extras

* Tue Dec 29 2015 Fabio Alessandro Locati <fabio@locati.cc> - 0.9.0-1
- Upgrade to upstream current version
- Improve the spec file
- Make possible to build in EL6

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.5.0-1
- New version

* Fri Jul 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-2
- Add Python 3 support

* Fri Jul 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-1
- Initial packaging
