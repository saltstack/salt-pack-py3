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


centos7_deps:
  file.managed:
    - name: /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
    - source: salt://setup/amazon/RPM-GPG-KEY-CentOS-7
    - source_hash: sha256=8b48b04b336bd725b9e611c441c65456a4168083c4febc28e88828d8ec14827f
    - makedirs: True
    - user: root
    - group: root
    - file_mode: 644
    - dir_mode: 755


epel7_deps:
  file.managed:
    - name: /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
    - source: salt://setup/amazon/RPM-GPG-KEY-EPEL-7
    - source_hash: sha256=028b9accc59bab1d21f2f3f544df5469910581e728a64fd8c411a725a82300c2
    - makedirs: True
    - user: root
    - group: root
    - file_mode: 644
    - dir_mode: 755


centos7-base:
  pkgrepo.managed:
    - humanname: CentOS-7-Base
    - comments:
      - '## CentOS 7 Base support used with Amazon Linux 2'
    - mirrorlist: http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=os
    - gpgcheck: 1
    - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
    - require:
      - file: centos7_deps
      - file: epel7_deps


centos7-updates:
  pkgrepo.managed:
    - humanname: CentOS-7-Updates
    - comments:
      - '## CentOS 7 Updates support used with Amazon Linux 2'
    - mirrorlist: http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=updates
    - gpgcheck: 1
    - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7


centos7-extras:
  pkgrepo.managed:
    - humanname: CentOS-7-Extras
    - comments:
      - '## CentOS 7 Extras support used with Amazon Linux 2'
    - mirrorlist: http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=extras
    - gpgcheck: 1
    - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7


centos7-epel:
  pkgrepo.managed:
    - humanname: CentOS-7-Extra-Packages-for-Enterprise-Linux
    - comments:
      - '## Extra Packages for Enterprise Linux 7 support used with Amazon Linux 2'
    - mirrorlist: https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=x86_64
    - gpgcheck: 1
    - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7


build_additional_pkgs_{{build_cfg.build_release}}:
  pkg.installed:
    - pkgs:
      - mock
      - python2-gnupg
      - python2-rpm-macros
      - python3-rpm-macros


build_additional_{{build_cfg.build_release}}_{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_additional_pkgs_{{build_cfg.build_release}}


build_salt_mock_prefs_rm:
  file.absent:
    - name: {{amzn2_salt_mock_cfg}}
    - require:
      - file: centos7_deps


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
