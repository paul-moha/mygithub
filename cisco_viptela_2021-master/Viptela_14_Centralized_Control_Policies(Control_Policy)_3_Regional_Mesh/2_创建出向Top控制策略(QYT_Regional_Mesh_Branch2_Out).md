### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: QYT_Regional_Mesh_Branch2_Out
Description: QYT_Regional_Mesh_Branch2_Out

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: Branch1

Actions:
Accept
++++++++++++++++++++开始Route策略+++++++++++++++++++++++
=================Route=====================
Match Conditions
Site List: Hub_Site

Actions:
Accept
TLOC List: Branch1_vEdge
=================Route=====================
Match Conditions
Site List: Branch1

Actions:
Accept
TLOC List: Branch1_vEdge
=================Route=====================
Match Conditions
Site List: Branch3

Actions:
Accept
TLOC List: Branch1_vEdge
=================Route=====================
Match Conditions
Site List: Gateway

Actions:
Accept
TLOC List: Branch1_vEdge

------------------------------------------
Default Action
Reject  Enabled