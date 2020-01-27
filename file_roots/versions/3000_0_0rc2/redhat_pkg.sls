{% import "setup/redhat/map.jinja" as buildcfg %}

##  EPEL-7 py3.4 supplies
### EPEL-7 py3.6 supplies
##  RHEL-8 py3.6.8 supplies
## B bootstrapped

include:
{% if buildcfg.build_release == 'rhel8' %}

    - pkg.Cython.0_29_6.rhel8               ## B
    - pkg.distribution-gpg-keys.1_30.rhel8  ## B
    - pkg.libsodium.1_0_17.rhel8            ## B EPEL-7 libsodium-1.0.17-1.el7
    - pkg.libunwind.1_3_1.rhel8             ## B
##    - pkg.libtomcrypt.1_17.rhel8            ## extras-7   1.17-26.el7      not needed since M2Crypto
##    - pkg.libtommath.0_42_0.rhel8           ## extras-7   0.42.0-6.el7     not needed since M2Crypto
    - pkg.openpgm.5_2_122.rhel8             ## B EPEL-7 openpgm-5.2.122--2.el7
    - pkg.mock.1_4_15.rhel8                 ## B
    - pkg.mock-core-configs.30_3.rhel8      ## B
##    - pkg.python-chardet.2_2_1.rhel8      ## @anaconda    python3-chardet.noarch  3.0.4-7.el8
    - pkg.python36.3_6_8.rhel7
    - pkg.python-cherrypy.5_6_0.rhel8       ## B
##    - pkg.python-crypto.2_6_1.rhel8       ## no pycrypto provided, cryptography 2.3-2.el8, since M2Crypto
    - pkg.python-distro.1_2_0.rhel8         ## B
    - pkg.python-funcsigs.1_0_2.rhel8       ## B
    - pkg.python-gnupg.0_4_4.rhel8          ## B
    - pkg.python-libcloud.2_4_0.rhel8       ## B
###    - pkg.python-libnacl.1_6_1.rhel8     - leave this to later if needed at all
    - pkg.python-m2crypto.0_33_0.rhel8      ## B
    - pkg.python-msgpack.0_6_1.rhel8        ## B EPEL-7 python36-msgpack 0.5.6-5.el7,doing latest
    - pkg.python-mock.2_0_0.rhel8           ## B EPEL-7 python36-mock-2.0.0-1.el7
    - pkg.python-pbr.5_1_2.rhel8            ## B
##    - pkg.python-pycryptodome.3_6_1.rhel8 ## no pycryptodomex-3.7.3-2,  not needed since M2Crypto
    - pkg.python-psutil.5_4_3.rhel8         ## B EPEL-7 python36-psutil 2.2.1-4.el7
    - pkg.python-pyroute2.0_4_13.rhel8      ## B
    - pkg.python-pyzmq.17_0_0.rhel8         ## B
    - pkg.python-simplejson.3_16_0.rhel8    ## B EPEL-7 python36-simplejson 3.10.0-2.el7
##    - pkg.python-timelib.0_2_4.rhel8      ## needed by test, byut that nox, pytest, pip
    - pkg.python-tornado4.4_5_2.rhel8       ## B EPEL-7 python36-tornado 4.4.2-2.el7
    - pkg.python-typing.3_5_2_2.rhel8       ## B EPEL-7 python34-typing 3.5.2.2-4.el7
##    - pkg.python-urllib3.1_10_4.rhel8     ## @anaconda    python3-urllib3.noarch  1.23-5.el8
##    - pkg.python-yaml.5_1.rhel8           ## @anaconda    python3-pyyaml.x86_64   3.12-12.el8
    - pkg.salt.3000_0_0.rhel8
    - pkg.zeromq.4_3_1.rhel8                ## B EPEL-7 zeromq-4.1.4-6.el7

{% elif buildcfg.build_release == 'rhel7' %}

    - pkg.libsodium.1_0_18.rhel7            ##   EPEL libsodium-1.0.18-1.el7
