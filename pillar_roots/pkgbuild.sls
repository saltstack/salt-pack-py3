# set version to build
<<<<<<< HEAD
{% set build_version = '3005_4' %}
=======
{% set build_version = '3005_5' %}
>>>>>>> develop


{% if build_version != '' %}
include:
    - versions.{{build_version}}.pkgbuild
{% endif %}
