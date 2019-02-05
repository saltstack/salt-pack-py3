%{!?python3_pkgversion:%global python3_pkgversion 3}
%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%bcond_without python2
%bcond_without python3
%else
%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif
%endif

%global modname freezegun
%global sum Let your Python tests travel through time

Name:               python-freezegun
Version:            0.3.8
Release:            12%{?dist}
Summary:            %{sum}

Group:              Development/Libraries
License:            ASL 2.0
URL:                https://pypi.io/project/freezegun
Source0:            https://pypi.io/packages/source/f/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

%description
freezegun is a library that allows your python tests to travel through time by
mocking the datetime module.

%if %{with python2}
%package -n python2-freezegun
Summary:            %{sum}

%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
BuildRequires:      python-devel
%else
BuildRequires:      python2-devel
%endif
BuildRequires:      python2-setuptools
BuildRequires:      python2-six
BuildRequires:      python2-dateutil
BuildRequires:      python2-sure
BuildRequires:      python2-nose
BuildRequires:      python2-coverage
BuildRequires:      python2-mock

%{?python_provide:%python_provide python2-freezegun}

Requires:           python2-six
Requires:           python2-dateutil

%description -n python2-freezegun
freezegun is a library that allows your python tests to travel through time by
mocking the datetime module. This is the Python 2 library.
%endif # with python2

%if %{with python3}
%package -n python%{python3_pkgversion}-freezegun
Summary:            %{sum}

%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-dateutil
BuildRequires:      python%{python3_pkgversion}-sure
BuildRequires:      python%{python3_pkgversion}-nose
BuildRequires:      python%{python3_pkgversion}-coverage
BuildRequires:      python%{python3_pkgversion}-mock

%{?python_provide:%python_provide python%{python3_pkgversion}-freezegun}

Requires:           python%{python3_pkgversion}-six
Requires:           python%{python3_pkgversion}-dateutil

%description -n python%{python3_pkgversion}-freezegun
freezegun is a library that allows your python tests to travel through time by
mocking the datetime module. This is the Python 3 library.
%endif # with python3

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info
%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with python3

%build
%if %{with python2}
%py2_build
%endif # with python2
%if %{with python3}
pushd %{py3dir}
%py3_build
popd
%endif # with python3

%install
%if %{with python3}
pushd %{py3dir}
%py3_install
popd
%endif # with python3
%if %{with python2}
%py2_install
%endif # with python2

%check
%if %{with python3}
pushd %{py3dir}
nosetests-%{python3_version} tests/
popd
%endif # with python3

%if %{with python2}
nosetests-%{python2_version} tests/
%endif # with python2

%if %{with python2}
%files -n python2-freezegun
%doc README.rst LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}*
%endif # with python2

%if %{with python3}
%files -n python%{python3_pkgversion}-freezegun
%doc README.rst LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%endif # with python3

%changelog
* Fri Oct 12 2018 SaltStack Packaging Team <packaging@saltstack.com> - 0.3.8-12
- Support for Python 3 on Amazon Linux 2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-10
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.3.8-9
- Conditionalize the Python 2 subpackage and don't build it on EL > 7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.8-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 0.3.8-4
- REALLY rename Python 2 package to python2-freezegun

* Wed Dec 21 2016 Adam Williamson <awilliam@redhat.com> - 0.3.8-3
- Rebuild with Python 3.6 again (now python-sure is built)
- rename Python 2 package to python2-freezegun

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-2
- Rebuild for Python 3.6

* Tue Nov 08 2016 Ralph Bean <rbean@redhat.com> - 0.3.8-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 20 2016 Kevin Fenzi <kevin@scrye.com> - 0.3.6-1
- Update to 0.3.6. Fixes bug #1328934

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 0.3.2-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Adam Williamson <awilliam@redhat.com> - 0.3.2-1
- latest upstream release

* Thu Jan 22 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.12-4
- Adjust tests to actually do something

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 0.1.12-1
- initial package for Fedora
