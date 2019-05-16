%bcond_with python2
%bcond_without python3

Name:           python-gnupg
Version:        0.4.4
Release:        2%{?dist}
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

License:        BSD
URL:            https://gnupg.readthedocs.io/
Source0:        https://pypi.io/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
GnuPG bindings for python. This uses the gpg command.

%if %{with python2}
%package -n     python2-gnupg
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       gnupg
%{?python_provide:%python_provide python2-gnupg}
%{?el6:Provides: python-gnupg}
%{?el6:Obsoletes: python-gnupg < 0.3.8}

%description -n python2-gnupg
GnuPG bindings for python. This uses the gpg command.
%endif

%if %{with python3}
%package -n     python3-gnupg
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       gnupg
%{?python_provide:%python_provide python3-gnupg}

%description -n python3-gnupg
GnuPG bindings for python. This uses the gpg command.
%endif # with python3

%prep
%autosetup -n %{name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif # with python3

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif # with python3

%if %{with python2}
%files -n python2-gnupg
%{!?_licensedir:%global license %doc}
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/gnupg.py*
%{python2_sitelib}/python_gnupg-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-gnupg
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/gnupg.py
%{python3_sitelib}/python_gnupg-%{version}-py?.?.egg-info
%endif # with python3

%changelog
* Wed May 15 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.4.4-2
- Added support for Redhat 8, and support for Python 2 packages optional

* Fri Apr 26 2019 Paul Wouters <pwouters@redhat.com> - 0.4.4-1
- Resolves rhbz#1670364 Fixes CVE-2019-6690

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Paul Wouters <pwouters@redhat.com> - 0.4.3-1
- Updated to 0.4.3, updated URL and Source fields
- Resolves: rhbz#1547638 New version is available

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-10
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.8-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3.8-3
- Put the gnupg dependence for both py2 and py3 packages

* Wed May 04 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3.8-2
- Fix provides and obsoletes

* Sun Feb 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.3.8-1
- Enable python3 compilation
- Move to current python standard
- Update 0.3.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 06 2015 Paul Wouters <pwouters@redhat.com> - 0.3.7-1
- Updated to 0.3.7 Merged in export-minimal and armor options, many encoding fixes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-3
- Removed patch as gpg.decode_errors=ignore works well

* Thu Apr 17 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-2
- Re-instate part of export patch that fixed encoding bug

* Thu Feb 06 2014 Paul Wouters <pwouters@redhat.com> - 0.3.6-1
- Updated to 0.3.6 which includes Security fix (CVE-2014-XXXX)
- Upstream including our export patch and converted README file
- Upstream switched to new download site

* Mon Jan 06 2014 Paul Wouters <pwouters@redhat.com> - 0.3.5-4
- Require gnupg (duh)
- Remove cleaning in install target
- Fix license to BSD
- Link to upstream bug tracker for included patch

* Sat Jan 04 2014 Paul Wouters <pwouters@redhat.com> - 0.3.5-3
- Remove unused global, fix python macro, buildroot macro
- Converted README from DOS to unix (and reported upstream)

* Tue Dec 31 2013 Paul Wouters <pwouters@redhat.com> - 0.3.5-2
- Added minimal= and armor= options to export_keys()

* Sun Dec 22 2013 Paul Wouters <pwouters@redhat.com> - 0.3.5-1
- Initial package
