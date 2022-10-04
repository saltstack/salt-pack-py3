## For Python 3 only 

# Release Candidate
%global __rc_ver %{nil}

%global fish_dir %{_datadir}/fish/vendor_functions.d
%global zsh_dir %{_datadir}/zsh/site-functions

# py3_shbang_flags is '-s' and causing issues with pip install.
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

Name:    salt
Version: master%{?__rc_ver}
Release: 0%{?dist}
Summary: A parallel remote execution system
Group:   System Environment/Daemons
License: ASL 2.0
URL:     https://saltproject.io/
Source0: %{pypi_source}
Source1: %{name}-proxy@.service
Source2: %{name}-master
Source3: %{name}-syndic
Source4: %{name}-minion
Source5: %{name}-api
Source6: %{name}-master.service
Source7: %{name}-syndic.service
Source8: %{name}-minion.service
Source9: %{name}-api.service
Source10: README.fedora
Source11: %{name}-common.logrotate
Source12: %{name}.bash
Source13: %{name}.fish
Source14: %{name}_common.fish
Source15: %{name}-call.fish
Source16: %{name}-cp.fish
Source17: %{name}-key.fish
Source18: %{name}-master.fish
Source19: %{name}-minion.fish
Source20: %{name}-run.fish
Source21: %{name}-syndic.fish

Patch0: contextvars.patch
BuildArch: noarch

%ifarch %{ix86} x86_64
Requires: dmidecode
%endif

Requires: pciutils
Requires: which
Requires: dnf-utils
Requires: logrotate

BuildRequires: systemd-rpm-macros
BuildRequires: python3-devel


%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in
the world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds or even thousands of individual
servers, handle them quickly and through a simple and manageable interface.


%package    master
Summary:    Management component for salt, a parallel remote execution system
Group:      System Environment/Daemons
Requires:   %{name} = %{version}-%{release}
Requires:   python3-systemd

%description master
The Salt master is the central server to which all minions connect.
Supports Python 3.


%package    minion
Summary:    Client component for Salt, a parallel remote execution system
Group:      System Environment/Daemons
Requires:   %{name} = %{version}-%{release}

%description minion
The Salt minion is the agent component of Salt. It listens for instructions
from the master, runs jobs, and returns results back to the master.
Supports Python 3.


%package    syndic
Summary:    Master-of-master component for Salt, a parallel remote execution system
Group:      System Environment/Daemons
Requires:   %{name}-master = %{version}-%{release}

%description syndic
The Salt syndic is a master daemon which can receive instruction from a
higher-level master, allowing for tiered organization of your Salt
infrastructure.
Supports Python 3.


%package    api
Summary:    REST API for Salt, a parallel remote execution system
Group:      Applications/System
Requires:   %{name}-master = %{version}-%{release}
Requires:   python3-cherrypy >= 3.2.2

%description api
salt-api provides a REST interface to the Salt master.
Supports Python 3.


%package    cloud
Summary:    Cloud provisioner for Salt, a parallel remote execution system
Group:      Applications/System
Requires:   %{name}-master = %{version}-%{release}
Requires:   python3-libcloud

%description cloud
The salt-cloud tool provisions new cloud VMs, installs salt-minion on them, and
adds them to the master's collection of controllable minions.
Supports Python 3.


%package    ssh
Summary:    Agentless SSH-based version of Salt, a parallel remote execution system
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}

%description ssh
The salt-ssh tool can run remote execution functions and states without the use
of an agent (salt-minion) service.
Supports Python 3.


%prep
%autosetup -p1
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files salt

# Add some directories
install -d -m 0755 %{buildroot}%{_var}/log/%{name}
touch %{buildroot}%{_var}/log/%{name}/minion
touch %{buildroot}%{_var}/log/%{name}/master
install -d -m 0755 %{buildroot}%{_var}/cache/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/master.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/minion.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/pki
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/pki/master
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/pki/minion
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.conf.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.deploy.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.maps.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.profiles.d
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/cloud.providers.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/proxy.d

