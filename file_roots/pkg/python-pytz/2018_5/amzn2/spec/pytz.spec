%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%endif

Name:           pytz
Version:        2018.5
Release:        2%{?dist}
Summary:        World Timezone Definitions for Python

License:        MIT
URL:            http://pytz.sourceforge.net/
## Source0:        %%pypi_source
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
# Patch to use the system supplied zoneinfo files
Patch0:         pytz-zoneinfo.patch
# https://bugzilla.redhat.com/1497572
Patch1:         remove_tzinfo_test.patch

BuildArch:      noarch

%global _description\
pytz brings the Olson tz database into Python. This library allows accurate\
and cross platform timezone calculations using Python 2.3 or higher. It\
also solves the issue of ambiguous times at the end of daylight savings,\
which you can read more about in the Python Library Reference\
(datetime.tzinfo).\
\
Almost all (over 540) of the Olson timezones are supported.

%description %_description


%package -n python2-%{name}
Summary:        %summary
%{?python_provide:%python_provide python2-%{name}}
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel
%endif
BuildRequires:  python2-pytest
Requires:       tzdata
# Remove before F30
Provides: pytz = %{version}-%{release}
Obsoletes: pytz < %{version}-%{release}

%description -n python2-%{name} %_description


%package -n python%{python3_pkgversion}-%{name}
Summary:        %summary
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
Requires:       tzdata

%description -n python%{python3_pkgversion}-%{name} %_description


%prep
%autosetup -p1


%build
%py2_build
%py3_build


%install
%py2_install
rm -r %{buildroot}%{python2_sitelib}/pytz/zoneinfo
pathfix.py -pn -i %{__python2} %{buildroot}%{python2_sitelib}

%py3_install
rm -r %{buildroot}%{python3_sitelib}/pytz/zoneinfo
pathfix.py -pn -i %{__python3} %{buildroot}%{python3_sitelib}


%check
PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} -m pytest -v
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v


%files -n python2-%{name}
%license LICENSE.txt
%doc README.txt
%{python2_sitelib}/pytz/
%{python2_sitelib}/*.egg-info

%files -n python%{python3_pkgversion}-pytz
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/pytz/
%{python3_sitelib}/*.egg-info


%changelog
* Fri Oct 12 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.5-2
- Support for Python 3 on Amazon Linux 2

* Thu Aug 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.5-1
- Update to 2018.5 (#1508227)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.2-9
- Rebuilt for Python 3.7

* Wed May 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.2-8
- Fix ambiguous shebangs

* Sat Mar 17 2018 Matěj Cepl <mcepl@redhat.com> - 2017.2-7
- Switch __python for __python2 macro.

* Sat Mar 17 2018 Matěj Cepl <mcepl@redhat.com> - 2017.2-6
- remove test_tzinfo.PicklingTest.testRoundtrip which fails with our
  system-wide timezone database (#1497572)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 2017.2-4
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2017.2-3
- Python 2 binary package renamed to python2-pytz
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Petr Šabata <contyk@redhat.com> - 2017.2-1
- Update to 2017.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 2016.10-3
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2016.10-2
- Rebuild for Python 3.6
- Disable python3 tests for now

* Tue Dec 6 2016 Orion Poplawski <orion@cora.nwra.com> - 2016.10-1
- Update to 2016.10

* Tue Nov 8 2016 Orion Poplawski <orion@cora.nwra.com> - 2016.7-1
- Update to 2016.7

* Thu Jul 21 2016 Matěj Cepl <mcepl@redhat.com> - 2016.6.1-1
- Update to 2016.6.1 (RHBZ #1356337)
- Fix Source0 URL to override a change in PyPI URLs (see
  https://bitbucket.org/pypa/pypi/issues/438/)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2016.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Orion Poplawski <orion@cora.nwra.com> 2016.4-1
- Use proper PYTHONPATH with python3 test
- Use %%license
- Drop BuildRoot and %%clean

* Sat Apr 23 2016 Matěj Cepl <mcepl@redhat.com> 2016.4-1
- Update to 2016.4 (RHBZ #1265036)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 2015.7-2
- Rebuilt for Python3.5 rebuild

* Mon Oct 26 2015 Orion Poplawski <orion@cora.nwra.com> - 2015.7-1
- Update to 2015.7

* Sun Aug 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2015.4-1
- Update to 2015.4 (bug #1161236)
- Do not ship zoneinfo with python3 package (bug #1251554)
- Run tests

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012d-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012d-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2012d-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012d-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012d-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan  3 2013 David Malcolm <dmalcolm@redhat.com> - 2012d-3
- remove rhel logic from with_python3 conditional

* Fri Sep 14 2012 Jon Ciesla <limburgher@gmail.com> - 2012d-2
- Use system zoneinfo, BZ 857266.

* Thu Aug 23 2012 Jon Ciesla <limburgher@gmail.com> - 2012d-1
- Latest upstream, python3 support, BZ 851226.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010h-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010h-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2010h-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 28 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 2010h-2
- Define => global

* Tue Apr 27 2010 Jon Ciesla <limb@jcomserv.net> - 2010h-1
- Update to current version, BZ 573252.

* Mon Feb 01 2010 Jon Ciesla <limb@jcomserv.net> - 2009i-7
- Corrected Source0 URL, BZ 560168.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008i-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008i-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2008i-4
- Rebuild for Python 2.6

* Tue Nov 18 2008 Jef Spaleta <jspaleta at fedoraproject dot org> 2008i-3
- Apply patch correctly.

* Thu Nov 13 2008 Jef Spaleta <jspaleta at fedoraproject dot org> 2008i-2
- Updated tzdata patch from Petr Machata bug 471014

* Tue Nov 11 2008 Jef Spaleta <jspaleta at fedoraproject dot org> 2008i-1
- Update to latest, now using timezone files provided by tzdata package

* Fri Jan 04 2008 Jef Spaleta <jspaleta@gmail.com> 2006p-3
- Fix for egg-info file creation

* Mon Dec 11 2006 Jef Spaleta <jspaleta@gmail.com> 2006p-2
- Bump for rebuild against python 2.5 and change BR to python-devel accordingly

* Fri Dec  8 2006 Orion Poplawski <orion@cora.nwra.com> 2006p-1
- Update to 2006p

* Thu Sep  7 2006 Orion Poplawski <orion@cora.nwra.com> 2006g-1
- Update to 2006g

* Mon Feb 13 2006 Orion Poplawski <orion@cora.nwra.com> 2005r-2
- Rebuild for gcc/glibc changes

* Tue Jan  3 2006 Orion Poplawski <orion@cora.nwra.com> 2005r-1
- Update to 2005r

* Thu Dec 22 2005 Orion Poplawski <orion@cora.nwra.com> 2005m-1
- Update to 2005m

* Fri Jul 22 2005 Orion Poplawski <orion@cora.nwra.com> 2005i-2
- Remove -O1 from install command

* Tue Jul 05 2005 Orion Poplawski <orion@cora.nwra.com> 2005i-1
- Initial Fedora Extras package
