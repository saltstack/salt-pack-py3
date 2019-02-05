%if !(0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%global with_python3 1

%global _description \
CherryPy allows developers to build web applications in much the same way \
they would build any other object-oriented Python program. This usually \
results in smaller source code developed in less time.

%global srcname cherrypy

%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%endif

Name:           python-cherrypy
Version:        5.6.0
Release:        5%{?dist}
Summary:        Pythonic, object-oriented web development framework
Group:          Development/Libraries
License:        BSD
URL:            http://www.cherrypy.org/
Source0:        http://download.cherrypy.org/cherrypy/%{version}/CherryPy-%{version}.tar.gz
# Don't ship the tests or tutorials in the python module directroy,
# tutorial will be shipped as doc instead
Patch0:         python-cherrypy-tutorial-doc.patch
Patch1:         python-cherrypy-expose.patch
Patch2:         python-cherrypy-py34.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose


%description %{_description}

%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
%endif

%description -n python2-%{srcname} %{_description}
Python 2 version.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-nose
##%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides: python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python 3 version.
%endif


%prep
%setup -q -n CherryPy-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

## %%{__sed} -i 's/\r//' README.txt cherrypy/tutorial/README.txt cherrypy/tutorial/tutorial.conf
%{__sed} -i 's/\r//' cherrypy/tutorial/README.txt cherrypy/tutorial/tutorial.conf


%build
## %%{__python} setup.py build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif


%install
## rm -rf $RPM_BUILD_ROOT
## %%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
%py2_install
%if 0%{?with_python3}
%py3_install
%endif


%check
cd cherrypy/test
# These two tests hang in the buildsystem so we have to disable them.
# The third fails in cherrypy 3.2.2.
PYTHONPATH='../../' nosetests -s ./ -e 'test_SIGTERM' -e \
  'test_SIGHUP_tty' -e 'test_file_stream'


%clean
rm -rf $RPM_BUILD_ROOT


%files -n python2-%{srcname}
%defattr(-,root,root,-)
## %doc README.txt
%doc cherrypy/tutorial
%{_bindir}/cherryd
%{python2_sitelib}/*


%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
## %doc README.txt
%doc cherrypy/tutorial
%{_bindir}/cherryd
%{python3_sitelib}/*
%endif


%changelog
* Wed Oct 03 2018 SaltStack Packaging Team <packaging@saltstack.com> - 5.6.0-5
- Ported to Amazon Linux 2 for Python 3 support

* Thu Feb 08 2018 SaltStack Packaging Team <packaging@saltstack.com> - 5.6.0-4
- Adjusted support for Python 3

* Thu Jan 11 2018 SaltStack Packaging Team <packaging@saltstack.com> - 5.6.0-3
- Support for Python 3 on RHEL

* Tue Oct 10 2017 SaltStack Packaging Team <packaging@saltstack.com> - 5.6.0-2
- Apply patch from upstream https://github.com/cherrypy/cherrypy/commit/f3c0165a372375d4ce49f70c6b00e1788db845a1

* Mon Apr 17 2017 SaltStack Packaging Team <packaging@saltstack.com> - 5.6.0-1
- Update to 5.6.0

* Mon Apr 17 2017 SaltStack Packaging Team <packaging@saltstack.com> - 3.8.2-1
- Update to 3.8.2

* Wed Aug 27 2014 Luke Macken <lmacken@redhat.com> - 3.5.0-1
- Update to 3.5.0 (#1104560)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Conrad Meyer <konrad@tylerc.org> - 3.2.2-1
- Update to 3.2.2

* Sat Jul 16 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-4
- Fix a failing unittest with newer python

* Sat Apr 24 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-3
- Revert a try at 3.2.x-rc1 as the tests won't pass without some work.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-1
- New upstream with python-2.6 fixes.
- BR tidy for tests.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 1 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1
- Fix python-2.6 build errors
- Make test code non-interactive via cmdline switch
- Refresh the no test and tutorial patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.3-3
- Rebuild for Python 2.6

* Tue Jan 22 2008 Toshio Kuratomi <toshio@fedoraproject.org> 3.0.3-2
- Forgot to upload the tarball.

* Mon Jan 21 2008 Toshio Kuratomi <toshio@fedoraproject.org> 3.0.3-1
- Upgrade to 3.0.3.

* Thu Jan 17 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.3.0-2
- EINTR Patch needed to be forwarded ported as well as it is only applied to
  CP trunk (3.x).

* Thu Jan 17 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.3.0-1
- Update to new upstream which rolls in the backported security fix.
- Refresh other patches to apply against new version.
- Change to new canonical source URL.
- Reenable tests.

* Sun Jan  6 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.2.1-8
- Fix a security bug with a backport of http://www.cherrypy.org/changeset/1775
- Include the egginfo files as well as the python files.

* Sat Nov  3 2007 Luke Macken <lmacken@redhat.com> 2.2.1-7
- Apply backported fix from http://www.cherrypy.org/changeset/1766
  to improve CherryPy's SIGSTOP/SIGCONT handling (Bug #364911).
  Thanks to Nils Philippsen for the patch.

* Mon Feb 19 2007 Luke Macken <lmacken@redhat.com> 2.2.1-6
- Disable regression tests until we can figure out why they
  are dying in mock.

* Sun Dec 10 2006 Luke Macken <lmacken@redhat.com> 2.2.1-5
- Add python-devel to BuildRequires

* Sun Dec 10 2006 Luke Macken <lmacken@redhat.com> 2.2.1-4
- Rebuild for python 2.5

* Mon Sep 18 2006 Luke Macken <lmacken@redhat.com> 2.2.1-3
- Rebuild for FC6
- Include pyo files instead of ghosting them

* Thu Jul 13 2006 Luke Macken <lmacken@redhat.com> 2.2.1-2
- Rebuild

* Thu Jul 13 2006 Luke Macken <lmacken@redhat.com> 2.2.1-1
- Update to 2.2.1
- Remove unnecessary python-abi requirement

* Sat Apr 22 2006 Gijs Hollestelle <gijs@gewis.nl> 2.2.0-1
- Update to 2.2.0

* Wed Feb 22 2006 Gijs Hollestelle <gijs@gewis.nl> 2.1.1-1
- Update to 2.1.1 (Security fix)

* Tue Nov  1 2005 Gijs Hollestelle <gijs@gewis.nl> 2.1.0-1
- Updated to 2.1.0

* Sat May 14 2005 Gijs Hollestelle <gijs@gewis.nl> 2.0.0-2
- Added dist tag

* Sun May  8 2005 Gijs Hollestelle <gijs@gewis.nl> 2.0.0-1
- Updated to 2.0.0 final
- Updated python-cherrypy-tutorial-doc.patch to match new version

* Wed Apr  6 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.0-0.2.b
- Removed CFLAGS

* Wed Mar 23 2005 Gijs Hollestelle <gijs[AT]gewis.nl> 2.0.0-0.1.b
- Initial Fedora Package
