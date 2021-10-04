# Import base config
{% import "setup/debian/map.jinja" as build_cfg %}

include:
  - setup.debian.debian11.debian11_setup
  - setup.debian.gpg_agent

