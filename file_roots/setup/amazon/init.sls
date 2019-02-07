# Import base config
{% import "setup/amazon/map.jinja" as build_cfg %}

{% set pkg_pub_key_file = pillar.get('gpg_pkg_pub_keyname', None) %}
{% set pkg_priv_key_file = pillar.get('gpg_pkg_priv_keyname', None) %}

{% set gpg_key_dir = build_cfg.build_gpg_keydir %}
{% set pkg_pub_key_absfile = gpg_key_dir ~ '/' ~ pkg_pub_key_file %}
{% set pkg_priv_key_absfile = gpg_key_dir ~ '/' ~ pkg_priv_key_file %}


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


