{% import "setup/ubuntu/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'ubuntu1804' %}

    - pkg.python-m2crypto.0_31_0.ubuntu1804
    - pkg.salt.3000_8.ubuntu1804

{% elif buildcfg.build_release == 'ubuntu1604' %}

    - pkg.python-libcloud.1_5_0.ubuntu1604
    - pkg.python-msgpack.0_6_2.ubuntu1604
    - pkg.salt.3000_8.ubuntu1604

{% endif %}
