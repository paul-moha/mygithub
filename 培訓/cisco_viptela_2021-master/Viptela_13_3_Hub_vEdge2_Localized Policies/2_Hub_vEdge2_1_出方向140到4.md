### 创建路由策略
Configuration --- Policies --- Custom Options --- Localized Policy --- Route Policy

+ Add Route Policy

Name: Hub_vEdge2_140_to_4_Out

+++++++++复制Hub_vEdge1_140_to_4_Out，修改metric为100即可++++++++++

======================================
Match Conditions
Community List:
Criteria: OR
Community List: Community66

Actions:
Accept
Metric: 100
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
Metric: 100
======================================
Default Action
Reject  Enable
======================================