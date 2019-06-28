# Import base config
{% import "setup/amazon/map.jinja" as build_cfg %}


build_pkgs:
  pkg.installed:
    - allow_updates: True
    - pkgs:
      - createrepo
      - mock
      - rpmdevtools
      - rpm-sign
      - gnupg2
      - python3-gnupg
      - wget
      - rpm: latest


{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_pkgs


