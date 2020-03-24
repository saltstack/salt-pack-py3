%global srcname pycryptodomex
%global common_description PyCryptodome is a self-contained Python package of low-level cryptographic\
primitives. It's a fork of PyCrypto. It brings several enhancements with respect\
to the last official version of PyCrypto (2.6.1), for instance:\
\
  * Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)\
  * Accelerated AES on Intel platforms via AES-NI\
  * Elliptic curves cryptography (NIST P-256 curve only)\
  * Better and more compact API (nonce and iv attributes for ciphers, automatic\
    generation of random nonces and IVs, simplified CTR cipher mode, and more)\
  * SHA-3 (including SHAKE XOFs) and BLAKE2 hash algorithms\
  * Salsa20 and ChaCha20 stream ciphers\
  * scrypt and HKDF\
  * Deterministic (EC)DSA\
  * Password-protected PKCS#8 key containers\
  * Shamir's Secret Sharing scheme\
  * Random numbers get sourced directly from the OS (and not from a CSPRNG in\
    userspace)\
  * Cleaner RSA and DSA key generation (largely based on FIPS 186-4)\
  * Major clean ups and simplification of the code base\
\
PyCryptodome is not a wrapper to a separate C library like OpenSSL. To the\
largest possible extent, algorithms are implemented in pure Python. Only the\
pieces that are extremely critical to performance (e.g. block ciphers) are\
implemented as C extensions.\
\
Note: all modules are installed under the Cryptodome package to avoid conflicts\
with the PyCrypto library.


%bcond_with python2
%bcond_without python3
%bcond_with tests
%bcond_with docs

## %%global _with_python2 0%%{?rhel} || 0%%{?fedora} <= 29
## %%global _with_python3_other 0%%{?rhel}
## %%global python_sphinx_pkg %%{?rhel:python2}%%{?fedora:python%%{python3_pkgversion}}-sphinx
## %%global sphinx_build sphinx-build%%{?fedora:-%%{python3_version}}

%global _with_python3_other 0 


Name:           python-%{srcname}
Version:        3.7.3
Release:        4%{?dist}
Summary:        A self-contained cryptographic library for Python

# PyCrypto-based code is public domain, further PyCryptodome contributions are
# BSD
License:        BSD and Public Domain
URL:            http://www.pycryptodome.org/
Source0:        https://github.com/Legrandin/pycryptodome/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Use external libtomcrypt library
Patch0:         %{name}-3.7.3-use_external_libtomcrypt.patch
# Fix documentation build with Sphinx <= 1.2, especially on EL
Patch1:         %{name}-3.7.0-sphinx.patch
# Fix compilation flags
Patch2:         %{name}-3.7.3-cflags.patch

%description
%{common_description}

BuildRequires:  gcc
BuildRequires:  libtomcrypt-devel

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif


%if %{with python3}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{_with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%endif
%if %{with docs}
# Needed for documentation
BuildRequires:  %{python_sphinx_pkg}
%if 0%{?rhel}
BuildRequires:  python-sphinxcontrib-napoleon
%endif
%endif

%endif


%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
# GMP library is dl-opened
Requires:       gmp%{?_isa}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
# GMP library is dl-opened
Requires:       gmp%{?_isa}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{common_description}


%if 0%{?_with_python3_other}
%package -n python%{python3_other_pkgversion}-%{srcname}
Summary:        %{summary}
# GMP library is dl-opened
Requires:       gmp%{?_isa}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}

%description -n python%{python3_other_pkgversion}-%{srcname}
%{common_description}
%endif
%endif


%prep
%autosetup -n pycryptodome-%{version} -p0

# Drop bundled libraries
rm -r src/libtom/

# Remove shebang
sed '1{\@^#! /usr/bin/env python@d}' lib/Crypto/SelfTest/__main__.py >lib/Crypto/SelfTest/__main__.py.new && \
touch -r lib/Crypto/SelfTest/__main__.py lib/Crypto/SelfTest/__main__.py.new && \
mv lib/Crypto/SelfTest/__main__.py.new lib/Crypto/SelfTest/__main__.py


%build
touch .separate_namespace
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%if 0%{?_with_python3_other}
%py3_other_build
%endif
%endif


%if %{with docs}
# Build documentation
%make_build -C Doc/ man SPHINXBUILD=%{sphinx_build}
%endif


%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%if 0%{?_with_python3_other}
%py3_other_install
%endif
%endif


%if %{with docs}
# Install man pages
install -Dpm 0644 Doc/_build/man/pycryptodome.1 $RPM_BUILD_ROOT%{_mandir}/man1/pycryptodome.1
%endif

# Fix permissions
%if %{with python2}
chmod 0755 $RPM_BUILD_ROOT%{python2_sitearch}/Cryptodome/SelfTest/PublicKey/test_vectors/ECC/gen_ecc_p256.sh
%endif
%if %{with python3}
chmod 0755 $RPM_BUILD_ROOT%{python3_sitearch}/Cryptodome/SelfTest/PublicKey/test_vectors/ECC/gen_ecc_p256.sh
%if 0%{_with_python3_other}
chmod 0755 $RPM_BUILD_ROOT%{python3_other_sitearch}/Cryptodome/SelfTest/PublicKey/test_vectors/ECC/gen_ecc_p256.sh
%endif
%endif


%if %{with tests}

%check
%if %{with python2}
%{__python2} setup.py test
%endif
%if %{with python3}
%{__python3} setup.py test
%if 0%{?_with_python3_other}
%{__python3_other} setup.py test
%endif
%endif

%endif


%if %{with python2}
%files -n python2-%{srcname}
%doc AUTHORS.rst Changelog.rst README.rst
%license LICENSE.rst
%{python2_sitearch}/Cryptodome/
%{python2_sitearch}/%{srcname}-*.egg-info
%if %{with docs}
%{_mandir}/man1/pycryptodome.1.*
%endif
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc AUTHORS.rst Changelog.rst README.rst
%license LICENSE.rst
%{python3_sitearch}/Cryptodome/
%{python3_sitearch}/%{srcname}-*.egg-info
%if %{with docs}
%{_mandir}/man1/pycryptodome.1.*
%endif

%if 0%{?_with_python3_other}
%files -n python%{python3_other_pkgversion}-%{srcname}
%doc AUTHORS.rst Changelog.rst README.rst
%license LICENSE.rst
%{python3_other_sitearch}/Cryptodome/
%{python3_other_sitearch}/%{srcname}-*.egg-info
%if %{with docs}
%{_mandir}/man1/pycryptodome.1.*
%endif
%endif
%endif


%changelog
* Tue Mar 24 2020 SaltStack Packaging Team <packaging@saltstack.com> - 3.7.3-4
- Fix build issue with egg.info path

* Sun Sep 22 2019 SaltStack Packaging Team <packaging@saltstack.com> - 3.7.3-3
- Made support for Python 2, test and docs optional

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 3.7.3-2
- Rebuilt to change main python from 3.4 to 3.6

* Fri Feb 15 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3

* Mon Nov 19 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0
- Use the same .spec file for all supported releases of Fedora and EL
