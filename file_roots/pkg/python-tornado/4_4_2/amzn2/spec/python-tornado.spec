%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%endif


%{!?python3_pkgversion:%global python3_pkgversion 3}

%global srcname tornado

Name:           python3-%{srcname}
Version:        4.4.2
Release:        4%{?dist}
Summary:        Scalable, non-blocking web server and tools

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://www.tornadoweb.org
Source0:        https://github.com/tornadoweb/tornado/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Patch to use system CA certs instead of certifi
Patch0:         python-tornado-cert.patch
# Patch to run tests from project dir
# https://github.com/tornadoweb/tornado/pull/1781
Patch1:         python-tornado-test.patch
# Patch to ignore all DeprecationWarnings
Patch2:         python-tornado-test-deprecation.patch

%description
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Scalable, non-blocking web server and tools
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
%if 0%{?python3_pkgversion} < 35
# Only needed for python < 3.5
BuildRequires:  python%{python3_pkgversion}-backports_abc
%endif
Requires:       python%{python3_pkgversion}-pycurl
%if 0%{?python3_pkgversion} < 35
# Only needed for python < 3.5
Requires:       python%{python3_pkgversion}-backports_abc
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.


%package doc
Summary:        Examples for python-tornado
Group:          Documentation

%description doc
Tornado is an open source version of the scalable, non-blocking web
server and and tools. This package contains some example applications.


%prep 
%setup -q -n %{srcname}-%{version}
%patch0 -p1 -b .cert
%patch1 -p1 -b .test
%patch2 -p1 -b .test-deprecation
# remove shebang from files
sed -i.orig -e '/^#!\//, 1d' *py tornado/*.py tornado/*/*.py


%build
%py3_build
# Need to wait for python3-sphinx
#sphinx-build -q -E -n -W -b html docs docs/html



%install
%py3_install


%check
%{__python3} -m tornado.test.runtests --verbose


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-*.egg-info

%files doc
%license LICENSE
%doc demos


%changelog
* Mon Jan 13 2020 SaltStack Packaging Team <packaging@saltstack.com> - 4.4.2-4
- added definition for python3_pkgversion 3 if not exists

* Mon Jul 01 2019 SaltStack Packaging Team <packaging@saltstack.com> - 4.4.2-3
- Updated for support Amazon Linux 2 Python 3 only

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 4.4.2-3
- Rebuilt to change main python from 3.4 to 3.6

* Thu Nov 17 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.2-1
- Update to 4.4.2

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.1-1
- Update to 4.4.1

* Thu Feb 18 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3-1
- Initial EPEL package
