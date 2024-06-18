### 创建Community List

Configuration --- Policies --- Custom Options --- Localized Policy -- Lists --- Community

+ New Community List

Community List Name: Community66
Add Community: 66:66

注意: 一定要Add

### 创建Prefix List

Configuration --- Policies --- Custom Options --- Localized Policy -- Lists --- Prefix

+ New Prefix List

Prefix List Name: Default_Route
Add Prefix: 0.0.0.0/0

注意: 一定要Add

### 创建路由策略
Configuration --- Policies --- Custom Options --- Localized Policy --- Route Policy

+ Add Route Policy

Name: Hub_vEdge1_140_to_4_Out

======================================
Match Conditions
Community List:
Criteria: OR
Community List: Community66

Actions:
Accept
Metric: 50
======================================
Match Conditions
Address: Default_Route

Actions:
Reject  Enabled
======================================
Match Conditions
空

Actions:
Accept
Community: no-export
Metric: 50
======================================
Default Action
Reject  Enable
======================================