{% import "setup/redhat/map.jinja" as buildcfg %}
{% import "setup/macros.jinja" as macros with context %}
{% set pkg_data = salt["pillar.get"]("pkgbuild_registry:" ~ buildcfg.build_release, {}) %}
{% set force = salt["pillar.get"]("pkgbuild_force.all", False) or salt["pillar.get"]("pkgbuild_force." ~ slspath, False) %}
{% set sls_name = "python-jmespath" %}
{% set pypi_name = "jmespath" %}

{% set pkg_info = pkg_data.get(sls_name, {}) %}
{% if "version" in pkg_info %}
  {% set pkg_name = pkg_info.get("name", sls_name) %}
  {% set version, release = pkg_info["version"].split("-", 1) %}
  {% if pkg_info.get("noarch", False) %}
    {% set arch = "noarch" %}
  {% else %}
    {% set arch = buildcfg.build_arch %}
  {% endif %}

{{ macros.includes(sls_name, pkg_data) }}

{{sls_name}}-{{version}}:
  pkgbuild.built:
    - runas: {{buildcfg.build_runas}}
    - force: {{force}}

{{ macros.results(sls_name, pkg_data) }}

    - dest_dir: {{buildcfg.build_dest_dir}}
    - spec: salt://{{slspath}}/spec/python-{{pypi_name}}.spec
    - template: jinja
    - tgt: {{buildcfg.build_tgt}}

{{ macros.build_deps(sls_name, pkg_data) }}
{{ macros.requires(sls_name, pkg_data) }}

    - sources:
      - salt://{{slspath}}/sources/{{pypi_name}}-{{version}}.tar.gz
      - salt://{{slspath}}/sources/LICENSE.txt
      - salt://{{slspath}}/sources/MANIFEST.in
      - salt://{{slspath}}/sources/PKG-INFO
      - salt://{{slspath}}/sources/README.rst
      - salt://{{slspath}}/sources/setup.cfg
      - salt://{{slspath}}/sources/setup.py
      - salt://{{slspath}}/sources/bin/jp.py
      - salt://{{slspath}}/sources/jmespath/visitor.py
      - salt://{{slspath}}/sources/jmespath/ast.py
      - salt://{{slspath}}/sources/jmespath/functions.py
      - salt://{{slspath}}/sources/jmespath/lexer.py
      - salt://{{slspath}}/sources/jmespath/__init__.py
      - salt://{{slspath}}/sources/jmespath/parser.py
      - salt://{{slspath}}/sources/jmespath/exceptions.py
      - salt://{{slspath}}/sources/jmespath/compat.py
      - salt://{{slspath}}/sources/jmespath.egg-info/pbr.json
      - salt://{{slspath}}/sources/jmespath.egg-info/dependency_links.txt
      - salt://{{slspath}}/sources/jmespath.egg-info/top_level.txt
      - salt://{{slspath}}/sources/jmespath.egg-info/PKG-INFO
      - salt://{{slspath}}/sources/jmespath.egg-info/SOURCES.txt
      - salt://{{slspath}}/sources/tests/test_compliance.py
      - salt://{{slspath}}/sources/tests/test_parser.py
      - salt://{{slspath}}/sources/tests/__init__.py
##      - {{ macros.pypi_source(pypi_name, version) }}
{% endif %}

