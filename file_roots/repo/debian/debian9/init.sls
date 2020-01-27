{% import "setup/debian/map.jinja" as buildcfg %}

{% set repo_keyid = pillar.get('keyid', 'None') %}

include:
  - repo.debian

{{buildcfg.build_dest_dir}}:
  pkgbuild.repo:
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
        LABEL : 'salt_debian9'
        SUITE: 'oldstable'
        CODENAME : 'stretch'
{%- if buildcfg.build_arch == 'armhf' %}
        ARCHS : '{{buildcfg.build_arch}} source'
{%- else %}
        ARCHS : 'amd64 i386 source'
{%- endif %}
        COMPONENTS : 'main'
{%- if buildcfg.build_py3 %}
        DESCRIPTION : 'SaltStack Debian 9 Python 3 package repo'
{%- else %}
        DESCRIPTION : 'SaltStack Debian 9 Python 2 package repo'
{%- endif %}