# Add the config files
install -p -m 0640 conf/minion %{buildroot}%{_sysconfdir}/%{name}/minion
install -p -m 0640 conf/master %{buildroot}%{_sysconfdir}/%{name}/master
install -p -m 0600 conf/cloud  %{buildroot}%{_sysconfdir}/%{name}/cloud
install -p -m 0640 conf/roster %{buildroot}%{_sysconfdir}/%{name}/roster
install -p -m 0640 conf/proxy  %{buildroot}%{_sysconfdir}/%{name}/proxy

# Add the unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE8} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE9} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/

# Logrotate
install -p %{SOURCE10} .
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -p -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Bash completion
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -p -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}.bash

# Fish completion (TBD remove -v)
mkdir -p %{buildroot}%{fish_dir}
install -p -m 0644  %{SOURCE13} %{buildroot}%{fish_dir}/%{name}.fish
install -p -m 0644  %{SOURCE14} %{buildroot}%{fish_dir}/%{name}_common.fish
install -p -m 0644  %{SOURCE15} %{buildroot}%{fish_dir}/%{name}-call.fish
install -p -m 0644  %{SOURCE16} %{buildroot}%{fish_dir}/%{name}-cp.fish
install -p -m 0644  %{SOURCE17} %{buildroot}%{fish_dir}/%{name}-key.fish
install -p -m 0644  %{SOURCE18} %{buildroot}%{fish_dir}/%{name}-master.fish
install -p -m 0644  %{SOURCE19} %{buildroot}%{fish_dir}/%{name}-minion.fish
install -p -m 0644  %{SOURCE20} %{buildroot}%{fish_dir}/%{name}-run.fish
install -p -m 0644  %{SOURCE21} %{buildroot}%{fish_dir}/%{name}-syndic.fish

# ZSH completion
mkdir -p %{buildroot}%{zsh_dir}
install -p -m 0644 pkg/%{name}.zsh %{buildroot}%{zsh_dir}/_%{name}


%check
%pyproject_check_import -t


%files -f %{pyproject_files}
%license LICENSE
%doc README.fedora
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}.bash
%{_var}/cache/%{name}
%{_var}/log/%{name}
%{_bindir}/spm
%doc %{_mandir}/man1/spm.1*
%dir %{zsh_dir}
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/pki/
%{fish_dir}/%{name}*.fish
%{zsh_dir}/_%{name}

%files master
%doc %{_mandir}/man7/%{name}.7*
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-cp.1*
%doc %{_mandir}/man1/%{name}-key.1*
%doc %{_mandir}/man1/%{name}-master.1*
%doc %{_mandir}/man1/%{name}-run.1*
%{_bindir}/%{name}
%{_bindir}/%{name}-cp
%{_bindir}/%{name}-key
%{_bindir}/%{name}-master
%{_bindir}/%{name}-run
%{_unitdir}/%{name}-master.service
%config(noreplace) %{_sysconfdir}/%{name}/master
%config(noreplace) %{_sysconfdir}/%{name}/master.d
%config(noreplace) %{_sysconfdir}/%{name}/pki/master

%files minion
%doc %{_mandir}/man1/%{name}-call.1*
%doc %{_mandir}/man1/%{name}-minion.1*
%doc %{_mandir}/man1/%{name}-proxy.1*
%{_bindir}/%{name}-minion
%{_bindir}/%{name}-call
%{_bindir}/%{name}-proxy
%{_unitdir}/%{name}-minion.service
%{_unitdir}/%{name}-proxy@.service
%config(noreplace) %{_sysconfdir}/%{name}/minion
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%config(noreplace) %{_sysconfdir}/%{name}/minion.d
%config(noreplace) %{_sysconfdir}/%{name}/pki/minion

%files syndic
%doc %{_mandir}/man1/%{name}-syndic.1*
%{_bindir}/%{name}-syndic
%{_unitdir}/%{name}-syndic.service

