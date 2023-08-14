# set version to build
{% set build_version = '3005_2' %}


{% if build_version != '' %}
include:
    - versions.{{build_version}}.pkgbuild
{% endif %}
