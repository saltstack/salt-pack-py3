# Import base config
{% import "setup/amazon/map.jinja" as build_cfg %}


ensure_latest:
  module.run:
    - pkg.upgrade:


build_pkgs:
  pkg.installed:
    - allow_updates: True
    - pkgs:
      - createrepo_c
      - mock
      - rpmdevtools
      - rpm-sign
      - gnupg2
      - python3-gnupg
      - wget


{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_pkgs


