%global urllib3_unbundled_version 1.19.1


# SaltStack
%global python3_pkgversion 36
%global python3_other_pkgversion 0

Name:           python3-requests
Version:        2.12.5
Release:        4%{?dist}
Summary:        HTTP library, written in Python, for human beings

License:        ASL 2.0
URL:            http://python-requests.org/
Source0:        https://github.com/kennethreitz/requests/archive/v%{version}/requests-%{version}.tar.gz
# Explicitly use the system certificates in ca-certificates.
# https://bugzilla.redhat.com/show_bug.cgi?id=904614
Patch0:         python-requests-system-cert-bundle.patch

# Remove an unnecessary reference to a bundled compat lib in urllib3
# Some discussion with upstream:
# - https://twitter.com/sigmavirus24/status/529816751651819520
# - https://github.com/kennethreitz/requests/issues/1811
# - https://github.com/kennethreitz/requests/pull/1812
Patch1:         python-requests-remove-nested-bundling-dep.patch

# Tell setuptools about what version of urllib3 we're unbundling
# - https://github.com/kennethreitz/requests/issues/2816
Patch2:         python-requests-urllib3-at-%{urllib3_unbundled_version}.patch

BuildArch:      noarch

%description
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.

%package -n python%{python3_pkgversion}-requests
Summary: HTTP library, written in Python, for human beings

%{?python_provide:%python_provide python%{python3_pkgversion}-requests}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-chardet
BuildRequires:  python%{python3_pkgversion}-urllib3 == %{urllib3_unbundled_version}
Requires:       python%{python3_pkgversion}-chardet
Requires:       python%{python3_pkgversion}-idna
Requires:       python%{python3_pkgversion}-urllib3 == %{urllib3_unbundled_version}

%description -n python%{python3_pkgversion}-requests
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-requests
Summary: HTTP library, written in Python, for human beings

%{?python_provide:%python_provide python%{python3_pkgversion}-requests}

BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-chardet
BuildRequires:  python%{python3_other_pkgversion}-urllib3 == %{urllib3_unbundled_version}
Requires:       python%{python3_other_pkgversion}-chardet
Requires:       python%{python3_other_pkgversion}-idna
Requires:       python%{python3_other_pkgversion}-urllib3 == %{urllib3_unbundled_version}

%description -n python%{python3_other_pkgversion}-requests
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python’s built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.
%endif

%prep
%setup -q -n requests-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Unbundle the certificate bundle from mozilla.
rm requests/cacert.pem


%build
%py3_build
%if 0%{?python3_other_pkgversion}
%py3_other_build
%endif

# Unbundle chardet and urllib3.  We replace these with symlinks to system libs.
rm -r build/lib/requests/packages/chardet
rm -r build/lib/requests/packages/idna
rm -r build/lib/requests/packages/urllib3


%install
%py3_install
ln -s ../../chardet %{buildroot}/%{python3_sitelib}/requests/packages/chardet
ln -s ../../idna %{buildroot}/%{python3_sitelib}/requests/packages/idna
ln -s ../../urllib3 %{buildroot}/%{python3_sitelib}/requests/packages/urllib3
%if 0%{?python3_other_pkgversion}
%py3_other_install
%endif


## The tests succeed if run locally, but fail in koji.
## They require an active network connection to query httpbin.org
%check
#py.test-%{python3_version} -v
# At very, very least, we'll try to start python and import requests
PYTHONPATH=. %{__python3} -c "import requests"
%if 0%{?python3_other_pkgversion}
PYTHONPATH=. %{__python3_other} -c "import requests"
%endif


%files -n python%{python3_pkgversion}-requests
%license LICENSE
%doc NOTICE README.rst HISTORY.rst
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/requests/

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-requests
%license LICENSE
%doc NOTICE README.rst HISTORY.rst
%{python3_other_sitelib}/*.egg-info
%{python3_other_sitelib}/requests/
%endif


%changelog
* Sun Sep 22 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2.12.5-5
- Support for Redhat 7 with Python 3.6 without EPEL

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 2.12.5-3
- Rebuilt to change main python from 3.4 to 3.6

* Sun Nov 4 2018 Orion Poplwski <orion@nwra.com> - 2.12.5-2
- Ship python36-requests (bug #1645072)

* Thu Apr 5 2018 Orion Poplwski <orion@cora.nwra.com> - 2.12.5-1
- Update to 2.12.5

* Sun Dec 4 2016 Orion Poplwski <orion@cora.nwra.com> - 2.12.3-1
- Update to 2.12.3

* Sun Dec 4 2016 Orion Poplwski <orion@cora.nwra.com> - 2.12.1-2
- Add missing BR on setuptools

* Mon Nov 28 2016 Orion Poplwski <orion@cora.nwra.com> - 2.12.1-1
- Initial EPEL7 package
