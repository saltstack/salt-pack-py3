# Import base config
{% import "setup/redhat/map.jinja" as build_cfg %}

{% set epel_source_hash = '6494b13311caf38e11eaa575a83c2c57' %}

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
##  - setup.redhat.rhel8.base_pkgs


build_additional_py3_pkgs:
  pkg.installed:
    - pkgs:
      - python36
      - python36-devel
      - python3-gnupg
      - python3-setuptools
      - createrepo_c
      - rpm-sign
      - nfs-utils
      - openssl-devel
      - texlive-latex2man
      - krb5-devel
      - chrpath
      - python3-libcloud
      - git
      - python3-mock

