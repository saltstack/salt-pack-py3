%if 0%{?rhel} && 0%{?rhel} < 6
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

%global with_python3 1

%global srcname             simplejson

%global _description    \
simplejson is a simple, fast, complete, correct and extensible JSON \
<http://json.org> encoder and decoder for Python 2.5+. It is pure Python code   \
with no dependencies, but includes an optional C extension for a serious speed  \
boost.  \
\
The encoder may be subclassed to provide serialization in any kind of   \
situation, without any special support by the objects to be serialized  \
(somewhat like pickle). \
\
The decoder can handle incoming JSON strings of any specified encoding (UTF-8   \
by default).    \
\
simplejson is the externally maintained development version of the json library \
included with Python 2.6 and Python 3.0, but maintains backwards compatibility  \
with Python 2.5.  It gets updated more regularly than the json module in the    \
python stdlib.                                                              

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           python-simplejson
Version:        3.3.3
Release:        2%{?dist}
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

Group:          System Environment/Libraries
# The main code is licensed MIT.
# The docs include jquery which is licensed MIT or GPLv2
License: (MIT or AFL) and (MIT or GPLv2)
URL:            http://undefined.org/python/#simplejson
Source0:        http://pypi.python.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires: python-sphinx

%if 0%{?with_python3}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-nose
%endif # with_python3

# we don't want to provide private python extension libs
%global __provides_exclude_from ^(%{python_sitearch}|%{python3_sitearch}).*\\.so$


%description    %{_description}

%package    -n  python2-simplejson
Summary:        Simple, fast, extensible JSON encoder/decoder for Python2
Group:          %{group}
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-simplejson %{_description}
Supports Python 2.


%if 0%{?with_python3}
%package    -n  python%{python3_pkgversion}-simplejson
Summary:        Simple, fast, extensible JSON encoder/decoder for Python3
Group:          %{group}
##%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-simplejson %{_description}
Supports Python 3.
%endif # with_python3

%prep
%setup -q -n simplejson-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%{__python} setup.py build
./scripts/make_docs.py

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot}

rm docs/.buildinfo
rm docs/.nojekyll

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root=%{buildroot}
popd
%endif # with_python3

%check
nosetests -q

%if 0%{?with_python3}
pushd %{py3dir}
nosetests-%{python3_version} -q
popd
%endif # with_python3

%clean
rm -rf %{buildroot}


%files -n  python2-simplejson
%defattr(-,root,root,-)
%doc docs LICENSE.txt
%{python_sitearch}/*

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-simplejson
%defattr(-,root,root,-)
%doc LICENSE.txt
%{python3_sitearch}/*
%endif # python3

%changelog
* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 3.3.3-2
- Add support for Python 3

* Wed Feb 19 2014 Luke Macken <lmacken@redhat.com> - 3.3.3-1
- Update to 3.3.3 (#960949)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May  2 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2.0-1
- Trim changelog to 5 years.
- Update to 3.2.0 upstream feature additions

* Tue Apr  9 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.3-1
- Update to upstream 3.1.3

* Thu Mar 21 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-1
- Update to upstream 3.1.2 (documentation fixes)

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0 in Rawhide.
- Build the python3 subpackage
- Update to new-style filtering of provides

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0 which changes some messages thrown by exceptions to match
  with json module in python3.3 stdlib.  Probably safe for older releases but
  the python3 version there is 3.2 so there's also not any real need yet.

* Tue May 15 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2
- This update adds new PI but should be backwards compatible

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 9 2011 Toshio Kuratomi <toshoi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 -- behaviour changing bugfixes

* Mon May 9 2011 Toshio Kuratomi <toshoi@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6 for a segfault fix

* Sat Apr 30 2011 Toshio Kuratomi <toshoi@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5, trivial upstream release (change makes more compact output)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Toshio Kuratomi <toshoi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Mon Dec 20 2010 Toshio Kuratomi <toshoi@fedoraproject.org> - 2.1.2-1
- Update to upstream 2.1.2, a bugfix release with four small, self-contained
  fixes.

* Wed Oct 20 2010 Toshio Kuratomi <toshoi@fedoraproject.org> - 2.1.1-4
- Simplify the %%files section to own the tests directory
- Use the fedora documented filter functions to filter provides

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jun 30 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 2.1.1-2
- Filter unnecessary provides
- License tag update
- Minor spec file cleanups

* Mon Jun 21 2010 Kyle VanderBeek <kylev@kylev.com> - 2.1.1-1
- Update to 2.1.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Kyle VanderBeek <kylev@kylev.com> - 2.0.9-2
- Remove ill-advised gcc BuildRequires

* Thu Jun  4 2009 Kyle VanderBeek <kylev@kylev.com> - 2.0.9-1
- Update to 2.0.9
- Make sure to require gcc to the speedups get compiled
- Fix description since we're not "pure" python
- Change to pypi instead of cheesehop

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> 2.0.7-1
- Update to 2.0.7

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.3-3
- Rebuild for Python 2.6

* Thu Oct 23 2008 Luke Macken <lmacken@redhat.com> 2.0.3-2
- Use nose to run the simplejson test suite

* Mon Oct 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.3-1
- update to 2.0.3

* Wed Oct 01 2008 Luke Macken <lmacken@redhat.com> - 2.0.1-1
- Update to 2.0.1, which contains many optimizations and bugfixes

* Wed Sep 24 2008 Luke Macken <lmacken@redhat.com> - 1.9.3-1
- Update to 1.9.3, which includes a significant decoding speed boost, and
  various bug fixes.

* Tue May 06 2008 Luke Macken <lmacken@redhat.com> - 1.9.1-1
- Update to 1.9.1

* Wed Apr 02 2008 Luke Macken <lmacken@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> - 1.7.4-1
- Update to 1.7.4

* Fri Feb  8 2008 Luke Macken <lmacken@redhat.com> - 1.7.3-3
- Rebuild for gcc 4.3
