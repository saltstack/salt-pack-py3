# Import base config
{% import "setup/redhat/map.jinja" as build_cfg %}

## assume epel-7
{% set epel_source_hash = '58fa8ae27c89f37b08429f04fd4a88cc' %}

os_pkgs_repo_key:
  file.managed:
    - name: /etc/pki/rpm-gpg/RPM-GPG-KEY-{{build_cfg.build_epel|upper}}
    - source: https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-{{build_cfg.build_epel|upper}}
    - source_hash: md5={{epel_source_hash}}
    - dir_mode: 755
    - mode: 644
    - makedirs: True


os_pkgs_repo:
  pkgrepo.managed:
    - humanname: os_packages_repo_epel
    - mirrorlist: https://mirrors.fedoraproject.org/metalink?repo={{build_cfg.build_epel}}&arch=$basearch
    - comments:
      - '## Fedora Project support for epel-release {{build_cfg.build_epel}}'
    - gpgcheck: 1
    - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-{{build_cfg.build_epel|upper}}
    - require:
      - file: os_pkgs_repo_key


include:
  - setup.redhat
  - setup.redhat.rhel7.base_pkgs
  - setup.redhat.rhel7.base7_deps


build_additional_py3_pkgs:
  pkg.installed:
    - pkgs:
      - epel-release
      - python3
      - python3-devel
      - python3-setuptools
      - createrepo_c
      - createrepo
      - rpm-sign
      - nfs-utils
      - autoconf
      - bluez-libs-devel
      - bzip2
      - bzip2-devel
      - expat-devel
      - findutils
      - gcc-c++
      - gdb
      - glibc-devel
      - gmp-devel
      - libffi-devel
      - mesa-libGL-devel
      - libX11-devel
      - ncurses-devel
      - net-tools
      - openssl-devel
      - pkgconfig
      - python-rpm-macros
      - readline-devel
      - sqlite-devel
      - tar
      - tcl-devel
      - tix-devel
      - tk-devel
      - valgrind-devel
      - vsftpd
      - xz-devel
      - zlib-devel
      - curl
      - libcurl
      - libcurl-devel
      - python36-gnupg
      - python36-libcloud
      - chrpath
      - zeromq-devel

epel-rpm-macros:
  pkg.installed

##  - desktop-file-utils
##  - libappstream-glib
