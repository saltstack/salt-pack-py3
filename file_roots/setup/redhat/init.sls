# Import base config
{% import "setup/redhat/map.jinja" as build_cfg %}

build_pkgs:
  pkg.installed:
    - pkgs:
      - rpmdevtools
      - mock
      - gnupg2


ensure_build_dest_dir:
  file.directory:
    - name: {{build_cfg.build_dest_dir}}
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - dir_mode: 755
    - file_mode: 644
    - makedirs: True
    - recurse:
        - user
        - group
        - mode

