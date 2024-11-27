Configuration --- Templates --- Feature

模板类型:Feature
设备类型:vEdge_Cloud
Feature模板类型: VPN --- VPN Interface Ethernet
名称: Branch1_vEdge_interface_VRRP

---------Basic Configuration---------
Shutdown: 
```shell
vpn_vrrp_if_shutdown
```

Interface Name: 
```shell
vpn_vrrp_if_name
```

IPv4 Address: 
```shell
vpn_vrrp_if_ipv4_address
```

-----------VRRP----------------
+ New VRRP

Group ID: 
```shell
vpn_if_vrrp_grpid
```

Priority: 
```shell
vpn_if_vrrp_priority
```

Track OMP: On

IP Address:
```shell
vpn_if_vrrp_vrrp_ipaddress
```

注意: 一定要Add