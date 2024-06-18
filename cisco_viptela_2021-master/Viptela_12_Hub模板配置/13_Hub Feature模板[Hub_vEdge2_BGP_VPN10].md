Configuration --- Templates --- Feature

模板类型:Feature
设备类型:vEdge_Cloud
Feature模板类型: OTHER TEMPLATE --- BGP
名称: Hub_vEdge2_BGP_VPN10

+++++++++注意和Hub_vEdge1_BGP_VPN10一模一样，复制+改名即可++++++++++
---------Basic Configuration---------
AS Number:
```shell
bgp40_as_num
```

Propagate AS Path: On

---------UNICAST ADDRESS FAMILY---------
IPv4 --- NETWORK:
+ New Network
```shell
bgp40_network_network_address_prefix
```
注意: 一定要Add

---------NEIGHBOR---------
+ New Neighbor

Address
```shell
bgp40_neighbor_address
```

Remote AS
```shell
bgp40_neighbor_remote_as
```

Advanced Options --- EBGP Multihop: 255

注意: 一定要Add
