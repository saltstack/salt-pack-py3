%global modname pycurl


#SaltStack
%global python3_pkgversion 36
%global python3_other_pkgversion 0
%bcond_with tests

Name:           python3-%{modname}
Version:        7.43.0
Release:        8%{?dist}
Summary:        A Python interface to libcurl

License:        LGPLv2+ or MIT
URL:            http://pycurl.io/
Source0:        https://dl.bintray.com/pycurl/pycurl/pycurl-%{version}.tar.gz
# Run pyflakes with Python 3 or don't run it at all
Patch0:         python3-pycurl-py3.patch

BuildRequires:  curl-devel >= 7.19.0
BuildRequires:  openssl-devel
BuildRequires:  vsftpd

# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
%global libcurl_sed '/^#define LIBCURL_VERSION "/!d;s/"[^"]*$//;s/.*"//;q'
%global curlver_h /usr/include/curl/curlver.h
%global libcurl_ver %(sed %{libcurl_sed} %{curlver_h} 2>/dev/null || echo 0)

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.


%package -n python%{python3_pkgversion}-%{modname}
Summary:        Python interface to libcurl for Python 3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-bottle
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-nose
%endif
Requires:       libcurl%{?_isa} >= %{libcurl_ver}

%description -n python%{python3_pkgversion}-%{modname}
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

Python %{python3_version} version.


%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{modname}
Summary:        Python interface to libcurl for Python 3
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{modname}}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-bottle
BuildRequires:  python%{python3_other_pkgversion}-nose
Requires:       libcurl%{?_isa} >= %{libcurl_ver}

%description -n python%{python3_other_pkgversion}-%{modname}
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

Python %{python3_other_version} version.
%endif


%prep
%autosetup -n %{modname}-%{version} -p1

# remove binaries packaged by upstream
rm -f tests/fake-curl/libcurl/*.so

# remove a test-case that relies on sftp://web.sourceforge.net being available
rm -f tests/ssh_key_cb_test.py

# remove tests depending on the 'flaky' nose plug-in (not available in Fedora)
grep '^import flaky' -r tests | cut -d: -f1 | xargs rm -fv

# drop options that are not supported by nose in Fedora
sed -e 's/ --show-skipped//' \
    -e 's/ --with-flaky//' \
    -i tests/run.sh

# no realpath on EL6
%{?el6:sed -i -e 's/realpath/readlink -e/' tests/ext/test-lib.sh}

%build
%py3_build -- --with-nss
%if 0%{?python3_other_pkgversion}
%py3_other_build -- --with-nss
%endif

%install
%if 0%{?python3_other_pkgversion}
%py3_other_install
%endif
%py3_install
rm -rf %{buildroot}%{_datadir}/doc/pycurl

%if %{with tests}
%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYCURL_VSFTPD_PATH=/usr/sbin/vsftpd
export PYTHON=%{__python3}
make test PYTHON=%{__python3} NOSETESTS="nosetests-%{python3_version} -v" \
          PYFLAKES=/usr/bin/true
rm -fv tests/fake-curl/libcurl/*.so
%if 0%{?python3_other_pkgversion}
export PYTHONPATH=%{buildroot}%{python3_other_sitearch}
export PYTHON=%{__python3_other}
make test PYTHON=%{__python3_other} NOSETESTS="nosetests-%{python3_other_version} -v" \
          PYFLAKES=/usr/bin/true
rm -fv tests/fake-curl/libcurl/*.so
%endif
%endif


%files -n python%{python3_pkgversion}-pycurl
%license COPYING-LGPL COPYING-MIT
%doc ChangeLog README.rst examples doc tests
%{python3_sitearch}/curl/
%{python3_sitearch}/%{modname}.*.so
%{python3_sitearch}/%{modname}-%{version}-*.egg-info

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-pycurl
%license COPYING-LGPL COPYING-MIT
%doc ChangeLog README.rst examples doc tests
%{python3_other_sitearch}/curl/
%{python3_other_sitearch}/%{modname}.*.so
%{python3_other_sitearch}/%{modname}-%{version}-*.egg-info
%endif


%changelog
* Sun Sep 22 2019 SaltStack Packaging Team <packaging@saltstack.com> - 7.43.0-8
- Support for Redhat 7 Pyton 3.6 without EPEL

* Sun May  5 2019 Orion Poplawski <orion@nwra.com> - 7.43.0-7
- Build for python3_other (bugz#1705680)

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 7.43.0-6
- Rebuilt to change main python from 3.4 to 3.6

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> - 7.43.0-5
- Fix build on EL6

* Tue Nov 8 2016 Orion Poplawski <orion@cora.nwra.com> - 7.43.0-4
- Add patch to build with python3 pyflakes

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 7.43.0-3
- EPEL7 version
