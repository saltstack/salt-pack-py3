# build against xz?
%bcond_without xz
# just for giggles, option to build with internal Berkeley DB
%bcond_with int_bdb
# disable plugins initially
%bcond_with plugins

%global rpmver 4.11.3
%global rpmrel 43
%global srcver %{rpmver}

%global bdbname libdb
%global bdbver 5.3.15
%global dbprefix db

Summary: Python 3 bindings for apps which will manipulate RPM packages
Name: python3-rpm
Version: %{rpmver}
Release: 8%{?dist}
Url: http://www.rpm.org/
Source0: http://ftp.rpm.org/releases/rpm-4.11.x/rpm-%{srcver}.tar.bz2
%if %{with int_bdb}
Source1: db-%{bdbver}.tar.gz
%else
BuildRequires: libdb-devel
%endif

# Fedora specspo is setup differently than what rpm expects, considering
# this as Fedora-specific patch for now
Patch2: rpm-4.9.90-fedora-specspo.patch
# In current Fedora, man-pages pkg owns all the localized man directories
Patch3: rpm-4.9.90-no-man-dirs.patch
# gnupg2 comes installed by default, avoid need to drag in gnupg too
Patch4: rpm-4.8.1-use-gpg2.patch
Patch5: rpm-4.9.90-armhfp.patch
#conditionally applied patch for arm hardware floating point
Patch6: rpm-4.9.0-armhfp-logic.patch

# Patches already in upstream
Patch108: rpm-4.11.1-libtool-ppc64le.patch

# Patches already in upstream but not in 4.11.x branch
Patch150: rpm-4.11.x-dirlink-verify.patch
Patch151: rpm-4.11.x-defattr-permissions.patch
Patch152: rpm-4.8.x-error-in-log.patch
Patch153: rpm-4.11.x-setperms-setugids-mutual-exclusion.patch
Patch154: rpm-4.8.0-ignore-multiline2.patch
Patch155: rpm-4.11.x-deprecate-addsign.patch
Patch156: rpm-4.11.x-Add-make_build-macro.patch
Patch157: rpm-4.11.x-color-skipping.patch
Patch158: rpm-4.11.x-fix-stripping-of-binaries.patch
Patch159: rpm-4.11.x-fix-debuginfo-creation.patch
Patch160: rpm-4.11.x-systemd-inhibit.patch
Patch161: rpm-4.11.x-parametrized-macro-invocations.patch
Patch162: rpm-4.11.x-broken-pipe.patch
# Belongs to Patch 161
Patch163: rpm-4.11.x-Handle-line-continuation.patch
# Belongs to Patch 160
Patch164: rpm-4.11.3-Initialize-plugins-based-on-DSO-discovery.patch
Patch166: rpm-4.11.x-move-rename.patch
Patch167: rpm-4.11.x-bdb-warings.patch
Patch168: rpm-4.14.x-Add-justdb-to-the-erase-man.patch
Patch169: rpm-4.11.x-multitheaded_xz.patch
Patch170: rpm-4.11.x-perl.req-1.patch
Patch171: rpm-4.11.x-perl.req-2.patch
Patch172: rpm-4.11.x-perl.req-3.patch
Patch173: rpm-4.11.x-perl.req-4.patch
Patch174: rpm-4.11.x-define-PY_SSIZE_T_CLEAN.patch
Patch175: rpm-4.11.x-python-binding-test-case.patch
Patch176: rpm-4.11.x-Add-noplugins.patch
Patch177: rpm-4.11.x-no-longer-config.patch
Patch178: rpm-4.11.x-Fix-off-by-one-base64.patch
Patch179: rpm-4.11.x-sources-to-lua-variables.patch
Patch180: rpm-4.11.x-Fix-Python-hdr-refcount.patch
Patch181: rpm-4.11.x-perl.req-skip-my-var-block.patch
Patch182: rpm-4.11.x-verify-data-range.patch
Patch183: rpm-4.13.x-writable-tmp-dir.patch
Patch184: rpm-4.13.x-increase_header_size.patch
Patch185: rpm-4.13.x-Make-the-stftime-buffer-big-enuff.patch
Patch186: rpm-4.11.x-skipattr.patch
Patch187: rpm-4.13.x-Implement-noconfig-query.patch
Patch188: rpm-4.11.x-weakdep-tags.patch
Patch189: rpm-4.12.x-rpmSign-return-value-correction.patch
Patch190: rpm-4.13.x-fix_find_debuginfo_opts_g.patch
Patch191: rpm-4.13.x-enable_noghost_option.patch
Patch192: rpm-4.11.x-provide-audit-events.patch
Patch193: rpm-4.11.x-setcaps.patch
Patch194: rpm-4.11.x-disk-space-calculation.patch
Patch195: rpm-4.11.x-remove-perl-provides-from-requires.patch
Patch196: rpm-4.13.x-bad-owner-group.patch
Patch197: rpm-4.11.x-perl.req-6.patch
Patch198: rpm-4.13.x-fix-segfault-on-fingerprint-symlink.patch
Patch199: rpm-4.11.x-dependson.patch

