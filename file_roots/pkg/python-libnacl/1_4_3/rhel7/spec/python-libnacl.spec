%global with_python3 1


%{!?__python2: %global __python2 /usr/bin/python%{?pybasever}}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global _description \
This library is used to gain direct access to the functions exposed by Daniel \
J. Bernstein's nacl library via libsodium or tweetnacl. It has been constructed \
to maintain extensive documentation on how to use nacl as well as being \
completely portable. The file in libnacl/__init__.py can be pulled out and \
placed directly in any project to give a single file binding to all of nacl.

%{!?python3_pkgversion:%global python3_pkgversion 3}

%global srcname libnacl


Name:           python-%{srcname}
Version:        1.4.3
Release:        3%{?dist}
Summary:        Python bindings for libsodium/tweetnacl based on ctypes

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/saltstack/libnacl
Source0:        https://pypi.python.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{srcname}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch


%description %{_description}

%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  libsodium
Requires:       libsodium

BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       libsodium
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
## %{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides: python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python 3 version.
%endif


%prep
%setup -q -n %{srcname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
rm -rf %{buildroot}
%py2_install

%if 0%{?with_python3}
%py3_install
%endif


%clean
rm -rf %{buildroot}


%files -n python2-%{srcname}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%license LICENSE

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%license LICENSE
%endif

%changelog
* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 1.4.3-3
- Add support for Python 3

* Tue Jan 16 2018 SaltStack Packaging Team <packaging@saltstack.com> - 1.4.3-2
- Support for Python 3 on RHEL 7 & 6
- Removed support for RHEL 5

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
