# Import base config
{% import "setup/redhat/map.jinja" as build_cfg %}

include:
  - setup.redhat.rhel8.rhel8_setup
  - setup.redhat.rhel8.gpg_agent

