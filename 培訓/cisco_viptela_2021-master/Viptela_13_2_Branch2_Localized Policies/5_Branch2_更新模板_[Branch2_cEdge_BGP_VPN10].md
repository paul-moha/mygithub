### Branch2_cEdge设备模板关联策略

Configuration --- Templates --- Device --- Branch2_cEdge --- Edit

-------Additional Templates-------
Policy: Branch2_Policy

点击: Update (更新模板)

### 编辑Feature模板Branch2_cEdge_BGP_VPN10

Configuration --- Templates --- Feature --- Branch2_cEdge_BGP_VPN10 --- Edit

------- UNICAST ADDRESS FAMILY--------
RE-DISTRIBUTE
+ New Redistribue

Protocol: omp    [重分布OMP(SDWAN的路由)进入BGP]

注意: 一定要Add

------- NEIGHBOR ---------
Address                     Action
bgp2_neighbor_address       Edit

==========================
Address Family: On
Address Family: ipv4-unicast
Route Policy In: On  [入向控制只允许本地Prefix]
Policy Name:
```shell
bgp_neighbor_policer_in_pol_name
```
Route Policy Out: On  [出向Prefix打上no-export Community]
Policy Name:
```shell
bgp_neighbor_policer_out_pol_name
```

### 更新模板
Policy Name(bgp_neighbor_policer_in_pol_name): Community88
Policy Name(bgp_neighbor_policer_out_pol_name): No_Export