{% import "setup/ubuntu/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'ubuntu2004' %}

    - pkg.python-contextvars.2_4.ubuntu2004
    - pkg.python-immutables.0_14.ubuntu2004
    - pkg.salt.3003_5.ubuntu2004

{% elif buildcfg.build_release == 'ubuntu1804' %}

    - pkg.python-contextvars.2_4.ubuntu1804
    - pkg.python-immutables.0_14.ubuntu1804
    - pkg.python-m2crypto.0_31_0.ubuntu1804
    - pkg.python-pyzmq.17_1_2.ubuntu1804
    - pkg.salt.3003_5.ubuntu1804

{% elif buildcfg.build_release == 'ubuntu1604' %}

    - pkg.python-contextvars.2_4.ubuntu1604
    - pkg.python-immutables.0_14.ubuntu1604
    - pkg.python-libcloud.1_5_0.ubuntu1604
    - pkg.python-msgpack.0_6_2.ubuntu1604
    - pkg.python-pyzmq.17_1_2.ubuntu1604
    - pkg.python-pycryptodome.3_4_7.ubuntu1604
    - pkg.python-distro.1_0_1.ubuntu1604
    - pkg.salt.3003_5.ubuntu1604

{% endif %}
