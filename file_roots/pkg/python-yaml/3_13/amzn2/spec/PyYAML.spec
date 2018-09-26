Name:           PyYAML
Version:        4.2
Release:        0.1.b4%{?dist}
%global uversion %{version}b4
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            https://github.com/yaml/pyyaml
Source0:        https://github.com/yaml/pyyaml/archive/%{name}-%{uversion}.tar.gz

BuildRequires:  gcc
BuildRequires:  libyaml-devel

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-Cython

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython


%global _description\
YAML is a data serialization format designed for human readability and\
interaction with scripting languages.  PyYAML is a YAML parser and\
emitter for Python.\
\
PyYAML features a complete YAML 1.1 parser, Unicode support, pickle\
support, capable extension API, and sensible error messages.  PyYAML\
supports standard YAML tags and provides Python-specific tags that\
allow to represent an arbitrary Python object.\
\
PyYAML is applicable for a broad range of tasks from complex\
configuration files to object serialization and persistance.

%description %_description


%package -n python2-pyyaml
Summary:        %summary
Provides:       python-yaml = %{version}-%{release}
Provides:       python-yaml%{?_isa} = %{version}-%{release}
Provides:       python2-yaml = %{version}-%{release}
Provides:       python2-yaml%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python2-pyyaml}
# Remove before F30
Provides: PyYAML = %{version}-%{release}
Provides: PyYAML%{?_isa} = %{version}-%{release}
Obsoletes: PyYAML < %{version}-%{release}

%description -n python2-pyyaml %_description


%package -n python3-pyyaml
Summary:        %summary
Provides:       python3-yaml = %{version}-%{release}
Provides:       python3-yaml%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-pyyaml}
# Remove before F31
Provides:       python3-PyYAML = %{version}-%{release}
Provides:       python3-PyYAML%{?_isa} = %{version}-%{release}
Obsoletes:      python3-PyYAML < 4.1-5

%description -n python3-pyyaml %_description


%prep
%setup -q -n %{name}-%{uversion}
chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
%{__python2} setup.py test
%{__python3} setup.py test


%files -n python2-pyyaml
%license LICENSE
%doc CHANGES README examples
%{python2_sitearch}/*

%files -n python3-pyyaml
%license LICENSE
%doc CHANGES README examples
%{python3_sitearch}/*


%changelog
* Wed Sep 26 2018 SaltStack Packaging Team <packaging@saltstack.com> - 4.2-0.1.b4
- Ported to Amazon Linux 2 for Python 3 support

* Fri Jul 13 2018 John Eckersberg <eck@redhat.com> - 4.2-0.1.b4
- New upstream beta release 4.2b4
- Replaces 4.1 which was retracted upstream
  See https://mail.python.org/pipermail/python-announce-list/2018-June/011977.html
- Add BuildRequires for gcc
  See https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Jul 12 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1-5
- Rename python3-PyYAML to python3-pyyaml
- Modernize spec
- Fix python2 invocation

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1-3
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1-2
- Rebuilt for Python 3.7

* Wed Jun 27 2018 John Eckersberg <eck@redhat.com> - 4.1-1
- New upstream release 4.1

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 3.12-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.12-9
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 3.12-8
- Cleanup spec file conditionals

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.12-7
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.12-6
- Python 2 binary package renamed to python2-pyyaml
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.12-2
- Rebuild for Python 3.6

* Mon Aug 29 2016 John Eckersberg <eck@redhat.com> - 3.12-1
- New upstream release 3.12 (RHBZ#1371150)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  8 2015 John Eckersberg <eck@redhat.com> - 3.11-11
- Add provides for python3-yaml (RHBZ#1288807)

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 3.11-10
- Rebuilt for Python3.5 rebuild

* Fri Jul 17 2015 John Eckersberg <eck@redhat.com> - 3.11-9
- Add provides for python2-yaml (RHBZ#1241678)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 John Eckersberg <eck@redhat.com> - 3.11-7
- Add patch for CVE-2014-9130 (bug 1204829)

* Mon Sep 15 2014 Jakub Čajka <jcajka@redhat.com> - 3.11-6
- fixed typecast issues using debian patch(int->size_t)(BZ#1140189)
- spec file cleanup

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Tom Callaway <spot@fedoraproject.org> - 3.11-4
- fix license handling

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 21 2014 John Eckersberg <jeckersb@redhat.com> - 3.11-1
- New upstream release 3.11 (BZ#1081521)

* Thu Aug  8 2013 John Eckersberg <jeckersb@redhat.com> - 3.10-9
- Add check section and run test suite

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 3.10-6
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Wed Aug  1 2012 David Malcolm <dmalcolm@redhat.com> - 3.10-5
- remove rhel logic from with_python3 conditional

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 John Eckersberg <jeckersb@redhat.com> - 3.10-3
- Add Provides for python-yaml (BZ#740390)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 John Eckersberg <jeckersb@redhat.com> - 3.10-1
- New upstream release 3.10

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 John Eckersberg <jeckersb@redhat.com> - 3.09-7
- Add support to build for python 3

* Tue Jul 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.09-6
- Bump release number for upgrade path

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.09-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Oct 02 2009 John Eckersberg <jeckersb@redhat.com> - 3.09-1
- New upstream release 3.09

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 - John Eckersberg <jeckersb@redhat.com> - 3.08-5
- Minor tweaks to spec file aligning with latest Fedora packaging guidelines
- Enforce inclusion of libyaml in build with --with-libyaml option to setup.py
- Deliver to %%{python_sitearch} instead of %%{python_sitelib} due to _yaml.so
- Thanks to Gareth Armstrong <gareth.armstrong@hp.com>

* Tue Mar 3 2009 John Eckersberg <jeckersb@redhat.com> - 3.08-4
- Correction, change libyaml to libyaml-devel in BuildRequires

* Mon Mar 2 2009 John Eckersberg <jeckersb@redhat.com> - 3.08-3
- Add libyaml to BuildRequires

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 John Eckersberg <jeckersb@redhat.com> - 3.08-1
- New upstream release

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.06-2
- Rebuild for Python 2.6

* Fri Oct 24 2008 John Eckersberg <jeckersb@redhat.com> - 3.06-1
- New upstream release

* Wed Jan 02 2008 John Eckersberg <jeckersb@redhat.com> - 3.05-2
- Remove explicit dependency on python >= 2.3
- Remove executable on example script in docs

* Mon Dec 17 2007 John Eckersberg <jeckersb@redhat.com> - 3.05-1
- Initial packaging for Fedora
