
%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%bcond_with python2
%bcond_without python3
%bcond_with tests
%else
%bcond_without python2
%bcond_with python3
%bcond_without tests
%endif

%{!?python3_pkgversion:%global python3_pkgversion 3}

%global srcname backports_abc
%global sum A backport of recent additions to the 'collections.abc' module

Name:           python-%{srcname}
Version:        0.5
Release:        10%{?dist}
Summary:        %{sum}

License:        Python
URL:            https://pypi.python.org/pypi/backports_abc
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?with_amzn2}
%if %{with python2}
BuildRequires:  python2-rpm-macros
%endif
%if %{with python3}
BuildRequires:  python3-rpm-macros
%endif
%endif


%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
%{sum}.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{sum}.
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{sum}.
%endif


%prep
%autosetup -n %{srcname}-%{version}


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
%{__python2} setup.py test
%endif
%if %{with python3}
%{__python3} setup.py test
%endif
%endif


%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}*.egg-info/
%{python3_sitelib}/__pycache__/*
%endif


%changelog
* Tue Jun 11 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.5-10
- Made support for Python 2 optional and Python3 default

* Thu Feb 07 2019 SaltStack Packaging Team <packaging@#saltstack.com> -0.5-9
- Support for Python 3 on Amazon Linux 2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> -0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.5-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5-1
- Update to 0.5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-3
- Use %%{python3_pkgversion}

* Tue Feb 2 2016 Orion Poplawski <orion@cora.nwra.com> - 0.4-2
- Fix python3 package file ownership

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 0.4-1
- Initial package
