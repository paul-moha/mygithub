### 创建路由策略
Configuration --- Policies --- Custom Options --- Localized Policy --- Route Policy

+ Add Route Policy

Name: Hub_vEdge2_OMP_BGP40

+++++++++与Hub_vEdge1_OMP_BGP40一模一样，只需要改名字++++++++++

======================================
Match Conditions
OMP Tag: 33

Actions:
Accept
Community: 33:33
======================================
Default Action
Accept  Enable
======================================