# Filter soname dependencies by name
Patch200: rpm-4.11.x-filter-soname-deps.patch
Patch201: rpm-4.11.x-do-not-filter-ld64.patch

# These are not yet upstream
Patch301: rpm-4.6.0-niagara.patch
Patch302: rpm-4.7.1-geode-i686.patch
# Probably to be upstreamed in slightly different form
Patch304: rpm-4.9.1.1-ld-flags.patch
# Compressed debuginfo support (#833311)
Patch305: rpm-4.10.0-dwz-debuginfo.patch
# Minidebuginfo support (#834073)
Patch306: rpm-4.10.0-minidebuginfo.patch
# Fix CRC32 after dwz (#971119)
Patch307: rpm-4.11.1-sepdebugcrcfix.patch
# Fix minidebuginfo on ppc64 (#1052415)
Patch308: rpm-4.11.x-minidebuginfo-ppc64.patch
# Chmod 000 for files being unpacked
Patch309: rpm-4.11.x-chmod.patch
Patch310: rpm-4.11.x-CVE-2014-8118.patch
Patch311: rpm-4.11.3-update-config.guess.patch
Patch312: rpm-4.11.x-man-systemd-inhibit.patch
Patch313: rpm-4.11.x-quiet-signing.patch
Patch314: rpm-4.11.x-export-verifysigs-to-python.patch


# Temporary Patch to provide support for updates
Patch400: rpm-4.10.90-rpmlib-filesystem-check.patch
# Disable plugins
Patch401: rpm-4.11.3-disable-collection-plugins.patch
# Remove EVR check
Patch402: rpm-4.11.3-EVR-validity-check.patch

# Backport of RPMCALLBACK_ELEM_PROGRESS
# https://bugzilla.redhat.com/show_bug.cgi?id=1466649
Patch501: rpm-4.11.x-elem-progress.patch
# Make header to be available for RPMCALLBACK_ELEM_PROGRESS
Patch502: rpm-4.13.x-RPMCALLBACK_ELEM_PROGRESS-available-header.patch
# Backport of reinstall functionality from 4.12
# https://bugzilla.redhat.com/show_bug.cgi?id=1466650
Patch503: rpm-4.11.x-reinstall.patch
Patch504: rpm-4.11.x-add-g-libs.patch

# Fix brp-python-bytecompile script to work with Python 3 packages
# https://bugzilla.redhat.com/show_bug.cgi?id=1691402
# Fixed upstream:
# https://github.com/rpm-software-management/rpm/commit/a8e51b3bb05c6acb1d9b2e3d34f859ddda1677be
Patch505: rpm-4.11.3-brp-python-bytecompile-Fix-when-default-python-is-no.patch
Patch506: rpm-4.11.x-correct-g-libs.patch

# EPEL7 package specific patches
# python: remove redundant suffix in python module name in metadata
Patch701: rpm-4.14.x-python-package-name.patch
Patch702: rpm-4.12.0-Fix-Python3-import.patch

# Partially GPL/LGPL dual-licensed and some bits with BSD
# SourceLicense: (GPLv2+ and LGPLv2+ with exceptions) and BSD 
License: GPLv2+

%if %{without int_bdb}
BuildRequires: %{bdbname}-devel%{_isa}
%endif

