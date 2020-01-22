## Amazon Python 3 support is only for Python 3 itself, this implies
## that all dependencies will need to be produced for Python 3.
## Removed support for ioflo, raet, libnacl since deprecated

{% import "setup/amazon/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'amzn2' %}

    - pkg.distribution-gpg-keys.1_30.amzn2
    - pkg.libsodium.1_0_16.amzn2
    - pkg.libtomcrypt.1_17.amzn2
    - pkg.libtommath.0_42_0.amzn2
    - pkg.openpgm.5_2_122.amzn2
    - pkg.mock.1_4_15.amzn2
    - pkg.mock-core-configs.30_3.amzn2
    - pkg.python-attrs.17_4_0.amzn2
    - pkg.python-atomicwrites.1_1_5.amzn2
    - pkg.python-babel.2_6_0.amzn2
    - pkg.python-backports_abc.0_5.amzn2
    - pkg.python-bottle.0_12_13.amzn2
    - pkg.python-chardet.3_0_4.amzn2
    - pkg.python-cherrypy.5_6_0.amzn2
    - pkg.python-coverage.4_5_1.amzn2
    - pkg.python-crypto.2_6_1.amzn2
    - pkg.python-dateutil.2_7_3.amzn2
    - pkg.python-distro.1_2_0.amzn2
    - pkg.python-freezegun.0_3_8.amzn2
    - pkg.python-funcsigs.1_0_2.amzn2
    - pkg.python-gnupg.0_4_4.amzn2
    - pkg.python-hypothesis.3_66_11.amzn2
    - pkg.python-idna.2_7.amzn2
    - pkg.python-jinja2.2_10.amzn2
    - pkg.python-libcloud.2_2_1.amzn2
    - pkg.python-m2crypto.0_31_0.amzn2
    - pkg.python-markupsafe.1_0.amzn2
    - pkg.python-mock.2_0_0.amzn2           ## should not be needed since Py3.3 as part of Standard Library, list as dependencies in some packages
    - pkg.python-msgpack.0_5_6.amzn2
    - pkg.python-more-itertools.4_1_0.amzn2
    - pkg.python-nose.1_3_7.amzn2
    - pkg.python-pbr.5_1_2.amzn2
    - pkg.python-pluggy.0_7_1.amzn2
    - pkg.python-psutil.5_4_3.amzn2
    - pkg.python-py.1_5_4.amzn2
    - pkg.python-pycryptodome.3_6_1.amzn2
    - pkg.python-pycurl.7_43_0_2.amzn2
    - pkg.python-pyflakes.2_0_0.amzn2
    - pkg.python-pyroute2.0_5_3.amzn2
    - pkg.python-pysocks.1_6_8.amzn2
    - pkg.python-pytest.3_6_4.amzn2
    - pkg.python-pytest-runner.4_0.amzn2
    - pkg.python-pytz.2018_5.amzn2
    - pkg.python-pyzmq.17_0_0.amzn2
    - pkg.python-requests.2_19_1.amzn2
    - pkg.python-rpm.4_11_3.amzn2
    - pkg.python-setuptools_scm.3_1_0.amzn2
    - pkg.python-simplejson.3_16_0.amzn2
    - pkg.python-singledispatch.3_4_0_3.amzn2
    - pkg.python-six.1_11_0.amzn2
    - pkg.python-sure.1_4_11.amzn2
##    - pkg.python-tornado.4_5_2.amzn2    ## build and use this till salt updated
    - pkg.python-tornado4.4_5_2.amzn2    ## build and use this till salt updated
##    - pkg.python-tornado.5_0_2.amzn2     ## latest 5.1.1
    - pkg.python-timelib.0_2_4.amzn2
    - pkg.python-typing.3_5_2_2.amzn2
    - pkg.python-unittest2.1_1_0.amzn2
    - pkg.python-urllib3.1_23.amzn2
    - pkg.python-yaml.4_2.amzn2
    - pkg.python-zope-event.4_2_0.amzn2
    - pkg.python-zope-interface.4_5_0.amzn2
    - pkg.salt.3000_0_0.amzn2
    - pkg.zeromq.4_2_3.amzn2             ## latest 4.2.3

{% endif %}

