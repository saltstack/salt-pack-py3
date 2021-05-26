%{!?python3_pkgversion:%global python3_pkgversion 3}

Name: python-contextvars
Version: 2.4
Release: 1%{?dist}
Summary: python-contextvars
License: ASL 2.0
URL: https://github.com/MagicStack/contextvars
Source0: https://pypi.org/packages/source/c/contextvars/contextvars-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python%{python3_pkgversion}-setuptools
#BuildRequires: epel-rpm-macros
BuildRequires: python3-rpm-macros
#BuildRequires: python3-rpm-generators

%description
Python Contextvars Backport

%package -n python%{python3_pkgversion}-contextvars
Summary: python-contextvars
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-immutables
%{?python_provide:%python_provide python%{python3_pkgversion}-contextvars}

%description -n python%{python3_pkgversion}-contextvars


%prep
%autosetup -n contextvars-2.4

%build
#%%py3_build
CFLAGS="%{optflags}" %{__python3} setup.py %{?py_setup_args} build --executable="%{__python3} %{py3_shbang_opts}" %{?*}
sleep 1


%install
#%%py3_install
CFLAGS="%{optflags}" %{__python3} setup.py %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?*}


%files -n python%{python3_pkgversion}-contextvars
%license LICENSE
%doc README.rst
%{python3_sitelib}/contextvars-*.egg-info/
%{python3_sitelib}/contextvars/
