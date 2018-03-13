{% import "setup/redhat/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'rhel7' %}

## EPEL supplying python3.4, hence if EPEL provide no need to package

    - pkg.libsodium.1_0_5.rhel7
    - pkg.libtomcrypt.1_17.rhel7          ## RH7 extras 1.17-26
    - pkg.libtommath.0_42_0.rhel7         ## RH7 extras 0.42.0-6
    - pkg.openpgm.5_2_122.rhel7
    - pkg.python-chardet.2_2_1.rhel7        ## RH7 EPEL py34 2.3.0-3, 2.2.1-1.el7_1 base
    - pkg.python-cherrypy.5_6_0.rhel7
    - pkg.python-crypto.2_6_1.rhel7         ## RH7 EPEL py34 2.6.1-13
    - pkg.python-pycryptodome.3_4_3.rhel7
##    - pkg.python-enum34.1_0.rhel7         ## RH7 base 1.0.4-1
##    - pkg.python-futures.3_0_3.rhel7      ## not needed for Python 3
##    - pkg.python-impacket.0_9_14.rhel7    ## only need for disabled winexe, has no py 3 compat
    - pkg.python-ioflo.1_3_8.rhel7
    - pkg.python-libcloud.2_0_0.rhel7
    - pkg.python-libnacl.1_4_3.rhel7
    - pkg.python-m2crypto.0_27_0.rhel7
    - pkg.python-msgpack.0_4_6.rhel7        ## RH7 EPEL py34 0.4.8-1
    - pkg.python-mock.1_0_1.rhel7           ## RH7 EPEL py34 1.0.1-9
    - pkg.python-psutil.2_2_1.rhel7         ## RH7 EPEL py34 2.2.1-3
    - pkg.python-pyzmq.15_3_0.rhel7
    - pkg.python-raet.0_6_6.rhel7
    - pkg.python-requests.2_6_0.rhel7       ## RH7 EPEL py34 2.12.3-1
    - pkg.python-simplejson.3_3_3.rhel7     ## RH7 EPEL py34 3.10.0-1
    - pkg.python-tornado.4_2_1.rhel7        ## RH7 EPEL py34 4.4.2-1, 4.2.1-1 base
    - pkg.python-timelib.0_2_4.rhel7
    - pkg.python-urllib3.1_10_4.rhel7
    - pkg.python-yaml.3_11.rhel7
    - pkg.salt.2018_3.rhel7
##    - pkg.winexe.1_1.rhel7
    - pkg.zeromq.4_1_4.rhel7

{% elif buildcfg.build_release == 'rhel6' %}

## RH6 since building for Python 2 implies need Python 3.4 anyway
## EPEL supplying python3.4, hence if EPEL provide no need to package

    - pkg.babel.0_9_4.rhel6
    - pkg.libsodium.0_4_5.rhel6             ## RH6 EPEL 0.4.5-3
    - pkg.libtomcrypt.1_17.rhel6            ## RH6 EPEL 1.17-25 
    - pkg.libtommath.0_42_0.rhel6           ## RH6 EPEL 0.42.0-5
    - pkg.libyaml.0_1_3.rhel6               ## RH6 base  0.1.3-4
    - pkg.pciutils.3_1_10.rhel6             ## RH6 anaconda 3.1.10-4
    - pkg.python27.2_7_13.rhel6
    - pkg.python-backports.1_0.rhel6        ## RH6 base 1.0-5
    - pkg.python-backports-ssl_match_hostname.3_4_0_2.rhel6     ## RH6 base 3.4.0.2-5
    - pkg.python-chardet.2_2_1.rhel6        ## RH6 EPEL py34 2.3.0-3
    - pkg.python-cherrypy.5_6_0.rhel6   
    - pkg.python-crypto.2_6_1.rhel6
{% if buildcfg.build_arch == 'x86_64' %}
    - pkg.python-pycryptodome.3_4_3.rhel6
{% endif %}
    - pkg.python-enum34.1_0.rhel6           ## RH6 EPEL 1.0-4
    - pkg.python-futures.3_0_3.rhel6
    - pkg.python-importlib.1_0_2.rhel6      ## RH6 EPEL 1.0.4-1
    - pkg.python-ioflo.1_3_8.rhel6
    - pkg.python-impacket.0_9_14.rhel6
    - pkg.python-jinja2.2_8_1.rhel6         ## RH6 EPEL py34 2.8-2
    - pkg.python-libcloud.2_0_0.rhel6   
    - pkg.python-libnacl.1_4_3.rhel6
    - pkg.python-markupsafe.0_11.rhel6      ## RH6 EPEL py34 0.23-1
    - pkg.python-msgpack.0_4_6.rhel6        ## RH6 EPEL 0.4.6-1
    - pkg.python-mock.1_0_1.rhel6           ## RH6 EPEL py34 1.0.1-10
    - pkg.python-nose.1_3_7.rhel6           ## RH6 EPEL py34 1.3.7-2
    - pkg.python-pip.9_0_1.rhel6
    - pkg.python-psutil.5_2_2.rhel6
    - pkg.python-py.1_4_27.rhel6            ## RH6 EPEL py34 1.4.30-2
    - pkg.python-pycurl.7_19_0.rhel6        ## RH6 EPEL py34 7.43.0-5
    - pkg.python-pyzmq.14_5_0.rhel6
    - pkg.python-raet.0_6_6.rhel6
    - pkg.python-requests.2_7_0.rhel6       ## RH6 EPEL py34 2.12.3-1
    - pkg.python-setuptools.33_1_1.rhel6    ## RH6 EPEL py34 19.6.2-2
    - pkg.python-six.1_9_0.rhel6            ## RH6 EPEL py34 1.10.0-1
    - pkg.python-timelib.0_2_4.rhel6
    - pkg.python-tornado.4_2_1.rhel6        ## RH6 EPEL py34 4.4.2-1
    - pkg.python-unittest2.1_1_0.rhel6
    - pkg.python-urllib3.1_10_4.rhel6       ## RH6 EPEL py34 1.19.1-3
    - pkg.python-yaml.3_11.rhel6            ## RH6 EPEL py34 3.11-2
    - pkg.salt.2018_3.rhel6
##    - pkg.winexe.1_1.rhel6
    - pkg.yum-utils.1_1_30.rhel6
    - pkg.zeromq.4_0_5.rhel6

{% elif buildcfg.build_release == 'fedora' %}

    - pkg.salt.2018_3.fedora

{% endif %}
