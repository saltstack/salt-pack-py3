%global srcname pyroute2

%bcond_with python2
%bcond_without python3
%bcond_with tests

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name: python-%{srcname}
Version: 0.5.3
Release: 4%{?dist}
Summary: Pure Python netlink library
License: GPLv2+
URL: https://github.com/svinota/%{srcname}

BuildArch: noarch
Source: https://pypi.io/packages/source/p/pyroute2/pyroute2-%{version}.tar.gz


%description
PyRoute2 provides several levels of API to work with Netlink
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,
IPQ.

%if %{with python2}
%package -n python2-%{srcname}
Summary: %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
%endif
BuildRequires: python2-devel
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
PyRoute2 provides several levels of API to work with Netlink
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,
IPQ.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary: %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python%{python3_pkgversion}-rpm-macros
%endif
BuildRequires: python%{python3_pkgversion}-devel
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
PyRoute2 provides several levels of API to work with Netlink
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,
IPQ.
%endif


%prep
%setup -q -n %{srcname}-%{version}

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

%if %{with python2}
%files -n python2-%{srcname}
%if %{without python3}
%{_bindir}/ss2
%endif
%doc README* LICENSE.GPL.v2 LICENSE.Apache.v2
%{python2_sitelib}/%{srcname}*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%{_bindir}/ss2
%doc README* LICENSE.GPL.v2 LICENSE.Apache.v2
%{python3_sitelib}/%{srcname}*
%endif

%changelog
* Thu Jun 13 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.5.3-4
- Added support for Amazon Linux 2 Python 3

* Wed Feb 06 2019 Alfredo Moralejo <amoralej@redhat.com> - 0.5.3-3
- Fix build in CentOS7.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Slawek Kaplonski <skaplons@redhat.com> 0.5.3-1
- Update to 0.5.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.7

* Thu Jun 21 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.5.2-1
- Upstream 0.5.2 (includes previous deprecated async arg patch)

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.21-3
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.21-2
- Conditionalize the Python 2 subpackage
- Don't build the Python 2 subpackage on EL > 7

* Fri Feb 9 2018 amoralej <amoralej@redhat.com> - 0.4.21-1
- Upstream 0.4.21

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 hguemar <hguemar@benihime.seireitei> - 0.4.19-1
- Upstream 0.4.19

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun  1 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4.15-1
- Upstream 0.4.15
- req: #365 -- full and short nla notation fixed, critical
- iproute: #364 -- new method, brport()
- ipdb: -- support bridge port options

* Tue Mar  7 2017 Antoni S. Puimedon <antonisp@celebdor.com> 0.4.13-1
- upgrade to 0.4.13
- ipset hash:mac support
- ipset: hash:mac support
- ipset: list:set support
- ifinfmsg: allow absolute/relative paths in the net_ns_fd NLA
- ipdb: #322 -- IPv6 updates on interfaces in DOWN state
- rtnl: #284 -- support vlan_flags
- ipdb: #307 -- fix IPv6 routes management
- ipdb: #311 -- vlan interfaces address loading
- iprsocket: #305 -- support NETLINK_LISTEN_ALL_NSID

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.10-2
- Rebuild for Python 3.6

* Fri Oct 14 2016 Peter V. Saveliev <peter@svinota.eu> 0.4.10-1
- devlink fd leak fix

* Thu Oct  6 2016 Peter V. Saveliev <peter@svinota.eu> 0.4.9-1
- critical fd leak fix
- initial NETLINK_SOCK_DIAG support

* Tue Sep 27 2016 Peter V. Saveliev <peter@svinota.eu> 0.4.8-1
- uplift to 0.4.x

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.19-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr  5 2016 Peter V. Saveliev <peter@svinota.eu> 0.3.19-1
- separate Python2 and Python3 packages
- MPLS lwtunnel support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2

- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Fri Nov 20 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.15-1
- critical NetNS fd leak fix

* Tue Sep  1 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.14-1
- bogus rpm dates in the changelog are fixed
- both licenses added

* Tue Sep  1 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.13-1
- BPF filters support
- MPLS routes support
- MIPS platform support
- multiple improvements on iwutil
- memory consumption improvements

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan  8 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.4-1
- Network namespaces support
- Veth, tuntap
- Route metrics

* Fri Dec  5 2014 Peter V. Saveliev <peter@svinota.eu> 0.3.3-1
- Fix-ups, 0.3.3
- Bugfixes for Python 2.6

* Tue Nov 18 2014 Peter V. Saveliev <peter@svinota.eu> 0.3.2-1
- Update to 0.3.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Jiri Pirko <jpirko@redhat.com> - 0.2.7-1
- Update to 0.2.7

* Thu Aug 22 2013 Peter V. Saveliev <peet@redhat.com> 0.1.11-1
- IPRSocket threadless objects
- rtnl: tc filters improvements

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Peter V. Saveliev <peet@redhat.com> 0.1.10-1
- fd and threads leaks fixed
- shutdown sequence fixed (release() calls)
- ipdb: interface removal
- ipdb: fail on transaction sync timeout

* Tue Jun 11 2013 Peter V. Saveliev <peet@redhat.com> 0.1.9-2
- fedpkg import fix

* Tue Jun 11 2013 Peter V. Saveliev <peet@redhat.com> 0.1.9-1
- several races fixed
- Python 2.6 compatibility issues fixed

* Wed Jun 05 2013 Peter V. Saveliev <peet@redhat.com> 0.1.8-1
- initial RH build

