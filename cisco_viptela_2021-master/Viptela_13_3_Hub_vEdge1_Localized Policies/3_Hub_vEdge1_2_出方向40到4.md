### 创建Community List

Configuration --- Policies --- Custom Options --- Localized Policy -- Lists --- Community

+ New Community List

Community List Name: Community33
Add Community: 33:33

注意: 一定要Add

### 创建路由策略
Configuration --- Policies --- Custom Options --- Localized Policy --- Route Policy

+ Add Route Policy

Name: Hub_vEdge1_40_to_4_Out

======================================
Match Conditions
Community List:
Criteria: OR
Community List: Community33

Actions:
Accept
Metric: 50
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