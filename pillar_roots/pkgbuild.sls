# set version to build
{% set build_version = '3004rc1' %}


{% if build_version != '' %}
include:
    - versions.{{build_version}}.pkgbuild
{% endif %}
