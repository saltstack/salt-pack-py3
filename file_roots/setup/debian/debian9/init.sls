# Import base config
{% import "setup/debian/map.jinja" as build_cfg %}

include:
  - setup.debian.debian9.debian9_setup
  - setup.debian.gpg_agent

