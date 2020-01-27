{% import "setup/amazon/map.jinja" as buildcfg %}

{% set repo_keyid = pillar.get('keyid', 'None') %}

include:
  - repo.amazon

{{buildcfg.build_dest_dir}}:
  pkgbuild.repo:
    - gnupghome: {{buildcfg.build_gpg_keydir}}
    - runas: {{buildcfg.build_runas}}
    - timeout: {{buildcfg.repo_sign_timeout}}
    - order: last
{% if repo_keyid != 'None' %}
    - keyid: {{repo_keyid}}
    - use_passphrase: {{buildcfg.repo_use_passphrase}}
{% endif %}
    - env:
{%- if buildcfg.build_py3 %}
        ORIGIN : 'SaltStack Amazon Linux 2 Python 3 package repo'
{% else %}
        ORIGIN : 'SaltStack Amazon Linux 2 Python 2 package repo'
{% endif %}
