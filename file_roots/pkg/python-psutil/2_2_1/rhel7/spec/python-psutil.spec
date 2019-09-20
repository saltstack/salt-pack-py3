%bcond_with python2
%bcond_without python3
%bcond_with tests

%global short_name psutil

%{!?python3_pkgversion:%global python3_pkgversion 3}

%global _description    \
psutil is a module providing an interface for retrieving information on all \
running processes and system utilization (CPU, memory, disks, network, users) in    \
a portable way by using Python, implementing many functionalities offered by    \
command line tools such as: ps, top, df, kill, free, lsof, free, netstat,   \
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.


# Filter Python modules from Provides
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

Name:           python-%{short_name}
Version:        2.2.1
Release:        3%{?dist}
Summary:        A process and system utilities module for Python

Group:          Development/Languages
License:        BSD
URL:            http://psutil.googlecode.com/
Source0:        https://pypi.python.org/packages/source/p/%{short_name}/%{short_name}-%{version}.tar.gz

%description    %{_description}


%if %{with python2}
%package    -n  python2-psutil
Summary:        %{summary}
Group:          %{group}
BuildRequires:  python2-devel
%{?python_provide:%python_provide python-%{short_name}}
%{?python_provide:%python_provide python2-%{short_name}}

%description -n python2-psutil %{_description}
Supports Python 2.
%endif


%if %{with python3}
%package    -n  python%{python3_pkgversion}-psutil
Summary:        %{summary}
Group:          %{group}
BuildRequires:  python%{python3_pkgversion}-devel
%{?python_provide:%python_provide python%{python3_pkgversion}-%{short_name}}

%description -n python%{python3_pkgversion}-psutil %{_description}
Supports Python 3.
%endif


%prep
%autosetup -n %{short_name}-%{version}

# Remove shebangs
for file in psutil/*.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%if %{with python2}
CFLAGS=$RPM_OPT_FLAGS %py2_build
%endif
%if %{with python3}
CFLAGS=$RPM_OPT_FLAGS %py3_build
%endif


%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif


%if %{with python2}
%files -n python2-psutil
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst TODO
%{python_sitearch}/%{short_name}/
%{python_sitearch}/*.egg-info
%{python_sitearch}/*.so
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-psutil
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst TODO
%{python3_sitearch}/%{short_name}/
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/*.so
%endif


%changelog
* Fri Sep 20 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2.2.1-3
- Made support for Python 2 optional

* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2.2.1-2
- Add support for Python 3

* Wed Dec 09 2015 Ralph Bean <rbean@redhat.com> - 2.2.1-1
- Update to 2.2.1 for https://bugzilla.redhat.com/1288221
- Update names of %%doc files.

* Wed Mar 11 2015 Alan Pevec <apevec@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Tue Feb 18 2014 Matthias Runge <mrunge@redhat.com> - 0.6.1-3
- epel doesn't have python3


* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 0.6.1-1
- Update to 0.6.1

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.5.1-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sun Nov 20 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Mon Jul 18 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Wed Mar 23 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1
- Spec cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.3-5
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.3-4
- bump, because previous build nvr already existed in F-14

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.3-2
- Add missing popd in %%build

* Sat Mar 27 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.3-1
- Update to 0.1.3
- Remove useless call to 2to3 and corresponding BuildRequires
  python2-tools (this version supports Python 3)

* Sat Feb 20 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-4
- Change python-utils BuildRequires for python2-utils

* Sat Feb 20 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-3
- Add python3 subpackage

* Thu Jan 14 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-2
- Drop no-shebang patch for a sed command
- Drop test suite from %%doc tag

* Fri Jan  8 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-1
- Initial RPM release
