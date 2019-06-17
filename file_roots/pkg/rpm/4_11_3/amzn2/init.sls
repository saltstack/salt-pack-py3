{% import "setup/amazon/map.jinja" as buildcfg %}
{% import "setup/macros.jinja" as macros with context %}
{% set pkg_data = salt["pillar.get"]("pkgbuild_registry:" ~ buildcfg.build_release, {}) %}
{% set force = salt["pillar.get"]("pkgbuild_force.all", False) or salt["pillar.get"]("pkgbuild_force." ~ slspath, False) %}
{% set sls_name = "rpm" %}
{% set src_name = "rpm" %}

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
      - salt://{{slspath}}/sources/{{src_name}}-{{version}}.tar.bz2
      - salt://{{slspath}}/sources/libsymlink.attr
      - salt://{{slspath}}/sources/rpm-4.10.0-dwz-debuginfo.patch
      - salt://{{slspath}}/sources/rpm-4.10.90-rpmlib-filesystem-check.patch
      - salt://{{slspath}}/sources/rpm-4.10.0-minidebuginfo.patch
      - salt://{{slspath}}/sources/rpm-4.11.1-sepdebugcrcfix.patch
      - salt://{{slspath}}/sources/rpm-4.11.1-libtool-ppc64le.patch
      - salt://{{slspath}}/sources/rpm-4.11.3-EVR-validity-check.patch
      - salt://{{slspath}}/sources/rpm-4.11.3-disable-collection-plugins.patch
      - salt://{{slspath}}/sources/rpm-4.11.3-Initialize-plugins-based-on-DSO-discovery.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-define-PY_SSIZE_T_CLEAN.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-defattr-permissions.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-CVE-2014-8118.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-color-skipping.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-chmod.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-broken-pipe.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-bdb-warings.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-Add-noplugins.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-Add-make_build-macro.patch
      - salt://{{slspath}}/sources/rpm-4.11.3-update-config.guess.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-Handle-line-continuation.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-fix-stripping-of-binaries.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-Fix-Python-hdr-refcount.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-Fix-off-by-one-base64.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-fix-debuginfo-creation.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-filter-soname-deps.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-export-verifysigs-to-python.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-elem-progress.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-do-not-filter-ld64.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-dirlink-verify.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-deprecate-addsign.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-perl.req-skip-my-var-block.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-perl.req-4.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-perl.req-3.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-perl.req-2.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-perl.req-1.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-parametrized-macro-invocations.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-no-longer-config.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-multitheaded_xz.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-move-rename.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-minidebuginfo-ppc64.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-man-systemd-inhibit.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-verify-data-range.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-systemd-inhibit.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-sources-to-lua-variables.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-skipattr.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-setperms-setugids-mutual-exclusion.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-reinstall.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-quiet-signing.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-python-binding-test-case.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-provide-audit-events.patch
      - salt://{{slspath}}/sources/rpm-4.8.0-ignore-multiline2.patch
      - salt://{{slspath}}/sources/rpm-4.7.1-geode-i686.patch
      - salt://{{slspath}}/sources/rpm-4.6.0-niagara.patch
      - salt://{{slspath}}/sources/rpm-4.14.x-Add-justdb-to-the-erase-man.patch
      - salt://{{slspath}}/sources/rpm-4.13.x-writable-tmp-dir.patch
      - salt://{{slspath}}/sources/rpm-4.13.x-RPMCALLBACK_ELEM_PROGRESS-available-header.patch
      - salt://{{slspath}}/sources/rpm-4.13.x-Make-the-stftime-buffer-big-enuff.patch
      - salt://{{slspath}}/sources/rpm-4.13.x-increase_header_size.patch
      - salt://{{slspath}}/sources/rpm-4.13.x-Implement-noconfig-query.patch
      - salt://{{slspath}}/sources/rpm-4.13.x-fix_find_debuginfo_opts_g.patch
      - salt://{{slspath}}/sources/rpm-4.13.x-enable_noghost_option.patch
      - salt://{{slspath}}/sources/rpm-4.12.x-rpmSign-return-value-correction.patch
      - salt://{{slspath}}/sources/rpm-4.11.x-weakdep-tags.patch
      - salt://{{slspath}}/sources/rpm-4.9.90-no-man-dirs.patch
      - salt://{{slspath}}/sources/rpm-4.9.90-fedora-specspo.patch
      - salt://{{slspath}}/sources/rpm-4.9.90-armhfp.patch
      - salt://{{slspath}}/sources/rpm-4.9.1.1-ld-flags.patch
      - salt://{{slspath}}/sources/rpm-4.9.0-armhfp-logic.patch
      - salt://{{slspath}}/sources/rpm-4.8.x-error-in-log.patch
      - salt://{{slspath}}/sources/rpm-4.8.1-use-gpg2.patch

{% endif %}
