{% import "setup/ubuntu/map.jinja" as buildcfg %}
{% set force = salt['pillar.get']('build_force.all', False) or salt['pillar.get']('build_force.' ~ slspath, False) %}
{% set pypi_name = 'distro' %}
{% set name = 'python-' ~ pypi_name %}
{% set name3 = 'python3-' ~ pypi_name %}
{% set version = '1.5.0' %}
{% set release_ver = '1' %}

{{name}}-{{version.replace('.', '_')}}:
  pkgbuild.built:
    - runas: {{buildcfg.build_runas}}
    - results:
      - {{name}}_{{version}}-{{release_ver}}_all.deb
      - {{name3}}_{{version}}-{{release_ver}}_all.deb
      - {{name}}_{{version}}-{{release_ver}}.dsc
      - {{pypi_name}}-{{version}}.tar.gz
    - force: {{force}}
    - dest_dir: {{buildcfg.build_dest_dir}}
    - spec: salt://{{slspath}}/spec/{{name}}_{{version}}-{{release_ver}}.dsc
    - tgt: {{buildcfg.build_tgt}}
    - template: jinja
    - env:
        DEB_BUILD_OPTIONS : 'nocheck'
    - sources:
      - salt://{{slspath}}/sources/{{pypi_name}}-{{version}}.tar.gz

