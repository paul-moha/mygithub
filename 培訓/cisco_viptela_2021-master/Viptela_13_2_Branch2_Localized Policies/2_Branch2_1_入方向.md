### 创建Community List

Configuration --- Policies --- Custom Options --- Localized Policy -- Lists --- Community

+ New Community List

Community List Name: Community88
Add Community: 88:88

注意: 一定要Add

### 创建路由策略
Configuration --- Policies --- Custom Options --- Localized Policy --- Route Policy

+ Add Route Policy

Name: Community88

======================================
Match Conditions
Community List:
Criteria: OR
Community List: Community88

Actions:
Reject  Enabled
======================================
Default Action
Accept  Enable
======================================