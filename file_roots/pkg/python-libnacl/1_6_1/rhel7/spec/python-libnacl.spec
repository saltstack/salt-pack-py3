%bcond_with python2 
%bcond_without python3

%{!?python3_pkgversion:%global python3_pkgversion 3}

%global _description \
This library is used to gain direct access to the functions exposed by Daniel \
J. Bernstein's nacl library via libsodium or tweetnacl. It has been constructed \
to maintain extensive documentation on how to use nacl as well as being \
completely portable. The file in libnacl/__init__.py can be pulled out and \
placed directly in any project to give a single file binding to all of nacl.

%global srcname libnacl

Name:           python-%{srcname}
Version:        1.6.1
Release:        3%{?dist}
Summary:        Python bindings for libsodium/tweetnacl based on ctypes
Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/saltstack/libnacl
Source0:        https://pypi.python.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{srcname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description    %{_description}

%if %{with python2}
%package -n     python2-%{srcname}
Summary:        %{summary}
Group:          Development/Libraries
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  libsodium
Requires:       libsodium
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.
%endif



%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:  Python bindings for libsodium/tweetnacl based on ctypes
Group:    Development/Libraries
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  libsodium
Requires:       libsodium

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

Python 3 version.
%endif


%prep
%autosetup -n %{srcname}-%{version}

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf %{buildroot}

%if %{with python2}
%files
%defattr(-,root,root,-)
%{python2_sitelib}/*
%license LICENSE
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%license LICENSE
%endif

%changelog
* Wed Jun 05 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.6.1-3
- Added support for Redhat 7 Python 3.6, and support for Python 2 packages optional

* Thu Apr 04 2019 Packaging <pqackaging@saltstack.com> - 1.6.1-2
- Adjust support for Python 3.6

* Fri Apr 20 2018 Packaging <pqackaging@saltstack.com> - 1.6.1-1
- Updated to 1.6.1 and removed support for Redhat 5, adjust support for Python 3

* Wed Aug  5 2015 Packaging <pqackaging@saltstack.com> - 1.4.3-1
- Updated to 1.4.3

* Wed May 27 2015 Erik Johnson <erik@saltstack.com> - 1.4.2-1
- Updated to 1.4.2, added license file

* Thu Sep  4 2014 Erik Johnson <erik@saltstack.com> - 1.3.5-1
- Updated to 1.3.5

* Fri Aug 22 2014 Erik Johnson <erik@saltstack.com> - 1.3.3-1
- Updated to 1.3.3

* Fri Aug  8 2014 Erik Johnson <erik@saltstack.com> - 1.3.2-1
- Updated to 1.3.2

* Fri Aug  8 2014 Erik Johnson <erik@saltstack.com> - 1.3.1-1
- Updated to 1.3.1

* Thu Aug  7 2014 Erik Johnson <erik@saltstack.com> - 1.3.0-1
- Updated to 1.3.0

* Fri Jun 20 2014 Erik Johnson <erik@saltstack.com> - 1.0.0-1
- Initial build
