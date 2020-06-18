# Import base config
{% import "setup/ubuntu/map.jinja" as build_cfg %}

include:
  - setup.ubuntu.ubuntu2004.ubuntu2004_setup
  - setup.ubuntu.gpg_agent
