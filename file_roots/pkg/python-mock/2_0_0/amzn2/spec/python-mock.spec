%bcond_with python2
%bcond_without python3
%bcond_with tests

# Not yet in Fedora buildroot
%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%endif

%global mod_name mock

Name:           python-mock
Version:        2.0.0
Release:        14%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        http://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

%if %{with python2}
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
%endif
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-funcsigs
BuildRequires:  python2-pbr
# For tests
%if %{with tests}
BuildRequires:  python2-unittest2
%endif
%endif

%if %{with python3}
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3-pbr
# For tests
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-unittest2
%endif
%endif


%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%if %{with python2}
%package -n python2-mock
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python2-%{mod_name}}
Requires:    python2-funcsigs
Requires:    python2-pbr
Requires:    python2-six >= 1.9.0

%description -n python2-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-mock
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}
Requires:    python3-pbr
Requires:    python3-six >= 1.9.0

%description -n python%{python3_pkgversion}-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.
Supports Python %{python3_version}.
%endif


%prep
%setup -q -n %{mod_name}-%{version}


%build
%if %{with python2}
%{py2_build}
%endif
%if %{with python3}
%{py3_build}
%endif


%if %{with tests}
%check
%if %{with python2}
%{__python2} setup.py test
%endif
%if %{with python3}
%{__python3} -m unittest2 discover
%endif
%endif

%install
%if %{with python3}
%{py3_install}
%endif
%if %{with python2}
%{py2_install}
%endif


%if %{with python2}
%files -n python2-mock
%license LICENSE.txt
%doc docs/*
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%{mod_name}
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-mock
%license LICENSE.txt
%doc docs/*
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{mod_name}
%endif


%changelog
* Mon Jun 17 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2.0.0-15
- Added support for Amazon Linux 2 Python 3

* Thu May 09 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2.0.0-14
- Added support for Redhat 8, and support for Python 2 packages optional

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Petr Viktorin <pviktori@redhat.com> - 2.0.0-12
- Run tests for Python 3

* Fri Aug 17 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-11
- Don't require funcsigs on python3, it's part of the standard library

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Troy Dawson <tdawson@redhat.com> - 2.0.0-6
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 14 2016 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 2.0.0-1
- Upstream 2.0.0 (RHBZ#1244145)

* Fri Feb 26 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.0-1
- Upstream 1.3.0 (RHBZ#1244145)
- Use epel macros rather than rhel

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-9
- Modernize spec
- Run python2 tests, python3 failing

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 02 2015 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-7
- Fix #1276771

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 1.0.1-6
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dennis Gilmore <dennis@ausil.us> - 1.0.1-3
- rebuild for python 3.4
- disable test suite deps missing

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Run the test suite
- Add python-unittest2 as a build requirement

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.8.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.8.0-2
- Python3 support

* Thu Mar 22 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8.0-1
- Updated to new version

* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.2-1
- Initial RPM release
