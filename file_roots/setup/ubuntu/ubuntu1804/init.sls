# Import base config
{% import "setup/ubuntu/map.jinja" as build_cfg %}

include:
  - setup.ubuntu.ubuntu1804.ubuntu1804_setup
  - setup.ubuntu.gpg_agent
