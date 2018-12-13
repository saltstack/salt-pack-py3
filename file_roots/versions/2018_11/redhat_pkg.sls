{% import "setup/redhat/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'rhel7' %}

    - pkg.libsodium.1_0_16.rhel7
##    - pkg.libtomcrypt.1_17.rhel7      ## extras   1.17-26.el7
##    - pkg.libtommath.0_42_0.rhel7     ## extras   0.42.0-6.el7
    - pkg.openpgm.5_2_122.rhel7
##    - pkg.python-chardet.2_2_1.rhel7  ## EPEL python34-chardet 2.3.0-4.el7, python36-chardet 2.3.0-4.el7
    - pkg.python-cherrypy.5_6_0.rhel7
##    - pkg.python-crypto.2_6_1.rhel7   ## EPEL python34-crypto 2.6.1-13.el7
    - pkg.python-enum34.1_0.rhel7       ## is this even needed ???
##    - pkg.python-futures.3_0_3.rhel7  ## not even needed
    - pkg.python-ioflo.1_3_8.rhel7
    - pkg.python-libcloud.2_0_0.rhel7
    - pkg.python-libnacl.1_6_1.rhel7
    - pkg.python-m2crypto.0_28_2.rhel7
##    - pkg.python-msgpack.0_4_6.rhel7  ## EPEL python34-msgpack 0.5.6-4.el7
##    - pkg.python-mock.1_0_1.rhel7     ## EPEL python34-mock 1.0.1-9.el7
    - pkg.python-pycryptodome.3_6_1.rhel7
##    - pkg.python-psutil.2_2_1.rhel7   ## EPEL python34-psutil 2.2.1-4.el7, python36-psutil 2.2.1-4.el7
    - pkg.python-pyzmq.15_3_0.rhel7
    - pkg.python-raet.0_6_6.rhel7
##    - pkg.python-simplejson.3_3_3.rhel7   ## EPEL python34-simplejson 3.10.0-1.el7
    - pkg.python-timelib.0_2_4.rhel7
##    - pkg.python-tornado.4_2_1.rhel7  ## EPEL python34-tornado 4.4.2-1.el7
##    - pkg.python-typing.3_5_2_2.rhel7 ## EPEL python34-typing 3.5.2.2-3.el7
##    - pkg.python-urllib3.1_10_4.rhel7 ## EPEL python34-urllib3 1.19.1-4.el7, python36-urllib3 1.19.1-4.el7
    - pkg.python-yaml.3_11.rhel7
    - pkg.salt.2018_11.rhel7
    - pkg.zeromq.4_1_4.rhel7

{% elif buildcfg.build_release == 'fedora' %}

    - pkg.salt.2018_11.fedora

{% endif %}
