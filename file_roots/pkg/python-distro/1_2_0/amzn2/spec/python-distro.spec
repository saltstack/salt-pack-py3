%global pypi_name distro

%if 0%{?rhel} && 0%{?rhel} == 8
%bcond_with python2
%bcond_without python3
%bcond_with tests

%else

%if 0%{?rhel} && 0%{?rhel} <= 6
%bcond_with python3
%else
%bcond_without python3
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with tests
%else
%bcond_without tests
%endif

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%bcond_with python2
%bcond_without python3
%bcond_with tests
%endif

%endif

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        5%{?dist}
Summary:        Linux Distribution - a Linux OS platform information API

License:        ASL 2.0
URL:            https://github.com/nir0s/distro
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%global _description \
The distro (for: Linux Distribution) package provides information about the\
Linux distribution it runs on, such as a reliable machine-readable ID, or\
version information.\
\
It is a renewed alternative implementation for Python's original\
platform.linux_distribution function, but it also provides much more\
functionality. An alternative implementation became necessary because\
Python 3.5 deprecated this function, and Python 3.7 is expected to remove it\
altogether. Its predecessor function platform.dist was already deprecated since\
Python 2.6 and is also expected to be removed in Python 3.7. Still, there are\
many cases in which access to that information is needed. See Python issue 1322\
for more information.

# ' for python''s


%description %{_description}

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
%endif
BuildRequires:  python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
%else
BuildRequires:  python2-setuptools
%endif
%if 0%{?fedora}
Suggests:       /usr/bin/lsb_release
%endif
%if %{with tests}
BuildRequires: python%{python3_pkgversion}-tox >= 2.4.0
%endif
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name} %{_description}

Python 2 version.
%endif

%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python%{python3_pkgversion}-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?fedora}
Suggests:       /usr/bin/lsb_release
%endif
%if 0%{?epel}
# /usr/bin/distro was moved from there
Conflicts:      python2-%{pypi_name} < 1.2.0-2
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif


%check
%if %{with tests}
tox
%endif


%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst CHANGES README.md
%license LICENSE
%{python2_sitelib}/%{pypi_name}-*.egg-info/
%{python2_sitelib}/%{pypi_name}.py*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst CHANGES README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%endif

%{_bindir}/distro

%changelog
* Thu Jun 13 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.2.0-5
- Added support for Amazon Linux 2 Python 3

* Wed May 08 2019 SaltStack Packaging Team <packaging@saltstack.com> - 1.2.0-4
- Added support for Redhat 8, and support for Python 2 packages optional

* Wed Apr 24 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Add explicit conflicts for clean update path of /usr/bin/distro

* Mon Feb 04 2019 Scott K Logan <logans@cottsay.net> 1.2.0-2
- add python 3 support for EL7

* Tue Jan 02 2018 Miroslav Suchý <msuchy@redhat.com> 1.2.0-1
- run tests
- rebase to distro 1.2.0

* Mon Mar 20 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.3-1
- rebase to 1.0.3

* Tue Jan 24 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.2-3
- typo in license macro

* Tue Jan 24 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.2-2
- add license macro for el6

* Tue Jan 24 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.2-1
- update to 1.0.2
- 1415667 - require python-argparse on EL6

* Tue Jan 03 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.1-2
- soft deps on lsb_release

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Provide only one copy of $bindir/distro
- Cleanups in spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-7
- Rebuild for Python 3.6

* Thu Oct 06 2016 Miroslav Suchý <msuchy@redhat.com> 1.0.0-6
- polish spec according the package review

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-5
- use python3 in /usr/bin/distro on Fedoras

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-4
- use python3 in /usr/bin/distro on Fedoras

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-3
- python2 subpackages only on rhel
- correct description

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-2
- require lsb_release

* Wed Oct 05 2016 Miroslav Suchý 1.0.0-1
- initial packaging

