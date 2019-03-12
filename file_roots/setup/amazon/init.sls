# Import base config
{% import "setup/amazon/map.jinja" as build_cfg %}

{% set pkg_pub_key_file = pillar.get('gpg_pkg_pub_keyname', None) %}
{% set pkg_priv_key_file = pillar.get('gpg_pkg_priv_keyname', None) %}

{% set gpg_key_dir = build_cfg.build_gpg_keydir %}
{% set pkg_pub_key_absfile = gpg_key_dir ~ '/' ~ pkg_pub_key_file %}
{% set pkg_priv_key_absfile = gpg_key_dir ~ '/' ~ pkg_priv_key_file %}


{% set build_epel = 'epel-7' %}
{% set epel_source_hash = '58fa8ae27c89f37b08429f04fd4a88cc' %}

os_pkgs_repo_key:
  file.managed:
    - name: /etc/pki/rpm-gpg/RPM-GPG-KEY-{{build_epel|upper}}
    - source: https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-{{build_epel|upper}}
    - source_hash: md5={{epel_source_hash}}
    - dir_mode: 755
    - mode: 644
    - makedirs: True


os_pkgs_repo:
  pkgrepo.managed:
    - humanname: os_packages_repo_epel
    - mirrorlist: https://mirrors.fedoraproject.org/metalink?repo={{build_epel}}&arch=$basearch
    - comments:
        - '## Fedora Project support for epel-release {{build_epel}}'
    - gpgcheck: 1
    - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-{{build_epel|upper}}
    - require:
      - file: os_pkgs_repo_key


build_pkgs:
  pkg.installed:
    - pkgs:
      - createrepo
      - mock
      - rpmdevtools
      - rpm-sign
      - gnupg2
      - python2-gnupg


{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_pkgs