#    - pkg.libtomcrypt.1_17.rhel7           ##   extras   1.17-26.el7      not needed since M2Crypto
#    - pkg.libtommath.0_42_0.rhel7          ##   extras   0.42.0-6.el7     not needed since M2Crypto
    - pkg.openpgm.5_2_122.rhel7             ##   EPEL openpgm-5.2.122-2.el7
    - pkg.python36.3_6_8.rhel7
    - pkg.python-bottle.0_12_13.rhel7       ##   EPEL python36-bottle.0.12.13-3
    - pkg.python-chardet.3_0_4.rhel7        ##   EPEL python36-chardet 3.0-4-1.el7
    - pkg.python-cherrypy.5_6_0.rhel7
    - pkg.python-crypto.2_6_1.rhel7         ##   EPEL python36-crypto 2.6.1-16.el7  not needed since M2Crypto
###    - pkg.python-enum34.1_0.rhel7     ##   is this even needed ???   removing this with Py3.6
##    - pkg.python-futures.3_0_3.rhel7   ##   not even needed
    - pkg.python-gnupg.0_4_4.rhel7          ## B
    - pkg.python-idna.2_7.rhel7             ## EPEL python36-idna.2.7-5.el7
    - pkg.python-ioflo.1_3_8.rhel7          ## B
    - pkg.python-jinja2.2_8_1.rhel7         ## EPEL python36-jinja2.2.8.1-2.el7
    - pkg.python-libcloud.2_0_0.rhel7       ## B
    - pkg.python-libnacl.1_6_1.rhel7        ## B
    - pkg.python-m2crypto.0_33_0.rhel7      ## B
    - pkg.python-markupsafe.0_23.rhel7      ## EPEL python36-markupsafe-0.23-3.el7
    - pkg.python-msgpack.0_5_6.rhel7        ##   EPEL python36-msgpack 0.5.6-5.el7
    - pkg.python-mock.2_0_0.rhel7           ##   EPEL python36-mock-2.0.0-2.el7
    - pkg.python-pycryptodomex.3_7_3.rhel7  ##   EPEL python36-pycryptodomex-3.7.3-2
    - pkg.python-psutil.2_2_1.rhel7         ##   EPEL python36-psutil 2.2.1-5.el7
    - pkg.python-pbr.4_2_0.rhel7            ## EPEL python36-pbr.4.2.0-2.el7
    - pkg.python-pycurl.7_43_0.rhel7        ## EPEL python36-pycurl.7.43.0-7
    - pkg.python-pysocks.1_6_8.rhel7        ## EPEL python36-pysocks.1.6.8-6.el7
    - pkg.python-pyzmq.15_3_0.rhel7         ## B
    - pkg.python-raet.0_6_6.rhel7           ## B
    - pkg.python-requests.2_12_5.rhel7      ## EPEL python36-requests.2.12.5-3.el7
    - pkg.python-setuptools.39_2_0.rhel7    ## EPEL python36-setuptools.309.2.0-4.el7
    - pkg.python-simplejson.3_10_0.rhel7    ##   EPEL python36-simplejson 3.10.0-2.el7
    - pkg.python-six.1_11_0.rhel7           ## EPEL python36-six.1.11.0-3.el7
    - pkg.python-timelib.0_2_4.rhel7        ## B
    - pkg.python-tornado.4_4_2.rhel7        ##   EPEL python36-tornado 4.4.2-2.el7
    - pkg.python-typing.3_5_2_2.rhel7       ##   EPEL python36-typing 3.5.2.2-4.el7
    - pkg.python-urllib3.1_19_1.rhel7       ##   EPEL python36-urllib3 1.19.1-5.el7
    - pkg.python-yaml.3_11.rhel7            ##   EPEL python36-PyYaml-3.12-1.el7
    - pkg.salt.3000_0_0.rhel7
    - pkg.zeromq.4_1_4.rhel7                ##   EPEL zeromq-4.1.4-6.el7

{% elif buildcfg.build_release == 'fedora' %}

    - pkg.salt.3000_0_0.fedora

{% endif %}