%files api
%doc %{_mandir}/man1/%{name}-api.1*
%{_bindir}/%{name}-api
%{_unitdir}/%{name}-api.service

%files cloud
%doc %{_mandir}/man1/%{name}-cloud.1*
%{_bindir}/%{name}-cloud
%{_sysconfdir}/%{name}/cloud.conf.d
%{_sysconfdir}/%{name}/cloud.deploy.d
%{_sysconfdir}/%{name}/cloud.maps.d
%{_sysconfdir}/%{name}/cloud.profiles.d
%{_sysconfdir}/%{name}/cloud.providers.d
%config(noreplace) %{_sysconfdir}/%{name}/cloud

%files ssh
%doc %{_mandir}/man1/%{name}-ssh.1*
%{_bindir}/%{name}-ssh
%config(noreplace) %{_sysconfdir}/%{name}/roster


# assumes systemd for RHEL 7 & 8
%preun master
%systemd_preun %{name}-syndic.service

%preun minion
%systemd_preun %{name}-minion.service

%preun api
%systemd_preun %{name}-api.service

%post master
%systemd_post %{name}-master.service

%post syndic
%systemd_post %{name}-syndic.service

%post minion
%systemd_post %{name}-minion.service

%post api
%systemd_post %{name}-api.service

%postun master
%systemd_postun_with_restart %{name}-master.service

%postun syndic
%systemd_postun_with_restart %{name}-syndic.service

%postun minion
%systemd_postun_with_restart %{name}-minion.service

%postun api
%systemd_postun_with_restart %{name}-api.service


%changelog
* Tue Oct 04 2022 Salt Project Packaging <saltproject-packaging@vmware.com> - %{version}-1
- Update to feature release %{version}-1 for Python 3

* Thu Aug 25 2022 Salt Project Packaging <saltproject-packaging@vmware.com> - 3005-1
- Update to feature release 3005-1 for Python 3

* Thu Jul 28 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 3004.2-3
- Cleaned up specfile

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3004.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Salt Project Packaging <saltproject-packaging@vmware.com> - 3004.2-1
- Update to CVE release 3004.2-1 for Python 3

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3004.1-2
- Rebuilt for Python 3.11

* Mon Mar 28 2022 Salt Project Packaging <saltproject-packaging@vmware.com> - 3004.1-1
- Update to CVE release 3004.1-1 for Python 3

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Salt Project Packaging <saltproject-packaging@vmware.com> - 3004-1
- Update to feature release 3004-1 for Python 3

* Wed Sep 08 2021 SaltStack Packaging Team <saltproject-packaging@vmware.com> - 3003.3-1
- Update to CVE release 3003.3-1 https://saltproject.io/security_announcements/salt-security-advisory-2021-sep-02/

* Thu Aug 12 2021 SaltStack Packaging Team <packaging@saltstack.com> - 3003.2-1
- Update to bugfix release 3003.2-1 for Python 3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3003.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 SaltStack Packaging Team <packaging@saltstack.com> - 3003.1-1
- Update to bugfix release 3003.1-1 for Python 3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3003-2
- Rebuilt for Python 3.10

* Mon Apr 26 2021 SaltStack Packaging Team <packaging@saltstack.com> - 3003-1
- Update to feature release 3003-1 for Python 3

* Fri Mar 26 2021 SaltStack Packaging Team <packaging@saltstack.com> - 3002.6-1
- Update to bugfix release 3002.6-1 for Python 3

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3002.5-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Fri Feb 26 2021 SaltStack Packaging Team <packaging@saltstack.com> - 3002.5-1
- Update to CVE release 3002.5-1 for Python 3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3002.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 SaltStack Packaging Team <packaging@saltstack.com> - 3002.2-1
- Update to bugfix release 3002.2-1 for Python3
- Revert _scope_id patch since it's been fixed upstream

* Wed Nov 04 2020 SaltStack Packaging Team <packaging@saltstack.com> - 3002.1-1
- Update to CVE release 3002.1-1 for Python3

