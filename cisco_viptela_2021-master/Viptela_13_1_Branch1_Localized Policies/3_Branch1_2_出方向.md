### 创建Prefix-list

Configuration --- Policies --- Custom Options --- Localized Policy -- Lists --- Prefix

+ New Prefix List

Prefix List Name: Prefix_Branch1_BGP_Out
Add Prefix: 172.16.11.0/24,10.1.1.0/24

注意: 一定要Add

### 创建路由策略
Configuration --- Policies --- Custom Options --- Localized Policy --- Route Policy

+ Add Route Policy

Name: Branch1_BGP_Out

================Route=================
Match Conditions
Address: Prefix_Branch1_BGP_Out

Actions
Accept
======================================
Default Action
Reject  Enable
======================================
