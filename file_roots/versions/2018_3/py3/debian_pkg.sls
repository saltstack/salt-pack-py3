{% import "setup/debian/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'debian9' %}

##    - pkg.libsodium.1_0_3.debian9         ## Deb 9 provides 1.0.11-2
##    - pkg.python-future.0_14_3.debian9    ## Deb 9 provides 0.15.2-4
##    - pkg.python-futures.3_0_3.debian9    ## Deb 9 provides 3.0.5-3
##    - pkg.python-libcloud.1_5_0.debian9   ## Deb9 provides 1.5.0-1
##    - pkg.python-libnacl.4_1.debian9      ## Deb9 provides 1.5.0-1
##    - pkg.python-pyzmq.14_4_0.debian9     ## Deb9 provides 16.0.2-2
##    - pkg.python-systemd.231.debian9      ## Deb9 provides 233-1
##    - pkg.python-tornado.4_2_1.debian9    ## Deb9 provides 4.4.3-1
##    - pkg.zeromq.4_0_5.debian9            ## Deb9 provides libzmq5 4.2.1-4

    - pkg.python-ioflo.1_7_4.debian9        ## updated to latest, was 1.3.8
    - pkg.python-jinja2.2_9_4.debian9
    - pkg.python-raet.0_6_8.debian9         ## updated to latest, was 0.6.3
    - pkg.python-timelib.0_2_4.debian9
    - pkg.salt.2018_3.debian9

{% elif buildcfg.build_release == 'debian8' %}

{% if buildcfg.build_arch == 'armhf' %}

    - pkg.libsodium.1_0_3.debian8
    - pkg.python-future.0_14_3.debian8
    - pkg.python-futures.3_0_3.debian8
    - pkg.python-ioflo.1_7_4.debian8
    - pkg.python-libcloud.1_5_0.debian8
##    - pkg.python-libnacl.4_1.debian8      ## available 8   20110221-4.1
##    - pkg.python-pyzmq.14_4_0.debian8     ## available 8   14.4.0-1
    - pkg.python-raet.0_6_8.debian8
##    - pkg.python-systemd.231.debian8      ## available 8   233-1~bpo8+1
    - pkg.python-timelib.0_2_4.debian8
    - pkg.python-tornado.4_2_1.debian8
    - pkg.salt.2018_3.debian8
##    - pkg.zeromq.4_0_5.debian8            ## available 8   4.0.5+dfsg-2+deb8u1

{% else %}
##    - pkg.libsodium.1_0_3.debian8         ## available 8.10   1.0.11-1~bpo8+1
##    - pkg.python-cherrypy.2_3_0.debian8   ## available 8.10   3.5.0-1 cherrypy3
##    - pkg.python-croniter.0_3_4.debian8   ## available 8.10   0.3.12-1~bpo8+1
##    - pkg.python-crypto.2_6_1.debian8     ## available 8.10   2.6.1-5+deb8u1
    - pkg.python-enum34.1_0_4.debian8
##    - pkg.python-future.0_14_3.debian8    ## available 8.10   0.15.2-4~bpo8+1
##    - pkg.python-futures.3_0_3.debian8    ## available 8.10   3.0.5-2~bpo8+1
    - pkg.python-ioflo.1_7_4.debian8
    - pkg.python-jinja2.2_9_4.debian8
    - pkg.python-libcloud.1_5_0.debian8
##    - pkg.python-libnacl.4_1.debian8      ## available 8.10   20110221-4.1
##    - pkg.python-msgpack.0_4_2.debian8    ## available 8.10   0.4.6-1~bpo8+1
##    - pkg.python-pyzmq.14_4_0.debian8     ## available 8.10   14.4.0-1
    - pkg.python-raet.0_6_8.debian8
##    - pkg.python-requests.2_7_0.debian8   ## available 8.10   2.11.1-1~bpo8+1 
##    - pkg.python-systemd.231.debian8      ## available 8.10   233-1~bpo8+1
    - pkg.python-timelib.0_2_4.debian8
##    - pkg.python-tornado.4_2_1.debian8    ## available 8.10   4.4.3-1~bpo8+1 
##    - pkg.python-urllib3.1_10_4.debian8   ## available 8.10   1.16-1~bpo8+1
##    - pkg.python-yaml.3_11.debian8        ## available 8.10   3.11-2
    - pkg.salt.2018_3.debian8
##    - pkg.zeromq.4_0_5.debian8            ## available 8.10   4.0.5+dfsg-2+deb8u1

{% endif %}

{% endif %}
