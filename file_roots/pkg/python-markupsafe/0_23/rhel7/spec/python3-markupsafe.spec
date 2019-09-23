
#SaltStack
%global python3_pkgversion 36
%global python3_other_pkgversion 0

Name: python3-markupsafe
Version: 0.23
Release: 4%{?dist}
Summary: Implements a XML/HTML/XHTML Markup safe string for Python

License: BSD
URL: http://pypi.python.org/pypi/MarkupSafe
Source0: http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz

%description
A library for safe markup escaping.


%package -n python%{python3_pkgversion}-markupsafe
Summary: %summary
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-markupsafe
A library for safe markup escaping.


%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-markupsafe
Summary: %summary
BuildRequires: python%{python3_other_pkgversion}-devel
BuildRequires: python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-markupsafe
A library for safe markup escaping.
%endif


%prep
%setup -q -n MarkupSafe-%{version}


%build
%py3_build
%if 0%{?python3_other_pkgversion}
%py3_other_build
%endif


%install
%py3_install
%if 0%{?python3_other_pkgversion}
%py3_other_install
%endif


%check
%{__python3} setup.py test
%if 0%{?python3_other_pkgversion}
%{__python3_other} setup.py test
%endif


%files -n python%{python3_pkgversion}-markupsafe
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitearch}/*

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-markupsafe
%license LICENSE
%doc AUTHORS README.rst
%{python3_other_sitearch}/*
%endif


%changelog
* Sun Sep 22 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.23-4
- Support for Redhat 7 Python 3.6 without EPEL

* Thu Apr 04 2019 Orion Poplawski <orion@nwra.com> - 0.23-3
- Build for python3_other

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 0.23-2
- Rebuilt to change main python from 3.4 to 3.6

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 0.23-1
- Initial EPEL package
