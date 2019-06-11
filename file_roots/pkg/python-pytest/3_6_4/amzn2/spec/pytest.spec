%global pylib_version 1.5.0

%bcond_with python2
%bcond_without python3
%bcond_with tests

%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%bcond_with timeout
%bcond_with optional_tests
%bcond_with docs
%bcond_with tests
%else
# The test in this specfile use pytest-timeout
# When building pytest for the first time with new Python version
# that is not possible as it depends on pytest
%bcond_without timeout

# When building pytest for the first time with new Python version
# we might not yet have all the BRs, this allows us to build without some that
# are likely not yet built.
# Pytest will skip the related tests, so we only conditionalize the BRs
%bcond_without optional_tests

# When building pytest for the first time with new Python version
# we also don't have sphinx yet and cannot build docs.
%bcond_without docs
%endif

Name:           pytest
Version:        3.6.4
Release:        3%{?dist}
Summary:        Simple powerful testing with Python
License:        MIT
URL:            http://pytest.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz


%if %{with docs}
BuildRequires:  %{_bindir}/sphinx-build-3
BuildRequires:  python3-sphinxcontrib-trio
BuildRequires:  %{_bindir}/rst2html
%endif

BuildArch:      noarch

%description
py.test provides simple, yet powerful testing for Python.

%if %{with python2}
%package -n python2-%{name}
Summary:        Simple powerful testing with Python
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
%endif
BuildRequires:  python2-atomicwrites
BuildRequires:  python2-attrs
BuildRequires:  python2-devel
BuildRequires:  python2-funcsigs
BuildRequires:  python2-hypothesis
BuildRequires:  python2-more-itertools >= 4.0.0
BuildRequires:  python2-pluggy
BuildRequires:  python2-py >= %{pylib_version}
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-six

%if %{with timeout}
BuildRequires:  python2-pytest-timeout
%endif

%if %{with optional_tests}
BuildRequires:  python2-decorator
BuildRequires:  python2-jinja2
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-twisted
%endif

Requires:       python2-atomicwrites
Requires:       python2-attrs
Requires:       python2-funcsigs
Requires:       python2-more-itertools >= 4.0.0
Requires:       python2-pluggy
Requires:       python2-py >= %{pylib_version}
Requires:       python2-setuptools
Requires:       python2-six
%{?python_provide:%python_provide python2-%{name}}
# the python2 package was named pytest up to 2.8.7-2
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < 2.8.7-3

%description -n python2-%{name}
py.test provides simple, yet powerful testing for Python.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{name}
Summary:        Simple powerful testing with Python
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-atomicwrites
BuildRequires:  python%{python3_pkgversion}-attrs
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hypothesis
BuildRequires:  python%{python3_pkgversion}-more-itertools
BuildRequires:  python%{python3_pkgversion}-pluggy
BuildRequires:  python%{python3_pkgversion}-py >= %{pylib_version}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-six

%if %{with timeout}
BuildRequires:  python%{python3_pkgversion}-pytest-timeout
%endif
%if %{with optional_tests}
BuildRequires:  python%{python3_pkgversion}-argcomplete
BuildRequires:  python%{python3_pkgversion}-decorator
BuildRequires:  python%{python3_pkgversion}-jinja2
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-twisted
%endif
Requires:       python%{python3_pkgversion}-atomicwrites
Requires:       python%{python3_pkgversion}-attrs
Requires:       python%{python3_pkgversion}-more-itertools
Requires:       python%{python3_pkgversion}-pluggy
Requires:       python%{python3_pkgversion}-py >= %{pylib_version}
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Obsoletes:      platform-python-%{name} < %{version}-%{release}

%description -n python3-%{name}
py.test provides simple, yet powerful testing for Python.
%endif

