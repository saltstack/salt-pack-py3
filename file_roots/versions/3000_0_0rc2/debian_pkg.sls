{% import "setup/debian/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'debian10' %}

##    - pkg.python-m2crypto.0_31_0.debian10
    - pkg.salt.3000_0_0.debian10

{% elif buildcfg.build_release == 'debian9' %}

    - pkg.python-ioflo.1_7_4.debian9        ## need update to latest, was 1.3.8
    - pkg.python-jinja2.2_9_4.debian9
##    - pkg.python-m2crypto.0_31_0.debian9
    - pkg.python-raet.0_6_8.debian9         ## need update to latest, was 0.6.3
    - pkg.python-timelib.0_2_4.debian9
    - pkg.salt.3000_0_0.debian9

{% endif %}
