Configuration --- Templates --- Feature

模板类型:Feature
设备类型:CSR1000v
Feature模板类型: OTHER TEMPLATES --- Cisco BGP
名称: Branch2_cEdge_BGP_VPN10

---------Basic Configuration---------

AS Number: 
```shell
bgp2_as_num
```

Propagate AS Path: On

---------UNICAST ADDRESS FAMILY---------
NETWORK: [发默认路由到BGP]
+ New Network
```shell
bgp2_network_network_address_prefix
```
注意: 一定要Add

---------NEIGHBOR---------
+ New Neighbor

Address
```shell
bgp2_neighbor_address
```

Remote AS
```shell
bgp2_neighbor_remote_as
```

Advanced Options --- EBGP Multihop: 255

注意: 一定要Add
