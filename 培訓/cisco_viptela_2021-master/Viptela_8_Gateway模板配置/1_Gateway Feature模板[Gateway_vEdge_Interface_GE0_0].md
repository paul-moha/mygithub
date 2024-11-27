Configuration --- Templates --- Feature

模板类型:Feature
设备类型:vEdge_Cloud
Feature模板类型: VPN ---VPN Interface Ethernet
名称: Gateway_vEdge_Interface_GE0/0

### Gateway_vEdge_Interface_GE0/0 [VPN Interface Ethernet ]
---------Basic Configuration---------
Shutdown: 
```shell
vpn0_ge0/0_if_shutdown
```

Interface Name: 
```shell
vpn0_ge0/0_if_name
```

IPv4 Address: 
```shell
vpn0_ge0/0_if_ipv4_address
```

---------Tunnel---------
Tunnel Interface: On

Color: 
```shell
vpn0_ge0/0_if_tunnel_color_value
```

Restrict: 
```shell
vpn0_ge0/0_if_tunnel_color_restrict
```

vManage Connection Preference: 
```shell
vpn0_ge0/0_if_tunnel_vmanage_connection_preference
```

Allow Service --- All: 
```shell
vpn0_ge0/0_if_tunnel_all
```

---------NAT---------

NAT: On

Refresh Mode:
```shell
vpn0_ge0/0_nat_refresh
```