* Sun Oct 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 3002-1
- 3002
- Patch for _scope_id 3.9 error.

* Mon Jul 27 2020 SaltStack Packaging Team <packaging@saltstack.com> - 3001.1-1
- Update to feature release 3001.1-1  for Python 3

* Thu Jun 18 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 30001-1
- Update to feature release 30001-1 for Python 3

* Wed Jun 03 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3001rc1-2
- Altered msgpack and python-zmq versions limitation

* Tue Jun 02 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3001rc1-1
- Update to Release Candidate rc1 for point release 3001

* Fri May 15 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000.3-1
- Update to feature release 3000.3-1  for Python 3

* Wed Apr 29 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000.2-1
- Update to feature release 3000.2-1  for Python 3

* Wed Apr 01 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000.1-1
- Update to feature release 3000.1-1  for Python 3

* Tue Feb 25 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000-5
- Fix lint clean up issues

* Tue Feb 25 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000-4
- Removed cherrypy < 18.0.0 check since python 3.5 no longer used on Fedora

* Mon Feb 24 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000-3
- Added distro as a build and requires dependency for Fedora >= 31

* Mon Feb 24 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000-2
- Changed dependency for crypto to pycryptodomex

* Mon Feb 03 2020 SaltStack Packaging Team <packaging@saltstack.com.com> - 3000-1
- Update to feature release 3000-1  for Python 3
- Removed Torando since salt.ext.tornado, add dependencies for Tornado

* Wed Jan 22 2020 SaltStack Packaging Team <packaging@saltstack.com> - 3000.0.0rc2-1
- Update to Neon Release Candidate 2 for Python 3
- Updated spec file to not use py3_build  due to '-s' preventing pip installs
- Updated patch file to support Tornado4

* Wed Jan 08 2020 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.3-1
- Update to feature release 2019.2.3-1  for Python 3

* Tue Oct 15 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.2-1
- Update to feature release 2019.2.2-1  for Python 3

* Thu Sep 12 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.1-1
- Update to feature release 2019.2.1-1  for Python 3

* Tue Sep 10 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-10
- Support for point release, added distro as a requirement

* Tue Jul 02 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-9
- Support for point release, only rpmsign and tornado4 patches

* Thu Jun 06 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-8
- Support for Redhat 7 need for PyYAML and tornado 4 patch since Tornado < v5.x

* Thu May 23 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-7
- Patching in support for gpg-agent and passphrase preset

* Wed May 22 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-6
- Patching in fix for rpmsign

* Thu May 16 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-5
- Patching in fix for gpg str/bytes to to_unicode/to_bytes

* Tue May 14 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-4
- Patching in support for Tornado 4

* Mon May 13 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-3
- Added support for Redhat 8, and removed support for Python 2 packages

* Mon Apr 08 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-2
- Update to support Python 3.6

* Mon Apr 08 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.4-2
- Update to allow for Python 3.6

* Mon Mar 04 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2.0-1
- Update to feature release 2019.2.0-1 for Python 2

* Sat Feb 16 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-1
- Update to feature release 2019.2.0-1  for Python 3

* Sat Feb 16 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.4-1
- Update to feature release 2018.3.4-1  for Python 3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 SaltStack Packaging Team <packaging@saltstack.com> - 2019.2.0-0
- Update to feature release branch 2019.2.0-0 for Python 2
- Revised acceptable versions of cherrypy, futures

* Thu Nov 29 2018 SaltStack Packaging Team <packaging@Ch3LL.com> - 2018.3.3-2
- Revised BuildRequires and Requires to use python2 versions of packages
- Cleaned up spec file to apply to Fedora 28 and above

* Mon Oct 15 2018 SaltStack Packaging Team <packaging@Ch3LL.com> - 2018.3.3-1
- Update to feature release 2018.3.3-1 for Python 2
- Revised versions of cherrypy acceptable

* Tue Oct 09 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.3-1
- Update to feature release 2018.3.3-1  for Python 3
- Revised versions of cherrypy acceptable

