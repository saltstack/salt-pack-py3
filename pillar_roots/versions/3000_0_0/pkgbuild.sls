# This file provides pillar data that will be used by Jinja macros to define #
# various SLS elements in templated SLS files. The formatting is flexible and
# allows for defaults to be overridden on a per-version basis.
#
# The top-level key must be named "pkgbuild_registry", which will contain
# sub-dictionaries for each platform. Each platform will contain its own
# sub-dictionary containing keys for each package. Here's an example:
#
# pkgbuild_registry:
#   rhel7:
#     foo:
#       version: 1.0.1-2
#       results:
#         - foo
#         - foo-devel
#     bar:
#       version: 2.1.0-1
#       build_deps:
#         - foo
#       additional_deps:
#         - baz
#     baz:
#       version: 4.5-3
#       4.2-1:
#         additional_deps:
#           - qux
#     qux:
#       version: 3.1-3
#     python-foo:
#       name: pyfoo
#       version: 6.1-1
#       additional_deps:
#         - foo
#
# The package keys ("foo", "bar", etc. in the example above) correspond to the
# directory names underneath the "pkg" dir which contains all the package
# sources and specs. If the actual package name to be built differs from this,
# then a sub-key called "name" must be used to specify the actual package name.
# This allows for differences between package naming in different distros to be
# managed flexibly. So, for instance, the sources and specs in
# pkg/python-foo/6_1/rhel7 would be for a package which will ultimately be
# named "pyfoo".
#
# The "results" key will contain a list of package names which will be built.
# If omitted, then it will be assumed that only a single package will be built,
# and its name will be the name of the parent dictionary key (or the value of #
# its "name" key, if present). For example, in the above example, "bar", "baz"
# and "qux" will build packages named "bar', "baz", and "qux", respectively.
# "foo" will build two packages, "foo" and "foo-devel", while "python-foo" will
# build a package named "pyfoo".
#
# The "version" key is required and should be defined in the format
# <version>-<release>. Note that the "release" portion of the version will not
# be included in the directory containing the sources and specs. For example,
# the files for the "baz" package above would be located in pkg/baz/4_5/rhel7/.
# The dots would be replaced with underscores to reduce confusion as dots
# signifiy directory boundaries when referenced as an SLS path (e.g.
# pkg.baz.4_5.rhel7).
#
# Two keys are used to detail dependency relationships, "build_deps" and
# "additional_deps".
#
# The "build_deps" key will contain a list of keys referring to the packages
# which are required as build-time dependencies. Note that individual package
# names should not be specified here, just the dictionary key for that package.
# For each build dep, the package(s) referred to by the "results" key (or its
# fallback) values will be added to the "deps" argument of the pkgbuild.built
# state, causing them to be installed in the build chroot before building.
#
# The "additional_deps" key will contain a list of keys referring to any
# runtime dependencies of the package, excluding any of those already defined
# in "build_deps". The build_deps and additional_deps will be defined as
# "require" requisites, ensuring that they are successfully built before
# attempting to build the current package. This is why runtime dependencies
# which are not also build dependencies do not need to be defined in the
# "additional_deps" key. Dependencies which are runtime-only and not needed at
# build time should be included here.
#
# NOTE: Only dependencies managed by this automated build system need to be
# defined in either "build_deps" or "additional_deps".
#
# A "noarch" key must be present and set to True to build
# architecture-independent packages, otherwise it will be assumed that the
# package is architecture-specific and the architecture will be inferred from
# the value of the pkgbuild.build_arch pillar key.
#
# Finally, keys for a specific <version>-<release> combo can contain
# "build_deps", "additional_deps", and "results" sub-keys, which can be used to
# define deviations from the values defined in higher-level keys. For example,
# if building "baz", and its "version" key is set to 4.2-1, then "qux" will be
# assumed to be a runtime dependency, whereas if the version is set to anything
# else then it will not.
#
# Keep in mind that setting these values will not automagically set build and
# runtime dependencies, versions, etc. in the spec files, the specs must be
# edited independently. The purpose of this pillar data is simply to make
# packages aware of their dependencies and pull in the right build deps, have
# the right requisites set, etc.
#

