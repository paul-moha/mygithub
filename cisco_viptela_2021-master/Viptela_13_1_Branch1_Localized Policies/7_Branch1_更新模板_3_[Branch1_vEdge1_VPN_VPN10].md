### 编辑Feature模板Branch1_vEdge1_VPN_VPN10

Configuration --- Templates --- Feature --- Branch1_vEdge1_VPN_VPN10 --- Edit

------- Global Route Leak -------
+ Add New Route Leak from Global VPN to Service VPN [VPN0 到 VPN10]

Route Protocol to leak from Global to Service: bgp
Route Policy to leak from Global to Service: Branch1_Only_MPLS_Import_VPN10

注意: 一定要Add

=============================================================================
+ Add New Route Leak from Service VPN to Global VPN [VPN10 到 VPN0]

Route Protocol to leak from Service to Global: connected

注意: 一定要Add