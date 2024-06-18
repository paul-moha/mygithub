Configuration --- Templates --- Feature

模板类型:Feature
设备类型:vEdge_Cloud
Feature模板类型: OTHER TEMPLATE --- BGP
名称: Branch1_vEdge1_BGP_VPN0

---------Basic Configuration---------
AS Number:
```shell
bgp_as_num
```

---------UNICAST ADDRESS FAMILY---------
NETWORK: [宣告172.16.11.0/24]
+ New Network
```shell
bgp_network_network_address_prefix
```
注意: 一定要Add

---------NEIGHBOR---------
+ New Neighbor

Address
```shell
bgp254_neighbor_address
```

Remote AS
```shell
bgp254_neighbor_remote_as
```

Advanced Options --- EBGP Multihop: 255

注意: 一定要Add

=================================================

+ New Neighbor

Address
```shell
bgp12_neighbor_address
```

Remote AS
```shell
bgp12_neighbor_remote_as
```

Advanced Options --- EBGP Multihop: 255

注意: 一定要Add
