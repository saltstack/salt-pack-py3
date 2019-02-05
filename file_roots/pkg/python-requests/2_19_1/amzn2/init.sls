{% import "setup/amazon/map.jinja" as buildcfg %}
{% import "setup/macros.jinja" as macros with context %}
{% set pkg_data = salt["pillar.get"]("pkgbuild_registry:" ~ buildcfg.build_release, {}) %}
{% set force = salt["pillar.get"]("pkgbuild_force.all", False) or salt["pillar.get"]("pkgbuild_force." ~ slspath, False) %}
{% set sls_name = "python-requests" %}
{% set pypi_name = "requests" %}

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
    - spec: salt://{{slspath}}/spec/{{pkg_name}}.spec
    - template: jinja
    - tgt: {{buildcfg.build_tgt}}

{{ macros.build_deps(sls_name, pkg_data) }}
{{ macros.requires(sls_name, pkg_data) }}

    - sources:
      - salt://{{slspath}}/sources/Don-t-inject-pyopenssl-into-urllib3.patch
      - salt://{{slspath}}/sources/dont-import-OrderedDict-from-urllib3.patch
      - salt://{{slspath}}/sources/requests-2.12.4-tests_nonet.patch
      - salt://{{slspath}}/sources/Remove-tests-that-use-the-tarpit.patch
      - salt://{{slspath}}/sources/patch-requests-certs.py-to-use-the-system-CA-bundle.patch
      - salt://{{slspath}}/sources/requests-v2.19.1.tar.gz
##      - {{ macros.pypi_source(pypi_name, version) }}
{% endif %}
