# Import build branch
{% import "setup/base_map.jinja" as versioncfg %}

'base':
  'G@os:CentOS':
    - {{versioncfg.redhat_pkg}}
  
  'G@osfullname:Debian or G@osfullname:Raspbian':
    - {{versioncfg.debian_pkg}}

  'G@osfullname:Ubuntu':
    - {{versioncfg.ubuntu_pkg}}