# XXX generally assumed to be installed but make it explicit as rpm
# is a bit special...
BuildRequires: redhat-rpm-config
BuildRequires: gawk
BuildRequires: elfutils-devel >= 0.112
BuildRequires: elfutils-libelf-devel
BuildRequires: readline-devel zlib-devel
BuildRequires: nss-devel
BuildRequires: nss-softokn-freebl-devel
# The popt version here just documents an older known-good version
BuildRequires: popt-devel >= 1.10.2
BuildRequires: file-devel
BuildRequires: gettext-devel
BuildRequires: libselinux-devel
# XXX semanage is only used by sepolicy plugin but configure requires it...
BuildRequires: libsemanage-devel
BuildRequires: ncurses-devel
BuildRequires: bzip2-devel >= 0.9.0c-2
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: lua-devel >= 5.1
BuildRequires: libcap-devel
BuildRequires: libacl-devel
%if ! %{without xz}
BuildRequires: xz-devel >= 4.999.8
%endif
BuildRequires: audit-libs-devel

# Only required by sepdebugcrcfix patch
BuildRequires: binutils-devel
# Couple of patches change makefiles so, require for now...
BuildRequires: automake libtool

%description
The python3-rpm package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python 3
programs that will manipulate RPM packages and databases.

%package -n python%{python3_pkgversion}-rpm
Summary: %{summary}
Requires: rpm = %{rpmver}
Requires: rpm >= %{rpmver}-%{rpmrel}
%{?python_provide:%python_provide python%{python3_pkgversion}-rpm}

%description -n python%{python3_pkgversion}-rpm
The python%{python3_pkgversion}-rpm package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python %{python3_version}
programs that will manipulate RPM packages and databases.

%prep
%setup -q -n rpm-%{srcver} %{?with_int_bdb:-a 1}
%patch2 -p1 -b .fedora-specspo
%patch3 -p1 -b .no-man-dirs
%patch4 -p1 -b .use-gpg2

%ifarch ppc64le
%patch108 -p2 -b .ppc64le
%endif

%patch150 -p1 -b .dirlink-verify
%patch151 -p1 -b .defattr-permissions
%patch152 -p1 -b .error-in-log
%patch153 -p1 -b .setperms-setugids
%patch154 -p1 -b .ignore-multiline2
%patch155 -p1 -b .deprecate-addsign
%patch156 -p1 -b .make-build
%patch157 -p1 -b .skip-color
%patch158 -p1 -b .strip-binaries
%patch159 -p1 -b .debuginfo
%patch160 -p1 -b .systemd-inihibit
%patch161 -p1 -b .macro-expansion
%patch162 -p1 -b .broken-pipe
%patch163 -p1 -b .line-continuation
%patch164 -p1 -b .plugin-detection
%patch166 -p1 -b .move-rename
%patch167 -p1 -b .bdb-warnings
%patch168 -p1 -b .justdb-man
%patch169 -p1 -b .mt_xz
%patch170 -p1 -b .perl.req1
%patch171 -p1 -b .perl.req2
%patch172 -p1 -b .perl.req3
%patch173 -p1 -b .perl.req4
%patch174 -p1 -b .py_size
%patch175 -p1 -b .py_size_test
%patch176 -p1 -b .noplugins
%patch177 -p1 -b .noconfig
%patch178 -p1 -b .offbyone
%patch179 -p1 -b .sourceslua
%patch180 -p1 -b .hdrrefcnt
%patch181 -p1 -b .perlblock
%patch182 -p1 -b .verifysignature
%patch183 -p1 -b .writable_tmp
%patch184 -p1 -b .hdr_size
%patch185 -p1 -b .strtime
%patch186 -p1 -b .skipattr
%patch187 -p1 -b .noconfig-cli
%patch188 -p1 -b .weakdep-tags
%patch189 -p1 -b .rpmsign-error
%patch190 -p1 -b .find_debuginfo_opts
%patch191 -p1 -b .noghost
%patch192 -p1 -b .audit-events
%patch193 -p1 -b .setcaps
%patch194 -p1 -b .diskspace
%patch195 -p1 -b .perl.req5
%patch196 -p1 -b .badowner
%patch197 -p1 -b .perl.req6
%patch198 -p1 -b .sf_fingerprint
%patch199 -p1 -b .dependson

