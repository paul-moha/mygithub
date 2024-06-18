### Branch1_vEdge2设备模板关联策略

Configuration --- Templates --- Device --- Branch1_vEdge2 --- Edit

-------Additional Templates-------
Policy: Branch1_Policy

点击: Update (更新模板)

### 编辑Feature模板Branch1_vEdge2_BGP_VPN0

Configuration --- Templates --- Feature --- Branch1_vEdge2_BGP_VPN0 --- Edit

------- UNICAST ADDRESS FAMILY--------
RE-DISTRIBUTE
+ New Redistribue

Protocol: static   [重分布静态到BGP]

注意: 一定要Add

------- NEIGHBOR ---------
Address                     Action
bgp11_neighbor_address      Edit

==========================  [BGP11出向Prefix控制]
Address Family: On
Address Family: ipv4-unicast
Route Policy Out: On
Policy Name:
```shell
bgp11_neighbor_policer_out_pol_name
```

### 更新模板
Policy Name(bgp11_neighbor_policer_out_pol_name): Branch1_BGP_Out