{% import "setup/ubuntu/map.jinja" as buildcfg %}

{% set repo_keyid = pillar.get('keyid', 'None') %}

include:
  - repo.ubuntu

{{buildcfg.build_dest_dir}}:
  pkgbuild.repo:
    - use_passphrase: {{buildcfg.repo_use_passphrase}}
    - gnupghome: {{buildcfg.build_gpg_keydir}}
    - runas: {{buildcfg.build_runas}}
    - timeout: {{buildcfg.repo_sign_timeout}}
{% if repo_keyid != 'None' %}
    - keyid: {{repo_keyid}}
    - use_passphrase: {{buildcfg.repo_use_passphrase}}
{% endif %}
    - env:
{%- if buildcfg.repo_use_passphrase %}
        OPTIONS : 'ask-passphrase'
{%- endif %}
        ORIGIN : 'SaltStack'
        LABEL : 'salt_ubuntu2004'
        CODENAME : 'focal'
{%- if build_cfg.build_arch == 'arm64' %}
        ARCHS : 'arm64 source'
{%- else %}
        ARCHS : 'amd64 source'
{%- endif %}
        COMPONENTS : 'main'
        DESCRIPTION : 'SaltStack Ubuntu 20.04 Python 3 package repo'

