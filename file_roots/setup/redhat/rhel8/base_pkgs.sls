# Import base config
{% import "setup/redhat/map.jinja" as build_cfg %}

build_base_pkgs:
  pkg.installed:
    - pkgs:
      - python3-gnupg
      - python3-mock


{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_base_pkgs


