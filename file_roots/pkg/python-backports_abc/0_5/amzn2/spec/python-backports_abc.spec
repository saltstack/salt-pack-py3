%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_python3 1
%global with_amzn2 1
%endif

%global srcname backports_abc
%global sum A backport of recent additions to the 'collections.abc' module

Name:           python-%{srcname}
Version:        0.5
Release:        9%{?dist}
Summary:        %{sum}

License:        Python
URL:            https://pypi.python.org/pypi/backports_abc
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
%if 0%{?with_python3}
BuildRequires:  python3-rpm-macros
%endif
%endif


BuildRequires:  python2-devel python%{python3_pkgversion}-devel
BuildRequires:  python2-setuptools python%{python3_pkgversion}-setuptools

%description
%{sum}.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{sum}.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{sum}.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
%{__python2} setup.py test
%{__python3} setup.py test


%files -n python2-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}*.egg-info/
%{python3_sitelib}/__pycache__/*


%changelog
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