* Tue Jul 24 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.2-5
- Fix version of python used, multiple addition of 2.7 

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.2-3
- Allow for removal of /usr/bin/python

* Mon Jul 09 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.2-2
- Correct tornado version check

* Thu Jun 21 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.2-1
- Update to feature release 2018.3.2-1  for Python 2

* Mon Jun 11 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.1-1
- Update to feature release 2018.3.1-1  for Python 3
- Revised minimum msgpack version >= 0.4

* Fri Jun 08 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.1-1
- Update to feature release 2018.3.1-1  for Python 2
- Revised minimum msgpack version >= 0.4

* Mon Apr 02 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.0-1
- Development build for Python 3 support

* Fri Mar 30 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2018.3.0-1
- Update to feature release 2018.3.0-1

* Tue Mar 27 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2017.7.5-1
- Update to feature release 2017.7.5-1

* Fri Feb 16 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2017.7.4-1
- Update to feature release 2017.7.4-1
- Limit to Tornado use to between versions 4.2.1 and less than 5.0

* Tue Jan 30 2018 SaltStack Packaging Team <packaging@Ch3LL.com> - 2017.7.3-1
- Update to feature release 2017.7.3-1

* Mon Sep 18 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2017.7.2-1
- Update to feature release 2017.7.2

* Tue Aug 15 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2017.7.1-1
- Update to feature release 2017.7.1
- Altered dependency for dnf-utils instead of yum-utils if Fedora 26 or greater

* Wed Jul 12 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2017.7.0-1
- Update to feature release 2017.7.0
- Added python-psutil as a requirement, disabled auto enable for Redhat 6

* Thu Jun 22 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.6-1
- Update to feature release 2016.11.6

* Thu Apr 27 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.5-1
- Update to feature release 2016.11.5
- Altered to use pycryptodomex if 64 bit and Redhat 6 and greater otherwise pycrypto
- Addition of salt-proxy@.service

* Wed Apr 19 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.4-1
- Update to feature release 2016.11.4 and use of pycryptodomex

* Mon Mar 20 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.3-2
- Updated to allow for pre and post processing for salt-syndic and salt-api

* Wed Feb 22 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.3-1
- Update to feature release 2016.11.3

* Tue Jan 17 2017 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.2-1
- Update to feature release 2016.11.2

* Tue Dec 13 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.1-1
- Update to feature release 2016.11.1

* Wed Nov 30 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.0-2
- Adjust for single spec for Redhat family and fish-completions

* Tue Nov 22 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.0-1
- Update to feature release 2016.11.0

* Wed Nov  2 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.0-0.rc2
- Update to feature release 2016.11.0 Release Candidate 2

* Wed Oct 26 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.11.0-0.rc1
- Update to feature release 2016.11.0 Release Candidate 1

* Fri Oct 14 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.3-4
- Ported to build on Amazon Linux 2016.09 natively

* Mon Sep 12 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.3-3
- Adjust spec file for Fedora 24 support

* Tue Aug 30 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.3-2
- Fix systemd update of existing installation

* Fri Aug 26 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.3-1
- Update to feature release 2016.3.3

* Fri Jul 29 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.2-1
- Update to feature release 2016.3.2

* Fri Jun 10 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.1-1
- Update to feature release 2016.3.1

* Mon May 23 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.0-1
- Update to feature release 2016.3.0

* Wed Apr  6 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2016.3.0-rc2
- Update to bugfix release 2016.3.0 Release Candidate 2

* Fri Mar 25 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.8-2
- Patched fixes 32129, 32023, 32117

* Wed Mar 16 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.8-1
- Update to bugfix release 2015.8.8

* Tue Feb 16 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.7-1
- Update to bugfix release 2015.8.7

* Mon Jan 25 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.4-1
- Update to bugfix release 2015.8.4

* Thu Jan 14 2016 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.3-3
- Add systemd environment files

* Mon Dec  7 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.3-2
- Additional salt configuration directories on install

