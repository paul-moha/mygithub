### 编辑Feature模板Hub_vEdge1_BGP_VPN10

Configuration --- Templates --- Feature --- Hub_vEdge1_BGP_VPN10 --- Edit

------- UNICAST ADDRESS FAMILY--------
RE-DISTRIBUTE
+ New Redistribue

Protocol: omp
Route Policy: 
```shell
bgp_redistribute_route_policy
```

注意: 一定要Add

------- NEIGHBOR ---------
Address                     Action
bgp40_neighbor_address      Edit

==========================
Address Family: On
Address Family: ipv4-unicast
Route Policy Out: On
Policy Name:
```shell
bgp40_neighbor_policer_out_pol_name
```

### 更新模板
Policy Name(bgp40_neighbor_policer_out_pol_name): Hub_vEdge1_40_to_4_Out
Route Policy(bgp_redistribute_route_policy): Hub_vEdge1_OMP_BGP40