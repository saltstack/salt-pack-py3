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

    - pkg.python-ioflo.1_7_4.debian9        ## need update to latest, was 1.3.8
    - pkg.python-jinja2.2_9_4.debian9
    - pkg.python-raet.0_6_8.debian9         ## need update to latest, was 0.6.3
    - pkg.python-timelib.0_2_4.debian9
    - pkg.salt.2018_3_4.debian9

{% endif %}
