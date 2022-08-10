# Import base config
{% import "setup/amazon/map.jinja" as build_cfg %}

{% set pkg_pub_key_file = pillar.get('gpg_pkg_pub_keyname', None) %}
{% set pkg_priv_key_file = pillar.get('gpg_pkg_priv_keyname', None) %}

{% set gpg_key_dir = build_cfg.build_gpg_keydir %}
{% set pkg_pub_key_absfile = gpg_key_dir ~ '/' ~ pkg_pub_key_file %}
{% set pkg_priv_key_absfile = gpg_key_dir ~ '/' ~ pkg_priv_key_file %}

{% set amzn2_salt_mock_cfg = '/etc/mock/amzn2-salt-x86_64.cfg' %}
{% set src_amzn2_salt_mock_cfg = 'salt://setup/amazon/amzn2/amzn2-salt-x86_64.cfg' %}

include:
  - setup.amazon


build_additional_pkgs_{{build_cfg.build_release}}:
  pkg.installed:
    - pkgs:
      - python3-rpm-macros
      - gcc
      - dbus-devel
      - dos2unix
      - libdb-devel
      - elfutils-devel
      - elfutils-libelf-devel
      - readline-devel
      - zlib-devel
      - nss-devel
      - nss-softokn-freebl-devel
      - popt-devel
      - file-devel
      - gettext-devel
      - libselinux-devel
      - libsemanage-devel
      - ncurses-devel
      - bzip2-devel
      - lua-devel
      - libcap-devel
      - libacl-devel
      - xz-devel
      - audit-libs-devel
      - binutils-devel
      - automake
      - libtool
      - chrpath
      - python3-libcloud
      - python3-devel
      - python3-mock


build_additional_{{build_cfg.build_release}}_{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_additional_pkgs_{{build_cfg.build_release}}


build_salt_mock_prefs_rm:
  file.absent:
    - name: {{amzn2_salt_mock_cfg}}


build_salt_mock_prefs_file:
  file.managed:
    - name: {{amzn2_salt_mock_cfg}}
    - source: {{src_amzn2_salt_mock_cfg}}
    - dir_mode: 755
    - mode: 644
    - makedirs: True
    - group: mock
    - skip_verify: True


manage_priv_key_{{build_cfg.build_release}}:
  file.managed:
    - name: {{build_cfg.build_gpg_keydir}}/{{ pillar['gpg_pkg_priv_keyname'] }}
    - dir_mode: 700
    - mode: 600
    - contents_pillar: gpg_pkg_priv_key
    - show_changes: false
    - user: {{build_cfg.build_runas}}
    - group: mock
    - makedirs: True
    - require:
      - user: build_additional_{{build_cfg.build_release}}_{{build_cfg.build_runas}}


manage_pub_key_{{build_cfg.build_release}}:
  file.managed:
    - name: {{build_cfg.build_gpg_keydir}}/{{ pillar['gpg_pkg_pub_keyname'] }}
    - dir_mode: 700
    - mode: 644
    - contents_pillar: gpg_pkg_pub_key
    - show_changes: false
    - user: {{build_cfg.build_runas}}
    - group: mock
    - makedirs: True
    - require:
      - file: manage_priv_key_{{build_cfg.build_release}}


gpg_load_pub_key_{{build_cfg.build_release}}:
  module.run:
    - name: gpg.import_key
    - kwargs:
        user: {{build_cfg.build_runas}}
        filename: {{pkg_pub_key_absfile}}
        gnupghome: {{gpg_key_dir}}
    - require:
      - file: manage_pub_key_{{build_cfg.build_release}}


gpg_load_priv_key_{{build_cfg.build_release}}:
  module.run:
    - name: gpg.import_key
    - kwargs:
        user: {{build_cfg.build_runas}}
        filename: {{pkg_priv_key_absfile}}
        gnupghome: {{gpg_key_dir}}
    - require:
      - module: gpg_load_pub_key_{{build_cfg.build_release}}


ensure_gpg_rights_{{build_cfg.build_release}}:
  file.directory:
    - name: {{gpg_key_dir}}
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - dir_mode: 700
    - file_mode: 600
    - recurse:
        - user
        - group
        - mode
    - require:
      - module: gpg_load_priv_key_{{build_cfg.build_release}}


ensure_pub_gpg_rights_{{build_cfg.build_release}}:
  module.run:
    - name: file.check_perms
    - m_name: {{gpg_key_dir}}/gpg_pkg_key.pub
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - mode: 644
    - ret: False
    - require:
      - file: ensure_gpg_rights_{{build_cfg.build_release}}

