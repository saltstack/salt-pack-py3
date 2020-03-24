#sphinx on EPEL7 is too old
%global bcond_with doc

#SaltStack
%global python3_pkgversion 36

Summary: Python wrapper module around the OpenSSL library
Name: python3-pyOpenSSL
Version: 17.3.0
Release: 2%{?dist}
Source0: https://files.pythonhosted.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz
Source1: https://files.pythonhosted.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz.asc

BuildArch: noarch
License: ASL 2.0
Url: http://pyopenssl.sourceforge.net/

%if %{with doc}
BuildRequires: python-sphinx
BuildRequires: python-sphinx_rtd_theme
%endif

%description
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

%package -n python%{python3_pkgversion}-pyOpenSSL
Summary: Python 3 wrapper module around the OpenSSL library
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-cryptography >= 1.3.0
Requires: python%{python3_pkgversion}-cryptography
%{?python_provide:%python_provide python%{python3_pkgversion}-pyOpenSSL}

%description -n python%{python3_pkgversion}-pyOpenSSL
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes

This is the Python %{python3_pkgversion} build of the module

%if %{with doc}
%package -n python%{python3_pkgversion}-pyOpenSSL-doc
Summary: Documentation for pyOpenSSL

%description -n python%{python3_pkgversion}-pyOpenSSL-doc
Documentation for pyOpenSSL
%endif

%prep
%setup -q -n pyOpenSSL-%{version}


%build
%py3_build
%if %{with doc}
%{__make} -C doc html
%endif


%install
%py3_install


%files -n python%{python3_pkgversion}-pyOpenSSL
%license LICENSE
%{python3_sitelib}/OpenSSL/
%{python3_sitelib}/pyOpenSSL-*.egg-info

%if %{with doc}
%files -n python%{python3_pkgversion}-pyOpenSSL-doc
%license LICENSE
%doc CHANGELOG.rst examples doc/_build/html
%endif


%changelog
* Tue Mar 24 2020 SaltStack Packaging Team <packaging@saltstack.com> - 17.3.0-2
- Updated for Salt packaging, work-around for python3_pkgversion 3

* Wed Jan 31 2018 Orion Poplawski <orion@nwra.com> - 17.3.0-1
- EPEL package