* Tue Dec  1 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.3-1
- Update to bugfix release 2015.8.3

* Fri Nov 13 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.2-1
- Update to bugfix release 2015.8.2

* Fri Oct 30 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.1-2
- Update for pre-install direcories

* Wed Oct  7 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.1-1
- Update to feature release 2015.8.1

* Wed Sep 30 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.0-3
- Update include python-uinttest2

* Wed Sep  9 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.0-2
- Update include testing

* Fri Sep  4 2015 SaltStack Packaging Team <packaging@saltstack.com> - 2015.8.0-1
- Update to feature release 2015.8.0

* Fri Jul 10 2015 Erik Johnson <erik@saltstack.com> - 2015.5.3-4
- Patch tests

* Fri Jul 10 2015 Erik Johnson <erik@saltstack.com> - 2015.5.3-3
- Patch init grain

* Fri Jul 10 2015 Erik Johnson <erik@saltstack.com> - 2015.5.3-2
- Update to bugfix release 2015.5.3, add bash completion

* Thu Jun  4 2015 Erik Johnson <erik@saltstack.com> - 2015.5.2-3
- Mark salt-ssh roster as a config file to prevent replacement

* Thu Jun  4 2015 Erik Johnson <erik@saltstack.com> - 2015.5.2-2
- Update skipped tests

* Thu Jun  4 2015 Erik Johnson <erik@saltstack.com> - 2015.5.2-1
- Update to bugfix release 2015.5.2

