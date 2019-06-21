%bcond_with python2
%bcond_without python3
%bcond_with tests

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%endif

%global tarball_name apache-libcloud
%global srcname libcloud
%global eggname apache_libcloud
%global _description \
libcloud is a client library for interacting with many of \
the popular cloud server providers.  It was created to make \
it easy for developers to build products that work between \
any of the services that it supports.

# Don't duplicate the same documentation
%global _docdir_fmt %{name}

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           python-libcloud
Version:        2.2.1
Release:        10%{?dist}
Summary:        A Python library to address multiple cloud provider APIs

Group:          Development/Languages
License:        ASL 2.0
URL:            http://libcloud.apache.org/
Source0:        https://files.pythonhosted.org/packages/source/a/%{tarball_name}/%{tarball_name}-%{version}.tar.gz

BuildArch:      noarch

%description %{_description}

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel
%endif
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest-runner
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest-runner
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

Patch0: 000-async.patch

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python 3 version.
%endif

%prep
%autosetup -p1 -n %{tarball_name}-%{version}

# Delete shebang lines in the demos
sed -i '1d' demos/gce_demo.py demos/compute_demo.py

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
## %%py3_build
## amzn2 has issue with %{py_setup} expansion
CFLAGS="%{optflags}" %{__python3} setup.py %{?py_setup_args} build --executable="%{__python3} %{py3_shbang_opts}" %{?*}
sleep 1
%endif

# Fix permissions for demos
chmod -x demos/gce_demo.py demos/compute_demo.py

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
## %%py3_install
## amzn2 has issue with %{py_setup} expansion
CFLAGS="%{optflags}" %{__python3} setup.py %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?*}
%endif


# Don't package the test suite. We dont run it anyway
# because it requires some valid cloud credentials
%if %{with python2}
rm -r $RPM_BUILD_ROOT%{python2_sitelib}/%{srcname}/test

%files -n python2-%{srcname}
%doc README.rst demos/
%license LICENSE
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{eggname}-*.egg-info/
%endif

%if %{with python3}
rm -r $RPM_BUILD_ROOT%{python3_sitelib}/%{srcname}/test

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst demos/
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{eggname}-*.egg-info/
%endif

%changelog
* Mon Jun 17 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2.2.1-10
- Made support for Python 2 optional

* Wed Oct 10 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2.2.1-9
- Ported to Amazon Linux 2 for Python 3 support

* Mon Jul 16 2018 Marcel Plch <mplch@redhat.com> - 2.2.1-8
- Patch for Python 3.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-6
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> 2.2.1-5
- Rebuilt the package to enable the python3-libcloud package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 2.2.1-3
- Fix the gitignore file for the package

* Wed Nov 22 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 2.2.1-2
- Add package python-pytest-runner as BuildRequires

* Wed Oct 25 2017 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 2.2.1-1
- Apache Libcloud version 2.2.1 upgrade

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Daniel Bruno <dbruno@fedoraproject.org> - 2.0.0-1
- Apache Libcloud version 2.0.0rc2 upgrade

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuild for Python 3.6

* Wed Nov 16 2016 Dominika Krejci <dkrejci@redhat.com> - 1.3.0-2
- Add python3 subpackage
- Include the upstream demos
- Don't package the test suite

* Mon Oct 24 2016 Daniel Bruno <dbruno@fedoraproject.org> - 1.3.0-1
- Python Libcloud 1.3.0 release

* Tue Jul 12 2016 Daniel Bruno <dbruno@fedoraproject.org> - 1.1.0-1
- Python Libcloud 1.1.0 release

* Sun Jan 24 2016 Daniel Bruno <dbruno@fedoraprojec.org> - 0.20.1-1
- This is a bug-fix release of the 0.20 series.

* Thu Jan 07 2016 Daniel Bruno dbruno@fedoraproject.org - 0.20.0-1
- Release 0.20.0 with new features and improvements

* Mon Aug 10 2015 Daniel Bruno <dbruno@fedoraproject.org> - 0.18.0-1
- Apache Libcloud 0.18.0 release with bug fixes and new features

* Fri Feb 20 2015 Daniel Bruno <dbruno@fedoraproject.org> - 0.17.0-1
- Apache Libcloud 0.17.0 release

* Wed Nov 12 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.16.0-1
- First release in the 0.16 series

* Mon Jul 21 2014 Daniel Bruno <dbruno@fedoraproject.org - 0.15.1-2
- Libcloud 0.15.1 bug-fix release

* Fri Jun 27 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.15.0-1
- First release in the 0.15 series which it brings many new features,
  improvements and bug fixes

* Mon Feb 10 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.14.1-1
- Release 0.14.1 includes some bug-fixes, improvements and new features

* Fri Jan 31 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.14.0-1
- Libcloud new release 0.14.0

* Fri Jan 03 2014 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.3-1
- Security Fix - BUG: 1047867 1047868

* Thu Sep 19 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.2-11
- Some bug fixes from Upstream

* Mon Sep 09 2013 Daniel Bruno <dbruno@fedoraproject.org> - 0.13.1-10
- Update to upstream release 0.13.1

* Mon Jul 01 2013 Daniel Bruno dbruno@fedoraproject.org - 0.13.0-9
- Update to upstream release 0.13.0, more details on Release Notes.

* Thu May 16 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.4-8
- Update to upstream version 0.12.4

* Tue Mar 26 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.3-6
- Update to upstream version 0.12.3

* Tue Feb 19 2013 Daniel Bruno dbruno@fedoraproject.org - 0.12.1-5
- Update to upstream version 0.12.1

* Wed Oct 10 2012 Daniel Bruno dbruno@fedoraproject.org - 0.11.3-4
- Update to 0.11.3

* Thu Aug 02 2012 Daniel Bruno dbruno@fedoraproject.org - 0.11.1-3
- Updating to upstream release 0.11.1

* Fri Jun 15 2012 Daniel Bruno dbruno@fedoraproject.org - 0.9.1-2
- Update to upstream version 0.10.1

* Mon Apr 16 2012 Daniel Bruno dbruno@fedoraproject.org - 0.9.1-1
- update to 0.9.1

* Mon Mar 26 2012 Daniel Bruno dbruno@fedoraproject.org - 0.8.0-4
- Updating release to 0.8.0

* Fri Dec 30 2011 Daniel Bruno dbruno@fedoraproject.org - 0.6.2-3
- Standardizing the description

* Tue Nov 22 2011 Daniel Bruno dbruno@fedoraproject.org - 0.6.2-2
- First build package build

