%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%global with_python3 1
%bcond_with docs
%else
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif
%bcond_without docs
%endif

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           python-zope-event
Version:        4.2.0
Release:        12%{?dist}
Summary:        Zope Event Publication
Group:          Development/Languages
License:        ZPLv2.1
URL:            http://pypi.python.org/pypi/zope.event/
Source0:        http://pypi.python.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz
BuildArch:      noarch

%description
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

%package -n python2-zope-event
Summary:        Zope Event Publication (Python 2)
%{?python_provide:%python_provide python2-zope-event}

%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel
%endif
BuildRequires:  python2-setuptools

Requires:       python2

%description -n python2-zope-event
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

This package contains the version for Python 2.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-zope-event
Summary:        Zope Event Publication (Python 3)
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-zope-event}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{with docs}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

Requires:       python3

%description -n python%{python3_pkgversion}-zope-event
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

This package contains the version for Python 3.
%endif

%prep
%setup -q -n zope.event-%{version}
rm -rf %{modname}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%if %{with docs}
# build the sphinx documents
pushd docs
PYTHONPATH=../src make SPHINXBUILD=sphinx-build-3 html
rm -f _build/html/.buildinfo
popd
%endif

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-zope-event
%doc CHANGES.rst COPYRIGHT.txt README.rst
%if %{with docs}
%doc docs/_build/html/
%endif
%license LICENSE.txt
%{python2_sitelib}/zope/event/
%exclude %{python2_sitelib}/zope/event/tests.py*
%dir %{python2_sitelib}/zope/
#%{python2_sitelib}/zope/__init__*
%{python2_sitelib}/zope.event-*.egg-info
%{python2_sitelib}/zope.event-*-nspkg.pth

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-zope-event
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%if %{with docs}
%doc docs/_build/html/
%endif
%license LICENSE.txt
%{python3_sitelib}/zope/event/
%exclude %{python3_sitelib}/zope/event/tests.py*
%exclude %{python3_sitelib}/zope/event/__pycache__/tests*
%dir %{python3_sitelib}/zope/
#%{python3_sitelib}/zope/__init__*
%{python3_sitelib}/zope.event-*.egg-info
%{python3_sitelib}/zope.event-*-nspkg.pth
%endif

%changelog
* Wed Oct 10 2018 SaltStack Packaging Team <packaging@saltstack.com> - 4.2.0-12 
- Support for Python 3 on Amazon Linux 2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-10
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-9
- Build the docs with Python 3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 4.2.0-7
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 4.2.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.2.0-2
- Modernized python macros.
- Added an explicit python2 subpackage.

* Fri Feb 19 2016 Ralph Bean <rbean@redhat.com> - 4.2.0-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.5

* Mon Oct 19 2015 Ralph Bean <rbean@redhat.com> - 4.1.0-1
- new version

* Mon Oct 19 2015 Ralph Bean <rbean@redhat.com> - 4.0.3-4
- No longer own zope/__init__.py.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Ralph Bean <rbean@redhat.com> - 4.0.3-2
- Fix a python3 conditional block.

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 4.0.3-1
- Latest upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Ralph Bean <rbean@redhat.com> - 4.0.2-1
- Latest upstream.
- Conditionalized python3 subpackage for el6.

* Thu Oct 18 2012 Robin Lee <cheeselee@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2 (ZTK 1.1.5)

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 3.5.1-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep  1 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1 (#728489)
- Build subpackage for Python 3.
- Include the sphinx documents
- Exclude the module for tests.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 31 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.0.1-4
- Add a missed percent character

* Tue Aug 31 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.0.1-3
- Remove python-zope-filesystem from requirements
- Own %%{python_sitelib}/zope/
- Spec cleaned up

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 17 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.5.0.1-1
- Update to 3.5.0-1
- Include more documents

* Sun Jul 5 2009 Conrad Meyer <konrad@tylerc.org> - 3.4.1-1
- Add missing BR on python-setuptools.
- Enable testing stuff as zope-testing is in devel.

* Sun Dec 14 2008 Conrad Meyer <konrad@tylerc.org> - 3.4.0-1
- Initial package.
