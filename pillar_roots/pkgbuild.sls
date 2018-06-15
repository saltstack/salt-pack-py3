# set version to build
<<<<<<< HEAD
{% set build_version = '2018_3_0' %}
=======
{% set build_version = '2018_3_1' %}
>>>>>>> develop


{% if build_version != '' %}
include:
    - .versions.{{build_version}}.pkgbuild
{% endif %}
