# Import base config
{% import "setup/amazon/map.jinja" as build_cfg %}


build_pkgs:
  pkg.installed:
    - pkgs:
      - createrepo
      - rpmdevtools
      - rpm-sign
      - gnupg2


<<<<<<< HEAD
ensure_pub_gpg_rights:
  module.run:
    - name: file.check_perms
    - m_name: {{gpg_key_dir}}/gpg_pkg_key.pub
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - mode: 644
    - ret: False
    - require:
      - file: ensure_gpg_rights


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


=======
>>>>>>> Continuing work in progress for Python 3 support on Amazon Linux 2
