{% import "setup/redhat/map.jinja" as buildcfg %}
{% import "setup/macros.jinja" as macros with context %}
{% set pkg_data = salt["pillar.get"]("pkgbuild_registry:" ~ buildcfg.build_release, {}) %}
{% set force = salt["pillar.get"]("pkgbuild_force.all", False) or salt["pillar.get"]("pkgbuild_force." ~ slspath, False) %}
{% set sls_name = "python36" %}
{% set pypi_name = "python" %}

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
      - salt://{{slspath}}/sources/00317-CVE-2019-5010.patch
      - salt://{{slspath}}/sources/00292-restore-PyExc_RecursionErrorInst-symbol.patch
      - salt://{{slspath}}/sources/00274-fix-arch-names.patch
      - salt://{{slspath}}/sources/00262-pep538_coerce_legacy_c_locale.patch
      - salt://{{slspath}}/sources/00251-change-user-install-location.patch
      - salt://{{slspath}}/sources/00205-make-libpl-respect-lib64.patch
      - salt://{{slspath}}/sources/00178-dont-duplicate-flags-in-sysconfig.patch
      - salt://{{slspath}}/sources/00170-gc-assertions.patch
      - salt://{{slspath}}/sources/00163-disable-parts-of-test_socket-in-rpm-build.patch
      - salt://{{slspath}}/sources/00160-disable-test_fs_holes-in-rpm-build.patch
      - salt://{{slspath}}/sources/00155-avoid-ctypes-thunks.patch
      - salt://{{slspath}}/sources/00132-add-rpmbuild-hooks-to-unittest.patch
      - salt://{{slspath}}/sources/00111-no-static-lib.patch
      - salt://{{slspath}}/sources/00102-lib64.patch
      - salt://{{slspath}}/sources/00001-rpath.patch
      - salt://{{slspath}}/sources/idle3.desktop
      - salt://{{slspath}}/sources/idle3.appdata.xml
      - salt://{{slspath}}/sources/check-pyc-and-pyo-timestamps.py
      - salt://{{slspath}}/sources/Python-3.6.8.tar.xz
{% endif %}
