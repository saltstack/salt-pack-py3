# state file to setup gpg-agent and config on minion
{% import "setup/redhat/map.jinja" as build_cfg %}

{% set pkg_pub_key_file = pillar.get('gpg_pkg_pub_keyname', None) %}
{% set pkg_priv_key_file = pillar.get('gpg_pkg_priv_keyname', None) %}

{% if pkg_pub_key_file!= 'None' and pkg_priv_key_file != 'None' %}

{% set gpg_key_dir = build_cfg.build_gpg_keydir %}
{% set gpg_config_file = gpg_key_dir ~ '/gpg.conf' %}
{% set gpg_tty_info = gpg_key_dir ~ '/gpg-tty-info-salt' %}
{% set gpg_agent_config_file = gpg_key_dir ~ '/gpg-agent.conf' %}

{% set write_env_file_prefix = '' %}
{% set write_env_file = '' %}
{% set pinentry_parms = '
        pinentry-timeout 30
        allow-loopback-pinentry' %}
{% set pinentry_text = 'pinentry-program /usr/bin/pinentry-tty' %}
{% set kill_gpg_agent_text = 'gpgconf --kill gpg-agent' %}

{% set pkg_pub_key_absfile = gpg_key_dir ~ '/' ~ pkg_pub_key_file %}
{% set pkg_priv_key_absfile = gpg_key_dir ~ '/' ~ pkg_priv_key_file %}

{% set gpg_agent_log_file = build_cfg.build_homedir ~ '/gpg-agent.log' %}

{% set gpg_agent_text = '# enable-ssh-support
        ' ~ write_env_file  ~ '
        default-cache-ttl 600
        default-cache-ttl-ssh 600
        max-cache-ttl 600
        max-cache-ttl-ssh 600
        allow-preset-passphrase
        daemon
        debug-all
        ## debug-pinentry
        log-file ' ~ gpg_agent_log_file ~ '
        verbose
        # PIN entry program
        ' ~ pinentry_text ~ pinentry_parms
%}

{% set gpg_agent_script_file = build_cfg.build_homedir ~ '/gpg-agent_start.sh' %}

## don't name kill script with gpg-agent as part of name, makes script easier
{% set gpg_ps_kill_script_file = build_cfg.build_homedir ~ '/gpg_kill.sh' %}

{% set gpg_agent_script_text = '#!/bin/sh
        gpgconf --launch gpg-agent
        GPG_TTY=/dev/pts/0
        export GPG_TTY
        echo "GPG_TTY=/dev/pts/0" > ' ~ gpg_tty_info ~ '
        sleep 5
' %}

## set xauth/export values
{% set xauth_text = build_cfg.build_runas %}
{% set xauth_dir = build_cfg.build_homedir ~ '/.xauth' %}
{% set xauth_file = xauth_dir ~ '/export' %}


gpg_agent_stop:
  cmd.run:
    - name: {{kill_gpg_agent_text}}
    - use_vt: True
    - onlyif: ps -ef | grep -v 'grep' | grep  gpg-agent


gpg_dir_rm:
  cmd.run:
    - name: rm -fR {{gpg_key_dir}}
    - use_vt: True


gpg_clear_agent_log:
  file.absent:
    - name: {{gpg_agent_log_file}}


gpg_agent_script_file_rm:
  file.absent:
    - name: {{gpg_agent_script_file}}


gpg_ps_kill_script_file_rm:
  file.absent:
    - name: {{gpg_ps_kill_script_file}}


xauth_kill_file:
  file.absent:
    - name: {{xauth_file}}


xauth_ensure_file:
  file.managed:
    - name: {{xauth_file}}
    - dir_mode: 700
    - mode: 644
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True
    - contents: {{xauth_text}}


manage_priv_key:
  file.managed:
    - name: {{pkg_priv_key_absfile}}
    - dir_mode: 700
    - mode: 600
    - contents_pillar: gpg_pkg_priv_key
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True


manage_pub_key:
  file.managed:
    - name: {{pkg_pub_key_absfile}}
    - dir_mode: 700
    - mode: 644
    - contents_pillar: gpg_pkg_pub_key
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True


gpg_conf_file_exists:
  file.managed:
    - name: {{gpg_config_file}}
    - dir_mode: 700
    - mode: 644
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True
    - contents: 'use-agent'


gpg_tty_file_exists:
  file.managed:
    - name: {{gpg_tty_info}}
    - dir_mode: 700
    - mode: 644
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True
    - contents: ''


gpg_agent_conf_file:
  file.managed:
    - name: {{gpg_agent_config_file}}
    - dir_mode: 700
    - mode: 644
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True
    - contents: |
        {{gpg_agent_text}}


gpg_agent_script_file_exists:
  file.managed:
    - name: {{gpg_agent_script_file}}
    - dir_mode: 755
    - mode: 755
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True
    - contents: |
        {{gpg_agent_script_text}}


gpg_agent_stop2:
  module.run:
    - name: cmd.shell
    - cmd: {{kill_gpg_agent_text}}
    - runas: 'root'
    - onlyif: ps -ef | grep -v 'grep' | grep  gpg-agent
    - require:
      - file: gpg_agent_script_file_exists


## finding killall and gpgpconf to stop gpg-agent failing on Ubuntu 18.04
## even as root from the command line, reqs investigation
## explicit kill with gusto for now
gpg_agent_ps_kill_script_file_exists:
  file.managed:
    - name: {{gpg_ps_kill_script_file}}
    - dir_mode: 755
    - mode: 755
    - show_changes: False
    - user: {{build_cfg.build_runas}}
    - group: {{build_cfg.build_runas}}
    - makedirs: True
    - contents: |
        #!/bin/bash
        gpg_active=$(ps -ef | grep -v 'grep' | grep 'gpg-agent')
        IFS=$'\n'	# make newlines the only seperator
        if [[ -n "$gpg_active" ]]; then
            for gpg_line in $gpg_active; do
                kpid=$(echo "$gpg_line" | awk '{print $2}')
                kill -9 $kpid
                sleep 1
            done
        fi
        unset IFS


#ensure all gpg activity completed before killing gpg
gpg_agent_ps_kill_run:
  module.run:
    - name: cmd.shell
    - cmd: {{gpg_ps_kill_script_file}}
    - runas: 'root'
    - require:
      - file: manage_priv_key
      - file: manage_pub_key
      - file: gpg_conf_file_exists
      - file: gpg_tty_file_exists
      - file: gpg_agent_conf_file
      - file: gpg_agent_script_file_exists
      - module: gpg_agent_stop2
      - file: gpg_agent_ps_kill_script_file_exists


gpg_agent_start:
  module.run:
    - name: cmd.shell
    - cmd: {{gpg_agent_script_file}}
    - cwd: {{build_cfg.build_homedir}}
    - runas: {{build_cfg.build_runas}}
    - use_vt: True
    - require:
      - module: gpg_agent_ps_kill_run


gpg_load_pub_key:
  module.run:
    - name: gpg.import_key
    - kwargs:
        user: {{build_cfg.build_runas}}
        filename: {{pkg_pub_key_absfile}}
        gnupghome: {{gpg_key_dir}}
    - require:
        - module: gpg_agent_start


gpg_load_priv_key:
  module.run:
    - name: gpg.import_key
    - kwargs:
        user: {{build_cfg.build_runas}}
        filename: {{pkg_priv_key_absfile}}
        gnupghome: {{gpg_key_dir}}
    - require:
      - module: gpg_load_pub_key


ensure_gpg_rights:
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
      - module: gpg_load_priv_key


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

{% endif %}

