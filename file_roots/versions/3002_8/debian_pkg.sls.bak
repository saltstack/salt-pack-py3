{% import "setup/debian/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'debian11' %}

    - pkg.python-contextvars.2_4.debian11
    - pkg.python-immutables.0_14.debian11
    - pkg.salt.master.debian11

{% elif buildcfg.build_release == 'debian10' %}

    - pkg.python-contextvars.2_4.debian10
    - pkg.python-immutables.0_14.debian10
    - pkg.salt.master.debian10

{% elif buildcfg.build_release == 'debian9' %}

    - pkg.python-contextvars.2_4.debian9
    - pkg.python-immutables.0_14.debian9
    - pkg.python-jinja2.2_9_4.debian9
    - pkg.python-msgpack.0_6_2.debian9
    - pkg.python-pycryptodome.3_6_1.debian9
    - pkg.python-pyzmq.17_1_2.debian9
    - pkg.salt.master.debian9

{% endif %}