* Mon Jun  1 2015 Erik Johnson <erik@saltstack.com> - 2015.5.1-2
- Add missing dependency on which (RH #1226636)

* Wed May 27 2015 Erik Johnson <erik@saltstack.com> - 2015.5.1-1
- Update to bugfix release 2015.5.1

* Mon May 11 2015 Erik Johnson <erik@saltstack.com> - 2015.5.0-1
- Update to feature release 2015.5.0

* Fri Apr 17 2015 Erik Johnson <erik@saltstack.com> - 2014.7.5-1
- Update to bugfix release 2014.7.5

* Tue Apr  7 2015 Erik Johnson <erik@saltstack.com> - 2014.7.4-4
- Fix RH bug #1210316 and Salt bug #22003

* Tue Apr  7 2015 Erik Johnson <erik@saltstack.com> - 2014.7.4-2
- Update to bugfix release 2014.7.4

* Tue Feb 17 2015 Erik Johnson <erik@saltstack.com> - 2014.7.2-1
- Update to bugfix release 2014.7.2

* Mon Jan 19 2015 Erik Johnson <erik@saltstack.com> - 2014.7.1-1
- Update to bugfix release 2014.7.1

* Fri Nov  7 2014 Erik Johnson <erik@saltstack.com> - 2014.7.0-3
- Make salt-api its own package

* Thu Nov  6 2014 Erik Johnson <erik@saltstack.com> - 2014.7.0-2
- Fix changelog

* Thu Nov  6 2014 Erik Johnson <erik@saltstack.com> - 2014.7.0-1
- Update to feature release 2014.7.0

* Fri Oct 17 2014 Erik Johnson <erik@saltstack.com> - 2014.1.13-1
- Update to bugfix release 2014.1.13

* Mon Sep 29 2014 Erik Johnson <erik@saltstack.com> - 2014.1.11-1
- Update to bugfix release 2014.1.11

* Sun Aug 10 2014 Erik Johnson <erik@saltstack.com> - 2014.1.10-4
- Fix incorrect conditional

* Tue Aug  5 2014 Erik Johnson <erik@saltstack.com> - 2014.1.10-2
- Deploy cachedir with package

* Mon Aug  4 2014 Erik Johnson <erik@saltstack.com> - 2014.1.10-1
- Update to bugfix release 2014.1.10

* Thu Jul 10 2014 Erik Johnson <erik@saltstack.com> - 2014.1.7-3
- Add logrotate script

* Thu Jul 10 2014 Erik Johnson <erik@saltstack.com> - 2014.1.7-1
- Update to bugfix release 2014.1.7

* Wed Jun 11 2014 Erik Johnson <erik@saltstack.com> - 2014.1.5-1
- Update to bugfix release 2014.1.5

* Tue May  6 2014 Erik Johnson <erik@saltstack.com> - 2014.1.4-1
- Update to bugfix release 2014.1.4

* Thu Feb 20 2014 Erik Johnson <erik@saltstack.com> - 2014.1.0-1
- Update to feature release 2014.1.0

* Mon Jan 27 2014 Erik Johnson <erik@saltstack.com> - 0.17.5-1
- Update to bugfix release 0.17.5

* Thu Dec 19 2013 Erik Johnson <erik@saltstack.com> - 0.17.4-1
- Update to bugfix release 0.17.4

* Tue Nov 19 2013 Erik Johnson <erik@saltstack.com> - 0.17.2-2
- Patched to fix pkgrepo.managed regression

* Mon Nov 18 2013 Erik Johnson <erik@saltstack.com> - 0.17.2-1
- Update to bugfix release 0.17.2

* Thu Oct 17 2013 Erik Johnson <erik@saltstack.com> - 0.17.1-1
- Update to bugfix release 0.17.1

* Thu Sep 26 2013 Erik Johnson <erik@saltstack.com> - 0.17.0-1
- Update to feature release 0.17.0

* Wed Sep 11 2013 David Anderson <dave@dubkat.com>
- Change sourcing order of init functions and salt default file

* Sat Sep 07 2013 Erik Johnson <erik@saltstack.com> - 0.16.4-1
- Update to patch release 0.16.4

* Sun Aug 25 2013 Florian La Roche <Florian.LaRoche@gmx.net>
- fixed preun/postun scripts for salt-minion

* Thu Aug 15 2013 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 0.16.3-1
- Update to patch release 0.16.3

* Thu Aug 8 2013 Clint Savage <herlo1@gmail.com> - 0.16.2-1
- Update to patch release 0.16.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 9 2013 Clint Savage <herlo1@gmail.com> - 0.16.0-1
- Update to feature release 0.16.0

* Sat Jun 1 2013 Clint Savage <herlo1@gmail.com> - 0.15.3-1
- Update to patch release 0.15.3
- Removed OrderedDict patch

* Fri May 31 2013 Clint Savage <herlo1@gmail.com> - 0.15.2-1
- Update to patch release 0.15.2
- Patch OrderedDict for failed tests (SaltStack#4912)

* Wed May 8 2013 Clint Savage <herlo1@gmail.com> - 0.15.1-1
- Update to patch release 0.15.1

* Sat May 4 2013 Clint Savage <herlo1@gmail.com> - 0.15.0-1
- Update to upstream feature release 0.15.0

* Fri Apr 19 2013 Clint Savage <herlo1@gmail.com> - 0.14.1-1
- Update to upstream patch release 0.14.1

* Sat Mar 23 2013 Clint Savage <herlo1@gmail.com> - 0.14.0-1
- Update to upstream feature release 0.14.0

* Fri Mar 22 2013 Clint Savage <herlo1@gmail.com> - 0.13.3-1
- Update to upstream patch release 0.13.3

* Wed Mar 13 2013 Clint Savage <herlo1@gmail.com> - 0.13.2-1
- Update to upstream patch release 0.13.2

* Fri Feb 15 2013 Clint Savage <herlo1@gmail.com> - 0.13.1-1
- Update to upstream patch release 0.13.1
- Add unittest support

* Sat Feb 02 2013 Clint Savage <herlo1@gmail.com> - 0.12.1-1
- Remove patches and update to upstream patch release 0.12.1

* Thu Jan 17 2013 Wendall Cada <wendallc@83864.com> - 0.12.0-2
- Added unittest support

* Wed Jan 16 2013 Clint Savage <herlo1@gmail.com> - 0.12.0-1
- Upstream release 0.12.0

* Fri Dec 14 2012 Clint Savage <herlo1@gmail.com> - 0.11.1-1
- Upstream patch release 0.11.1
- Fixes security vulnerability (https://github.com/saltstack/salt/issues/2916)

* Fri Dec 14 2012 Clint Savage <herlo1@gmail.com> - 0.11.0-1
- Moved to upstream release 0.11.0

* Wed Dec 05 2012 Mike Chesnut <mchesnut@gmail.com> - 0.10.5-2
- moved to upstream release 0.10.5
- removing references to minion.template and master.template, as those files
  have been removed from the repo

* Sun Nov 18 2012 Clint Savage <herlo1@gmail.com> - 0.10.5-1
- Moved to upstream release 0.10.5
- Added pciutils as Requires

* Wed Oct 24 2012 Clint Savage <herlo1@gmail.com> - 0.10.4-1
- Moved to upstream release 0.10.4
- Patched jcollie/systemd-service-status (SALT@GH#2335) (RHBZ#869669)

* Tue Oct 2 2012 Clint Savage <herlo1@gmail.com> - 0.10.3-1
- Moved to upstream release 0.10.3
- Added systemd scriplets (RHBZ#850408)

* Thu Aug 2 2012 Clint Savage <herlo1@gmail.com> - 0.10.2-2
- Fix upstream bug #1730 per RHBZ#845295

* Tue Jul 31 2012 Clint Savage <herlo1@gmail.com> - 0.10.2-1
- Moved to upstream release 0.10.2
- Removed PyXML as a dependency

* Sat Jun 16 2012 Clint Savage <herlo1@gmail.com> - 0.10.1-1
- Moved to upstream release 0.10.1

* Sat Apr 28 2012 Clint Savage <herlo1@gmail.com> - 0.9.9.1-1
- Moved to upstream release 0.9.9.1

* Tue Apr 17 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.8-2
- dmidecode is x86 only

* Wed Mar 21 2012 Clint Savage <herlo1@gmail.com> - 0.9.8-1
- Moved to upstream release 0.9.8

* Thu Mar 8 2012 Clint Savage <herlo1@gmail.com> - 0.9.7-2
- Added dmidecode as a Requires

* Thu Feb 16 2012 Clint Savage <herlo1@gmail.com> - 0.9.7-1
- Moved to upstream release 0.9.7

* Tue Jan 24 2012 Clint Savage <herlo1@gmail.com> - 0.9.6-2
- Added README.fedora and removed deps for optional modules

* Sat Jan 21 2012 Clint Savage <herlo1@gmail.com> - 0.9.6-1
- New upstream release

* Sun Jan 8 2012 Clint Savage <herlo1@gmail.com> - 0.9.4-6
- Missed some critical elements for SysV and rpmlint cleanup

* Sun Jan 8 2012 Clint Savage <herlo1@gmail.com> - 0.9.4-5
- SysV clean up in post

* Sat Jan 7 2012 Clint Savage <herlo1@gmail.com> - 0.9.4-4
- Cleaning up perms, group and descriptions, adding post scripts for systemd

* Thu Jan 5 2012 Clint Savage <herlo1@gmail.com> - 0.9.4-3
- Updating for systemd on Fedora 15+

* Thu Dec 1 2011 Clint Savage <herlo1@gmail.com> - 0.9.4-2
- Removing requirement for Cython. Optional only for salt-minion

* Wed Nov 30 2011 Clint Savage <herlo1@gmail.com> - 0.9.4-1
- New upstream release with new features and bugfixes

* Thu Nov 17 2011 Clint Savage <herlo1@gmail.com> - 0.9.3-1
- New upstream release with new features and bugfixes

* Sat Sep 17 2011 Clint Savage <herlo1@gmail.com> - 0.9.2-1
- Bugfix release from upstream to fix python2.6 issues

* Fri Sep 09 2011 Clint Savage <herlo1@gmail.com> - 0.9.1-1
- Initial packages
