# Import base config
{% import "setup/redhat/map.jinja" as build_cfg %}

### # no epel-8 at the moment
### {% set epel_source_hash = '88888888888888888888888888888888' %}
### 
### os_pkgs_repo_key:
###   file.managed:
###     - name: /etc/pki/rpm-gpg/RPM-GPG-KEY-{{build_cfg.build_epel|upper}}
###     - source: https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-{{build_cfg.build_epel|upper}}
###     - source_hash: md5={{epel_source_hash}}
###     - dir_mode: 755
###     - mode: 644
###     - makedirs: True
###
###
### os_pkgs_repo:
###   pkgrepo.managed:
###     - humanname: os_packages_repo_epel
###     - mirrorlist: https://mirrors.fedoraproject.org/metalink?repo={{build_cfg.build_epel}}&arch=$basearch
###     - comments:
###       - '## Fedora Project support for epel-release {{build_cfg.build_epel}}'
###     - gpgcheck: 1
###     - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-{{build_cfg.build_epel|upper}}
###     - require:
###       - file: os_pkgs_repo_key


include:
  - setup.redhat


build_additional_pkgs:
  pkg.installed:
    - pkgs:
      - rpm-sign
      - nfs-utils
      - createrepo_c
      - mock
      - openssl-devel
      - texlive-latex2man
      - krb5-devel
      - chrpath
      - python3-gpg
##      - python3-gnupg


{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_additional_pkgs


{% if build_cfg.build_py3 %}
build_additional_py3_pkgs:
  pkg.installed:
    - pkgs:
      - python36
      - python36-devel
      - python3-setuptools
##      - python3
##      - python3-devel
##      - epel-release
{% endif %}

