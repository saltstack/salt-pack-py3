# Enable building without docs to avoid a circular dependency between this
# and python-sphinx:
# Fails on EL6
%if 0%{?rhel} >= 7
%global with_docs 1
%else
%global with_docs 0
%endif

#SaltStack
%global with_docs 0
%global python3_pkgversion 36 
%global python3_other_pkgversion 0
%bcond_with tests


Name:           python3-jinja2
Version:        2.8.1
Release:        3%{?dist}
Summary:        General purpose template engine
License:        BSD
URL:            http://jinja.pocoo.org/
Source0:        https://github.com/pallets/jinja/archive/%{version}/jinja-%{version}.tar.gz
# CVE-2019-10906 - backport of https://github.com/pallets/jinja/commit/a2a6c930bcca591a25d2b316fcfd2d6793897b26
Patch0:         jinja2-CVE-2019-10906.patch

BuildArch:      noarch

%description
Jinja2 is a template engine written in pure Python.  It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.


%package -n python%{python3_pkgversion}-jinja2
Summary:        General purpose template engine
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-markupsafe
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%if 0%{?with_docs}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif # with_docs
Requires:       python%{python3_pkgversion}-markupsafe
Requires:       python%{python3_pkgversion}-setuptools
# babel isn't py3k ready yet, and is only a weak dependency
#Requires:       python%{python3_pkgversion}-babel >= 0.8


%description -n python%{python3_pkgversion}-jinja2
Jinja2 is a template engine written in pure Python.  It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.


%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-jinja2
Summary:        General purpose template engine
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-markupsafe
%if %{with tests}
BuildRequires:  python%{python3_other_pkgversion}-pytest
%endif
Requires:       python%{python3_other_pkgversion}-markupsafe
Requires:       python%{python3_other_pkgversion}-setuptools
# babel isn't py3k ready yet, and is only a weak dependency
#Requires:       python%{python3_other_pkgversion}-babel >= 0.8


%description -n python%{python3_other_pkgversion}-jinja2
Jinja2 is a template engine written in pure Python.  It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.
%endif


%if 0%{?with_docs}
%package doc
Summary:        Documentation for python3-jinja2

%description doc
Documentation for python3-jinja2.
%endif # with_docs


%prep
%setup -q -n jinja-%{version}
%patch0 -p1 -b .CVE-2019-10906
# fix EOL
sed -i 's|\r$||g' LICENSE


%build
%py3_build
%if 0%{?python3_other_pkgversion}
%py3_other_build
%endif
%if 0%{?with_docs}
%make_build -C docs html PYTHONPATH=$(pwd) SPHINXBUILD=sphinx-build-%{python3_version}
%endif # with_docs


%install
%if 0%{?python3_other_pkgversion}
%py3_other_install
%endif
%py3_install
# This gets installed on EL7+
rm -f %{buildroot}%{python3_sitelib}/jinja2/_debugsupport.c


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version}
%endif


%files -n python%{python3_pkgversion}-jinja2
%license LICENSE
%doc AUTHORS CHANGES ext examples
%{python3_sitelib}/jinja2/
%{python3_sitelib}/Jinja2-%{version}-py?.?.egg-info/

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-jinja2
%license LICENSE
%doc AUTHORS CHANGES ext examples
%{python3_other_sitelib}/jinja2/
%{python3_other_sitelib}/Jinja2-%{version}-py?.?.egg-info/
%endif

%if 0%{?with_docs}
%files doc
%license LICENSE
# docs are built with python2
%doc docs/_build/html
%endif # with_docs


%changelog
* Sun Sep 22 2019 SaltStack Packaging Team <packaging@saltstack.com>  - 2.8.1-3
- Support for Redhat 7 Python 3.6 without EPEL and tests

* Sat Apr 13 2019 Orion Poplawski <orion@nwra.com> - 2.8.1-2
- Backport fix for CVE-2016-10745 (bugz#1698839)

* Sat Apr 13 2019 Orion Poplawski <orion@nwra.com> - 2.8.1-1
- Update to 2.8.1 (CVE-2016-10745 bugz#1698350)

* Thu Apr  4 2019 Orion Poplawski <orion@nwra.com> - 2.8-4
- Build for python3_other

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 2.8-3
- Rebuilt to change main python from 3.4 to 3.6

* Tue Nov 29 2016 Orion Poplawski <orion@cora.nwra.com> - 2.8-2
- Use github tarball and run tests
- Split documentation in sub-package

* Fri Sep 16 2016 Orion Poplawski <orion@cora.nwra.com> - 2.8-1
- Initial EPEL package
