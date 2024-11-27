### Hub_vEdge1设备模板关联策略

Configuration --- Templates --- Device --- Hub_vEdge1 --- Edit

-------Additional Templates-------
Policy: Hub_vEdge1_Policy

点击: Update (更新模板)

### 编辑Feature模板Hub_vEdge1_BGP_VPN0

Configuration --- Templates --- Feature --- Hub_vEdge1_BGP_VPN0 --- Edit

------- NEIGHBOR ---------
Address                     Action
bgp4_neighbor_address       Edit

==========================
Address Family: On
Address Family: ipv4-unicast
Route Policy Out: On
Policy Name:
```shell
bgp140_neighbor_policer_out_pol_name
```

### 更新模板
Policy Name(bgp140_neighbor_policer_out_pol_name): Hub_vEdge1_140_to_4_Out