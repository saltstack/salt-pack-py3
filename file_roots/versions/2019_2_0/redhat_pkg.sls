{% import "setup/redhat/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'rhel7' %}

    - pkg.python-cherrypy.5_6_0.rhel7
    - pkg.python-ioflo.1_3_8.rhel7
    - pkg.python-libcloud.2_0_0.rhel7
    - pkg.python-libnacl.1_6_1.rhel7
    - pkg.python-m2crypto.0_31_0.rhel7
    - pkg.python-pyzmq.15_3_0.rhel7
    - pkg.python-raet.0_6_6.rhel7
    - pkg.python-timelib.0_2_4.rhel7
    - pkg.salt.2019_2_0.rhel7

{% elif buildcfg.build_release == 'fedora' %}

    - pkg.salt.2019_2_0.fedora

{% endif %}