%patch200 -p1 -b .filter-soname-deps
%patch201 -p1 -b .dont-filter-ld64

%patch301 -p1 -b .niagara
%patch302 -p1 -b .geode
%patch304 -p1 -b .ldflags
%patch305 -p1 -b .dwz-debuginfo
%patch306 -p1 -b .minidebuginfo
%patch307 -p1 -b .sepdebugcrcfix
%patch308 -p1 -b .minidebuginfo-ppc64
%patch309 -p1 -b .chmod
%patch310 -p1 -b .namesize
%patch311 -p1 -b .config.guess
%patch312 -p1 -b .man-inhibit
%patch313 -p1 -b .quiet-sign
%patch314 -p1 -b .verifysig

%patch400 -p1 -b .rpmlib-filesystem-check
%patch401 -p1 -b .disable-collection-plugins
%patch402 -p1 -b .remove-EVR-check

%patch5 -p1 -b .armhfp
# this patch cant be applied on softfp builds
%ifnarch armv3l armv4b armv4l armv4tl armv5tel armv5tejl armv6l armv7l
%patch6 -p1 -b .armhfp-logic
%endif

%patch501 -p1 -b .elem-progress
%patch502 -p1 -b .elem-progress-header
%patch503 -p1 -b .reinstall
%patch504 -p1 -b .g-libs
%patch505 -p1 -b .brp-python-bytecompile
%patch506 -p1 -b .fix-g-libs

%patch701 -p1 -b .python-package-name
%patch702 -p1 -b .fix-python3-import

%if %{with int_bdb}
ln -s db-%{bdbver} db
%endif

# compress our ChangeLog, it's fairly big...
bzip2 -9 ChangeLog


%build
CPPFLAGS="$CPPFLAGS `pkg-config --cflags nss`"
CFLAGS="$RPM_OPT_FLAGS"
export CPPFLAGS CFLAGS LDFLAGS

autoreconf -i -f

# Using configure macro has some unwanted side-effects on rpm platform
# setup, use the old-fashioned way for now only defining minimal paths.
./configure \
    --prefix=%{_usr} \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_var} \
    --sharedstatedir=%{_var}/lib \
    --libdir=%{_libdir} \
    --build=%{_target_platform} \
    --host=%{_target_platform} \
    --with-vendor=redhat \
    %{!?with_int_bdb: --with-external-db} \
    %{!?with_plugins: --disable-plugins} \
    --with-lua \
    --with-selinux \
    --with-cap \
    --with-acl

make %{?_smp_mflags}

pushd python
%py3_build
popd


%install
pushd python
%py3_install
popd

%check
test -f %{buildroot}%{python3_sitearch}/rpm-%{version}-py%{python3_version}.egg-info


%files -n python%{python3_pkgversion}-rpm
%doc GROUPS COPYING CREDITS ChangeLog.bz2
%{python3_sitearch}/rpm/
%{python3_sitearch}/rpm-%{version}-py%{python3_version}.egg-info

%changelog
* Thu May 14 2020 Miro Hrončok <mhroncok@redhat.com> - 4.11.3-8
- Sync with rpm-4.11.3-43.el7 (RHEL 7.8)
- Fix packages getting removed on failed update via dnf (#1710691)
- Fix segfault on fingerprint symlink (#1660232)
- Fix bogus if-condition in find-debuginfo.sh (#1720590)

* Fri Oct 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.11.3-7
- Fix Python import directive for more strict Python3 search rules (#1762942)

* Fri Sep 20 2019 Miro Hrončok <mhroncok@redhat.com> - 4.11.3-7
- Sync with rpm-4.11.3-40.el7 (RHEL 7.7)

* Wed May 01 2019 Miro Hrončok <mhroncok@redhat.com> - 4.11.3-7
- Provide python3-rpm

* Wed Apr 24 2019 Miro Hrončok <mhroncok@redhat.com> - 4.11.3-7
- Add lower bound for rpm release

* Wed Mar 20 2019 Miro Hrončok <mhroncok@redhat.com> - 4.11.3-3
- Initial EPEL package, copied from Fedora 20 and adapted