%prep
%autosetup

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%if %{with docs}
for l in doc/* ; do
  make -C $l html PYTHONPATH=$(pwd)/src SPHINXBUILD=%{_bindir}/sphinx-build-3
done
for f in README CHANGELOG CONTRIBUTING ; do
  rst2html ${f}.rst > ${f}.html
done
%endif

%install
%if %{with python2}
%py2_install
mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python2_version}
ln -snf pytest-%{python2_version} %{buildroot}%{_bindir}/pytest-2
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python2_version}
ln -snf py.test-%{python2_version} %{buildroot}%{_bindir}/py.test-2

# use 2.X
ln -snf pytest-%{python2_version} %{buildroot}%{_bindir}/pytest
ln -snf py.test-%{python2_version} %{buildroot}%{_bindir}/py.test
%endif

%if %{with python3}
%py3_install
mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python3_version}
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest-3
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python3_version}
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test-3

# use 3.X
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test
%endif


%if %{with docs}
mkdir -p _htmldocs/html
for l in doc/* ; do
  # remove hidden file
  rm ${l}/_build/html/.buildinfo
  mv ${l}/_build/html _htmldocs/html/${l##doc/}
done
%endif


%if %{with python2}
# remove shebangs from all scripts
find %{buildroot}%{python2_sitelib} \
     -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;
%endif
%if %{with python3}
# remove shebangs from all scripts
find %{buildroot}%{python3_sitelib} \
     -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;
%endif


%if %{with tests}
%check
%if %{with python2}
PATH=%{buildroot}%{_bindir}:${PATH} \
PYTHONPATH=%{buildroot}%{python2_sitelib} \
  %{buildroot}%{_bindir}/pytest-%{python2_version} -r s testing \
  %if %{with timeout}
  --timeout=30
  %endif
%endif

%if %{with python3}
PATH=%{buildroot}%{_bindir}:${PATH} \
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  %{buildroot}%{_bindir}/pytest-%{python3_version} -r s testing \
  %if %{with timeout}
  --timeout=30
  %endif
%endif
%endif


%if %{with python2}
%files -n python2-%{name}
%if %{with docs}
%doc CHANGELOG.html
%doc README.html
%doc CONTRIBUTING.html
%doc _htmldocs/html
%endif
%license LICENSE
%{_bindir}/pytest
%{_bindir}/pytest-2
%{_bindir}/pytest-%{python2_version}
%{_bindir}/py.test
%{_bindir}/py.test-2
%{_bindir}/py.test-%{python2_version}
%{python2_sitelib}/pytest-*.egg-info/
%{python2_sitelib}/_pytest/
%{python2_sitelib}/pytest.py*
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{name}
%if %{with docs}
%doc CHANGELOG.html
%doc README.html
%doc CONTRIBUTING.html
%doc _htmldocs/html
%endif
%license LICENSE
%{_bindir}/pytest-3
%{_bindir}/pytest-%{python3_version}
%{_bindir}/py.test-3
%{_bindir}/py.test-%{python3_version}
%{python3_sitelib}/pytest-*.egg-info/
%{python3_sitelib}/_pytest/
%{python3_sitelib}/pytest.py
%{python3_sitelib}/__pycache__/pytest.*
%endif

%changelog
* Tue Jun 11 2019 SaltStack Packaging Team <packaging@saltstack.com> - 3.6.4-3
- Made support for Python 2 optional

* Wed Oct 10 2018 SaltStack Packaging Team <packaging@#saltstack.com> - 3.6.4-2
- Support for Python 3 on Amazon Linux 2

* Sat Sep 29 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.6.4-1
- Update to 3.6.4.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.6.3-1
- Update to 3.6.3.

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.2-3
- Enable timeout

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.2-2
- Rebuilt for Python 3.7 (without timeout)

* Thu Jun 28 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.6.2-1
- Update to 3.6.2.

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.1-3
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.1-2
- Bootstrap for Python 3.7

* Tue Jun  5 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.6.1-1
- Update to 3.6.1.

* Mon May 28 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.0-1
- Update to 3.6.0 (#1581692)
- Require and BuildRequire atomicwrites

* Sat May 19 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.5.1-1
- Update to 3.5.1.
- Build the documentation with Python3.
- Update requirements.

* Thu Mar 15 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.4.2-2
- Add Requires for required modules

* Wed Mar 14 2018 Charalampos Stratakis <cstratak@redhat.com> - 3.4.2-1
- Update to 3.4.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.3-3
- Use better Obsoletes for platform-python

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.3-2
- Remove platform-python subpackage
- Cleanup conditionals

* Sat Oct  7 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.2.3-1
- Update to 3.2.3.

* Sat Sep  9 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.2.2-1
- Update to 3.2.2.
- Move BRs to their respective subpackages.
- Enable the platform-python subpackage only on F27+.

* Thu Aug 24 2017 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-3
- Rebuilt for rhbz#1484607

* Fri Aug 11 2017 Petr Viktorin <pviktori@redhat.com> - 3.2.1-2
- Add subpackage for platform-python (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Wed Aug  9 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.2.1-1
- Update to 3.2.1.

* Wed Aug 02 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.2.0-1
- 3.2.0.

* Sun Jul 30 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.1.3-1
- Update to 3.1.3.
- Update BRs.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun  3 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.1.1-1
- Update to 3.1.1.
- Add BR on setuptools_scm.

* Wed Mar 15 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.7-1
- Update to 3.0.7.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.6-1
- Update to 3.0.6.
- Drop patch applied upstream.

* Tue Dec 13 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.5-2
- Rebuild for Python 3.6

* Tue Dec  6 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.5-1
- Update to 3.0.5.

* Mon Nov 28 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.4-1
- Update to 3.0.4.

* Fri Sep 30 2016 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.3-1
- Update to 3.0.3.
- Update requirements.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.9.2-1
- Update to 2.9.2.

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Sat Apr  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.9.1-1
- Update to 2.9.1.
- Packaging updates.

* Tue Feb 2 2016 Orion Poplawski <orion@cora.nwra.com> - 2.8.7-2
- Use new python macros
- Fix python3 package file ownership

* Sun Jan 24 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.7-1
- Update to 2.8.7.

* Fri Jan 22 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.6-1
- Update to 2.8.6.

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2.8.5-1
- Update to 2.8.5

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2.8.2-3
- Re-enable pexpect in tests

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.2-1
- Update to 2.8.2.

* Mon Oct 12 2015 Robert Kuska <rkuska@redhat.com> - 2.7.3-2
- Rebuilt for Python3.5 rebuild

* Thu Sep 17 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.3-1
- Update to 2.7.3.
- Provide additional symlinks to the pytest executables (rhbz#1249891).

* Mon Sep 14 2015 Orion Poplawski <orion@cora.nwra.com> - 2.7.2-2
- Provide python2-pytest, use python_provide macro

* Thu Jun 25 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.2-1
- Update to 2.7.2.
- Small fixes.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.1-1
- Update to 2.7.1.

* Mon Apr 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.0-1
- Update to 2.7.0.
- Apply updated Python packaging guidelines.
- Mark LICENSE with %%license.

* Tue Dec  2 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.6.4-1
- Update to 2.6.4.

* Sat Oct 11 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.6.3-1
- Update to 2.6.3.

* Fri Aug  8 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.6.1-1
- Update to 2.6.1.

* Fri Aug  1 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.6.0-1
- Update to 2.6.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dennis Gilmore <dennis@ausil.us> - 2.5.2-2
- Redbuild for python 3.4

* Fri Apr 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.2-1
- Update to 2.5.2.

* Mon Oct  7 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.4.2-2
- Only run tests from the 'testing' subdir in %%check.

* Sat Oct  5 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.4.2-1
- Update to 2.4.2.
- Add buildroot's bindir to PATH while running the testsuite.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.5-3
- Disable tests using pexpect for now, fails on F19.

* Wed Jun 12 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.5-2
- Use python-sphinx for rhel > 6 (rhbz#973318).
- Update BR to use python-pexpect instead of pexpect.

* Sat May 25 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.5-1
- Update to 2.3.5.
- Docutils needed now to build README.html.
- Add some BR optionally used by the testsuite.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.4-1
- Update to 2.3.4.

* Sun Oct 28 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.2-1
- Update to 2.3.2.

* Sun Oct 21 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.1-1
- Update to 2.3.1.
- Re-enable some tests, ignore others.
- Docs are available in English and Japanese now.

* Thu Oct 11 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-4
- Add conditional for sphinx on rhel.
- Remove rhel logic from with_python3 conditional.
- Disable failing tests for Python3.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.4-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-1
- Update to 2.2.4.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.3-1
- Update to 2.2.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1.

* Tue Dec 13 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.0-1
- Update to 2.2.0.

* Wed Oct 26 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.3-1
- Update to 2.1.3.

* Tue Sep 27 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.2-1
- Update to 2.1.2.

* Sat Sep  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.1-2
- Fix: python3 dependencies.

* Sun Aug 28 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.1-1
- Update to 2.1.1.

* Thu Aug 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.0-2
- Update Requires and BuildRequires tags.

* Tue Aug  9 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.0-1
- Update to 2.1.0.

* Mon May 30 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.3-1
- Update to 2.0.3.

* Thu Mar 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.2-1
- Update to 2.0.2.

* Sun Jan 16 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.0-1
- New package.
