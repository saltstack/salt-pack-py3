# set version to build
{% set build_version = '3001_6' %}


{% if build_version != '' %}
include:
    - versions.{{build_version}}.pkgbuild
{% endif %}
