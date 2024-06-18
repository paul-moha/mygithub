### 编辑Feature模板Hub_vEdge_VPN_VPN10

Configuration --- Templates --- Feature --- Hub_vEdge_VPN_VPN10 --- Edit

--------------IPv4 ROUTE------------

+ New IPv4 Router

Prefix: 
```shell
vpn10_ipv4_ip_prefix
```

Gateway: Null0      -------修改
Enable Null0: On    -------修改

注意: 一定要Add

------------Advertise OMP------------

Static (IPv4):  On


### 需要更新两个vEdge
Prefix(vpn10_ipv4_ip_prefix): 0.0.0.0/0