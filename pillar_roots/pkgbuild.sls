# set version to build
{% set build_version = '2019_2_2' %}


include:
{% if build_version != '' %}
    - versions.{{build_version}}.pkgbuild
{% else %}
    - pkgbuild
{% endif %}