pkgbuild_registry:
  rhel8:
    Cython:
      version: 0.29.6-2
      results:
        - python3-Cython
    distribution-gpg-keys:
      version: 1.30-1
      noarch: True
      results:
        - distribution-gpg-keys
        - distribution-gpg-keys-copr
    libsodium:
      version: 1.0.17-2
      results:
        - libsodium
        - libsodium-devel
    libtomcrypt:
      version: 1.17-23
      results:
        - libtomcrypt
        - libtomcrypt-devel
    libtommath:
      version: 0.42.0-4
      results:
        - libtommath
        - libtommath-devel
    libunwind:
      version: 1.3.1-2
      results:
        - libunwind
        - libunwind-devel
    mock:
      version: 1.4.15-2
      noarch: True
      build_deps:
        - mock-core-configs
        - python-distro
        - python-pyroute2
      results:
        - mock
        - mock-lvm
        - mock-scm
    mock-core-configs:
      version: 30.3-1
      noarch: True
      build_deps:
        - distribution-gpg-keys
      results:
        - mock-core-configs
    openpgm:
      version: 5.2.122-17
      results:
        - openpgm
        - openpgm-devel
    python-cherrypy:
      version: 5.6.0-6
      noarch: True
      build_deps:
        - python-mock
      results:
        - python3-cherrypy
    python-distro:
      version: 1.2.0-4
      noarch: True
      results:
        - python3-distro
    python-funcsigs:
      version: 1.0.2-13
      noarch: True
      results:
        - python3-funcsigs
    python-gnupg:
      version: 0.4.4-2
      noarch: True
      results:
        - python3-gnupg
    python-libcloud:
      version: 2.4.0-1
      noarch: True
      results:
        - python3-libcloud
    python-libnacl:
      version: 1.6.1-2
      noarch: True
      results:
        - python-libnacl
        - python3-libnacl
    python-m2crypto:
      version: 0.33.0-1
      build_deps:
        - python-typing
      results:
        - python3-m2crypto
    python-msgpack:
      version: 0.6.1-3
      build_deps:
        - Cython
        - python-funcsigs
      results:
        - python3-msgpack
    python-mock:
      version: 2.0.0-14
      noarch: True
      build_deps:
        - python-pbr
      results:
        - python3-mock
    python-pbr:
      version: 5.1.2-3
      noarch: True
      results:
        - python3-pbr
    python-psutil:
      version: 5.4.3-8
      results:
        - python3-psutil
    python-pycryptodome:
      version: 3.6.1-3
      results:
        - python3-pycryptodomex
    python-pyroute2:
      version: 0.4.13-3
      noarch: True
      results:
        - python3-pyroute2
    python-pyzmq:
      name: python-zmq
      version: 17.0.0-5
      build_deps:
        - zeromq
      results:
        - python3-zmq
    python-simplejson:
      version: 3.16.0-3
      results:
        - python3-simplejson
    python-timelib:
      version: 0.2.4-4
      noarch: True
      results:
        - python3-timelib
    python-tornado4:
      version: 4.5.2-3
      build_deps:
        - python-backports_abc
        - python-pycurl
        - python-singledispatch
      results:
        - python3-tornado4
    python-typing:
      version: 3.5.2.2-4
      noarch: True
      results:
        - python3-typing
    python-yaml:
      name: PyYAML
      version: 5.1-2
      results:
        - python3-pyyaml
    salt:
      version: 3000.0.0rc2-1
      noarch: True
      build_deps:
        - python-mock
        - python-pyzmq
        - python-libcloud
      results:
        - salt
        - salt-master
        - salt-minion
        - salt-syndic
        - salt-api
        - salt-cloud
        - salt-ssh
    zeromq:
      version: 4.3.1-4
      build_deps:
        - libunwind
        - openpgm
      results:
        - zeromq
        - zeromq-devel


  rhel7:
    libsodium:
      version: 1.0.18-1
      results:
        - libsodium
        - libsodium-devel
    libtomcrypt:
      version: 1.17-23
      results:
        - libtomcrypt
        - libtomcrypt-devel
    libtommath:
      version: 0.42.0-4
      results:
        - libtommath
        - libtommath-devel
    openpgm:
      version: 5.2.122-2
      results:
        - openpgm
        - openpgm-devel
    python36:
      version: 3.6.8-2
      results:
        - python36
        - python36-debug
        - python36-debuginfo
        - python36-devel
        - python36-idle
        - python36-libs
        - python36-test
        - python36-tkinter
    python-bottle:
      version: 0.12.13-9
      noarch: True
      build_deps:
        - python36
        - python-setuptools
      results:
        - python36-bottle
    python-chardet:
      version: 3.0.4-12
      noarch: True
      build_deps:
        - python36
      results:
        - python36-chardet
    python-cherrypy:
      version: 5.6.0-6
      noarch: True
      build_deps:
        - python36
        - python-mock
      results:
        - python36-cherrypy
    python-crypto:
      version: 2.6.1-26
      build_deps:
        - libtommath
        - libtomcrypt
        - libtomcrypt-devel
        - python36
      results:
        - python36-crypto
    python-gnupg:
      version: 0.4.4-2
      noarch: True
      build_deps:
        - python36
      results:
        - python36-gnupg
    python-idna:
      version: 2.7-5
      noarch: True
      results:
        - python36-idna
    python-ioflo:
      version: 1.3.8-5
      noarch: True
      build_deps:
        - python36
      results:
        - python36-ioflo
    python-jinja2:
      version: 2.8.1-3
      noarch: True
      build_deps:
        - python36
        - python-markupsafe
        - python-setuptools
      results:
        - python36-jinja2
    python-libcloud:
      version: 2.0.0-4
      noarch: True
      build_deps:
        - python36
      results:
        - python36-libcloud
    python-libnacl:
      version: 1.6.1-3
      noarch: True
      build_deps:
        - python36
      results:
        - python36-libnacl
    python-m2crypto:
      version: 0.33.0-1
      build_deps:
        - python36
      results:
        - python36-m2crypto
    python-markupsafe:
      version: 0.23-4
      build_deps:
        - python36
        - python-setuptools
      results:
        - python36-markupsafe
    python-msgpack:
      version: 0.5.6-6
      build_deps:
        - python36
      results:
        - python36-msgpack
    python-mock:
      version: 2.0.0-3
      noarch: True
      build_deps:
        - python36
        - python-pbr
        - python-six
      results:
        - python36-mock
    python-pbr:
      version: 4.2.0-4
      noarch: True
      build_deps:
        - python36
      results:
        - python36-pbr
    python-psutil:
      version: 2.2.1-3
      build_deps:
        - python36
      results:
        - python36-psutil
    python-pycryptodomex:
      version: 3.7.3-3
      build_deps:
        - libtommath
        - libtomcrypt
        - libtomcrypt-devel
        - python36
      results:
        - python36-pycryptodomex
    python-pycurl:
      version: 7.43.0-8
      build_deps:
        - python-bottle
      results:
        - python36-pycurl
    python-pysocks:
      version: 1.6.8-6
      noarch: True
      build_deps:
        - python36
      results:
        - python36-pysocks
    python-pyzmq:
      name: python-zmq
      version: 15.3.0-6
      build_deps:
        - python36
        - zeromq
      results:
        - python36-zmq
    python-raet:
      version: 0.6.6-7
      noarch: True
      build_deps:
        - python36
        - python-ioflo
        - python-libnacl
      results:
        - python36-raet
    python-requests:
      version: 2.12.5-4
      noarch: True
      build_deps:
        - python36
        - python-chardet
        - python-urllib3
        - python-idna
      results:
        - python36-requests
    python-setuptools:
      version: 39.2.0-4
      noarch: True
      build_deps:
        - python36
      results:
        - python36-setuptools
    python-simplejson:
      version: 3.10.0-3
      build_deps:
        - python36
      results:
        - python36-simplejson
    python-six:
      version: 1.11.0-4
      noarch: True
      build_deps:
        - python36
      results:
        - python36-six
    python-timelib:
      version: 0.2.4-5
      noarch: True
      build_deps:
        - python36
      results:
        - python36-timelib
    python-tornado:
      version: 4.4.2-4
      build_deps:
        - python36
        - python-setuptools
      results:
        - python36-tornado
    python-typing:
      version: 3.5.2.2-4
      noarch: True
      build_deps:
        - python36
      results:
        - python36-typing
    python-urllib3:
      version: 1.19.1-6
      noarch: True
      build_deps:
        - python36
        - python-pysocks
        - python-setuptools
      results:
        - python36-urllib3
    python-yaml:
      name: PyYAML
      version: 3.11-3
      build_deps:
        - python36
        - python-setuptools
      results:
        - python36-PyYAML
    salt:
      version: 3000.0.0rc2-1
      noarch: True
      build_deps:
        - python36
        - python-m2crypto
        - python-msgpack
        - python-yaml
        - python-requests
        - python-pyzmq
        - python-markupsafe
        - python-tornado
        - python-libcloud
        - python-mock
        - python-six
      results:
        - salt
        - salt-master
        - salt-minion
        - salt-syndic
        - salt-api
        - salt-cloud
        - salt-ssh
    zeromq:
      version: 4.1.4-7
      build_deps:
        - openpgm
      results:
        - zeromq
        - zeromq-devel


  amzn2:
    distribution-gpg-keys:
      version: 1.30-1
      noarch: True
      results:
        - distribution-gpg-keys
        - distribution-gpg-keys-copr
    libsodium:
      version: 1.0.16-1
      results:
        - libsodium
        - libsodium-devel
    libtomcrypt:
      version: 1.17-27
      build_deps:
        - libtommath
      results:
        - libtomcrypt
        - libtomcrypt-devel
    libtommath:
      version: 0.42.0-7
      results:
        - libtommath
        - libtommath-devel
    mock:
      version: 1.4.15-3
      noarch: True
      build_deps:
        - mock-core-configs
        - python-distro
        - python-jinja2
        - python-requests
        - python-pyroute2
        - python-rpm
        - python-six
      results:
        - mock
        - mock-lvm
        - mock-scm
    mock-core-configs:
      version: 30.3-2
      noarch: True
      build_deps:
        - distribution-gpg-keys
      results:
        - mock-core-configs
    openpgm:
      version: 5.2.122-15
      results:
        - openpgm
        - openpgm-devel
    python-atomicwrites:
      version: 1.1.5-14
      noarch: True
      results:
        - python3-atomicwrites
    python-attrs:
      version: 17.4.0-9
      noarch: True
      results:
        - python3-attrs
    python-babel:
      version: 2.6.0-7
      noarch: True
      build_deps:
        - python-pytz
        - python-freezegun
        - python-pytest
      results:
        - python3-babel
    python-backports_abc:
      version: 0.5-10
      noarch: True
      results:
        - python3-backports_abc
    python-bottle:
      version: 0.12.13-8
      noarch: True
      results:
        - python3-bottle
    python-chardet:
      version: 3.0.4-11
      noarch: True
      results:
        - python3-chardet
    python-cherrypy:
      version: 5.6.0-6
      noarch: True
      results:
        - python3-cherrypy
      build_deps:
        - python-nose
    python-coverage:
      version: 4.5.1-5
      results:
        - python3-coverage
    python-crypto:
      version: 2.6.1-26
      build_deps:
        - libtommath
        - libtomcrypt
        - libtomcrypt-devel
      results:
        - python3-crypto
    python-dateutil:
      version: 2.7.3-3
      noarch: True
      build_deps:
        - python-six
        - python-setuptools_scm
        - python-hypothesis
      results:
        - python3-dateutil
    python-distro:
      version: 1.2.0-5
      noarch: True
      results:
        - python3-distro
    python-freezegun:
      version: 0.3.8-13
      noarch: True
      build_deps:
        - python-dateutil
        - python-sure
        - python-nose
        - python-coverage
        - python-six
        - python-mock
      results:
        - python3-freezegun
    python-funcsigs:
      version: 1.0.2-13
      noarch: True
      build_deps:
        - python-unittest2
      results:
        - python3-funcsigs
    python-gnupg:
      version: 0.4.4-2
      noarch: True
      results:
        - python3-gnupg
    python-hypothesis:
      version: 3.66.11-3
      noarch: True
      build_deps:
        - python-attrs
        - python-coverage
      results:
        - python3-hypothesis
    python-idna:
      version: 2.7-5
      noarch: True
      results:
        - python3-idna
    python-jinja2:
      version: 2.10-8
      noarch: True
      build_deps:
        - python-markupsafe
        - python-babel
        - python-pytest
      results:
        - python3-jinja2
    python-libcloud:
      version: 2.2.1-10
      noarch: True
      build_deps:
        - python-pytest-runner
      results:
        - python3-libcloud
    python-m2crypto:
      version: 0.31.0-4
      results:
        - python3-m2crypto
      build_deps:
        - python-typing
    python-markupsafe:
      version: 1.0-3
      results:
        - python3-markupsafe
    python-mock:
      version: 2.0.0-15
      noarch: True
      build_deps:
        - python-pbr
        - python-six
      results:
        - python3-mock
    python-more-itertools:
      version: 4.1.0-6
      noarch: True
      build_deps:
        - python-nose
        - python-six
      results:
        - python3-more-itertools
    python-msgpack:
      version: 0.5.6-7
      build_deps:
        - python-funcsigs
      results:
        - python3-msgpack
    python-nose:
      version: 1.3.7-23
      noarch: True
      build_deps:
        - python-setuptools
        - python-mock
        - python-coverage
        - python-six
      results:
        - python3-nose
    python-pbr:
      version: 5.1.2-4
      noarch: True
      results:
        - python3-pbr
    python-pluggy:
      version: 0.7.1-3
      noarch: True
      build_deps:
        - python-setuptools_scm
      results:
        - python3-pluggy
    python-psutil:
      version: 5.4.3-8
      build_deps:
        - python-mock
        - python-six
      results:
        - python3-psutil
    python-py:
      version: 1.5.4-5
      noarch: True
      build_deps:
        - python-setuptools_scm
      results:
        - python3-py
    python-pycryptodome:
      version: 3.6.1-4
      build_deps:
        - libtommath
        - libtomcrypt
        - libtomcrypt-devel
      results:
        - python3-pycryptodomex
    python-pycurl:
      version: 7.43.0.2-5
      build_deps:
        - python-bottle
        - python-nose
        - python-pyflakes
      results:
        - python3-pycurl
    python-pyflakes:
      version: 2.0.0-8
      noarch: True
      results:
        - python3-pyflakes
    python-pyroute2:
      version: 0.5.3-4
      noarch: True
      results:
        - python3-pyroute2
    python-pysocks:
      version: 1.6.8-6
      noarch: True
      results:
        - python3-pysocks
    python-pytest:
      version: 3.6.4-3
      noarch: True
      build_deps:
        - python-atomicwrites
        - python-attrs
        - python-funcsigs
        - python-hypothesis
        - python-more-itertools
        - python-setuptools_scm
        - python-zope-interface
        - python-zope-event
        - python-pluggy
        - python-py
      results:
        - python3-pytest
    python-pytest-runner:
      version: 4.0-5
      noarch: True
      build_deps:
        - python-pytest
        - python-setuptools_scm
      results:
        - python3-pytest-runner
    python-pytz:
      version: 2018.5-3
      noarch: True
      build_deps:
        - python-pytest
      results:
        - python3-pytz
    python-pyzmq:
      name: python-zmq
      version: 17.0.0-5
      build_deps:
        - zeromq
      results:
        - python3-zmq
    python-requests:
      version: 2.19.1-5
      noarch: True
      build_deps:
        - python-chardet
        - python-idna
        - python-urllib3
      results:
        - python3-requests
    python-rpm:
      version: 4.11.3-5
      build_deps:
        - rpm
        - rpm-build
        - rpm-build-libs
        - rpm-libs
        - rpm-plugin-systemd-inhibit
        - rpm-python
        - rpm-sign
      results:
        - python3-rpm
    python-setuptools_scm:
      version: 3.1.0-3
      noarch: True
      results:
        - python3-setuptools_scm
    python-simplejson:
      version: 3.16.0-3
      build_deps:
        - python-nose
      results:
        - python3-simplejson
    python-singledispatch:
      version: 3.4.0.3-15
      noarch: True
      build_deps:
        - python-six
      results:
        - python3-singledispatch
    python-six:
      version: 1.11.0-8
      noarch: True
      results:
        - python3-six
    python-sure:
      version: 1.4.11-5
      noarch: True
      build_deps:
        - python-mock
        - python-six
        - python-nose
      results:
        - python3-sure
    python-timelib:
      version: 0.2.4-5
      noarch: True
      results:
        - python3-timelib
    python-tornado:
      version: 4.5.2-5
      build_deps:
        - python-backports_abc
        - python-pycurl
        - python-singledispatch
      results:
        - python3-tornado
    python-tornado4:
      version: 4.5.2-5
      build_deps:
        - python-backports_abc
        - python-pycurl
        - python-singledispatch
      results:
        - python3-tornado4
    python-typing:
      version: 3.5.2.2-5
      noarch: True
      results:
        - python3-typing
    python-unittest2:
      version: 1.1.0-17
      noarch: True
      build_deps:
        - python-six
      results:
        - python3-unittest2
    python-urllib3:
      version: 1.23-6
      noarch: True
      build_deps:
        - python-six
        - python-pysocks
      results:
        - python3-urllib3
    python-yaml:
      name: PyYAML
      version: 4.2-0.1.b5
      results:
        - python3-pyyaml
    python-zope-event:
      version: 4.2.0-13
      noarch: True
      results:
        - python3-zope-event
    python-zope-interface:
      version: 4.5.0-4
      build_deps:
        - python-nose
        - python-zope-event
      results:
        - python3-zope-interface
    rpm:
      version: 4.11.3-36
      results:
        - rpm
        - rpm-build
        - rpm-build-libs
        - rpm-libs
        - rpm-plugin-systemd-inhibit
        - rpm-python
        - rpm-sign
        - rpm-debuginfo
        - rpm-devel
    salt:
      version: 3000.0.0rc2-1
      noarch: True
      build_deps:
        - python-pycryptodome
        - python-msgpack
        - python-yaml
        - python-requests
        - python-pyzmq
        - python-markupsafe
        - python-tornado4
        - python-futures
        - python-libcloud
        - python-mock
        - python-six
      results:
        - salt
        - salt-master
        - salt-minion
        - salt-syndic
        - salt-api
        - salt-cloud
        - salt-ssh
    zeromq:
      version: 4.2.3-1
      build_deps:
        - openpgm
        - libsodium
      results:
        - zeromq
        - zeromq-devel


