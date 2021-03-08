Name: python-immutables
Version: 0.14
Release: 1%{?dist}
Summary: python-immutables
License: ASL 2.0
URL: https://github.com/MagicStack/immutables
Source0: https://pypi.org/packages/source/i/immutables/immutables-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: epel-rpm-macros
BuildRequires: python3-rpm-macros
BuildRequires: python3-rpm-generators

%description
Python Immutables Backport

%package -n python%{python3_pkgversion}-immutables
Summary: python-immutables
Requires: python%{python3_pkgversion}
%{?python_provide:%python_provide python%{python3_pkgversion}-immutables}

%description -n python%{python3_pkgversion}-immutables


%prep
%autosetup -n immutables-0.14

%build
%py3_build

%install
%py3_install


%files -n python%{python3_pkgversion}-immutables
%license LICENSE
%doc README.rst
%{python3_sitearch}/immutables-*.egg-info/
%{python3_sitearch}/immutables/
