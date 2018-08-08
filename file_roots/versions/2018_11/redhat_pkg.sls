{% import "setup/redhat/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'rhel7' %}

    - pkg.libsodium.1_0_16.rhel7
    - pkg.libtomcrypt.1_17.rhel7
    - pkg.libtommath.0_42_0.rhel7
    - pkg.openpgm.5_2_122.rhel7
    - pkg.python-chardet.2_2_1.rhel7
    - pkg.python-cherrypy.5_6_0.rhel7
    - pkg.python-crypto.2_6_1.rhel7
    - pkg.python-enum34.1_0.rhel7
    - pkg.python-futures.3_0_3.rhel7
    - pkg.python-ioflo.1_3_8.rhel7
    - pkg.python-libcloud.2_0_0.rhel7
    - pkg.python-libnacl.1_6_1.rhel7
    - pkg.python-m2crypto.0_28_2.rhel7
    - pkg.python-msgpack.0_4_6.rhel7
    - pkg.python-mock.1_0_1.rhel7
    - pkg.python-pycryptodome.3_6_1.rhel7
    - pkg.python-psutil.2_2_1.rhel7
    - pkg.python-pyzmq.15_3_0.rhel7
    - pkg.python-raet.0_6_6.rhel7
    - pkg.python-requests.2_6_0.rhel7
    - pkg.python-simplejson.3_3_3.rhel7
    - pkg.python-timelib.0_2_4.rhel7
    - pkg.python-tornado.4_2_1.rhel7
    - pkg.python-typing.3_5_2_2.rhel7
    - pkg.python-urllib3.1_10_4.rhel7
    - pkg.python-yaml.3_11.rhel7
    - pkg.salt.2018_11.rhel7
    - pkg.zeromq.4_1_4.rhel7

{% elif buildcfg.build_release == 'fedora' %}

    - pkg.salt.2018_11.fedora

{% endif %}
