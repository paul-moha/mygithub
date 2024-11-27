### 创建Data Prefix List
Configuration --- Localized Policy --- Lists --- Data Prefix
+ New Data Prefix List

Data Prefix List Name: Hub_Data_Prefix
Internet Protocol: IPv4
Add Data Prefix: 10.1.4.0/24

注意: 一定要Add

Configuration --- Localized Policy --- Lists --- Data Prefix
+ New Data Prefix List

Data Prefix List Name: Branch2_Data_Prefix
Internet Protocol: IPv4
Add Data Prefix: 10.1.2.0/24

注意: 一定要Add

### 创建Access Control List
Configuration --- Localized Policy --- Access Control Lists
+ Add Access Control List Policy --- Add IPv4 ACL Policy

Name: Branch2_ACL
Description: Branch2_ACL

=================Access Control List=====================
Match Conditions
----------
Source Data Prefix List: Hub_Data_Prefix
Source IP
----------
Destination Data Prefix List: Branch2_Data_Prefix
Destination IP
----------
Destination Port: 80

++++++++++

Actions
Drop        Enabled
Log         Enabled
Counter     Branch2_ACL_Drop
=========================================================
Default Action
Accept  Enable
=========================================================

注意: 先 Save Match And Actions 然后 Save Access Control List Policy

### Localized Policy添加ACL
Configuration --- Policies --- Localized Policy

Branch2_Policy --- Edit

Access Control Lists 部分:
+ Add Access Control List Policy --- Import Existing
Policy: Branch2_ACL

### 修改模板Branch2_cEdge_Interface_G3
Configuration --- TEMPLATES --- Feature --- Branch2_cEdge_Interface_G3 --- Edit

------- ACL/QoS ---------
Egress ACL - IPv4: On
IPv4 Egress Access List: ipv4_access_list_egress_acl_name_ipv4

### 更新模板
Access list(ipv4_access_list_egress_acl_name_ipv4): Branch2_ACL