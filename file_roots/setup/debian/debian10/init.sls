# Import base config
{% import "setup/debian/map.jinja" as build_cfg %}

include:
  - setup.debian.debian10.debian10_setup
  - setup.debian.gpg_agent

