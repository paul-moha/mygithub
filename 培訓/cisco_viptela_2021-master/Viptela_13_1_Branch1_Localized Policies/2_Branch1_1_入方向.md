### 创建Prefix-list

Configuration --- Policies --- Custom Options --- Localized Policy -- Lists --- Prefix

+ New Prefix List

Prefix List Name: Prefix_Only_MPLS
Add Prefix: 10.1.6.0/24

注意: 一定要Add

### 创建路由策略
Configuration --- Policies --- Custom Options --- Localized Policy --- Route Policy

+ Add Route Policy

Name: Branch1_Only_MPLS_Import_VPN10

================Route=================
Match Conditions
Address: Prefix_Only_MPLS

Actions
Accept
======================================
Default Action
Reject  Enable
======================================








