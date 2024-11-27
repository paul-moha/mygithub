### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: QYT_Regional_Mesh_Branch1_Out
Description: QYT_Regional_Mesh_Branch1_Out

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: Branch2

Actions:
Accept
=================TLOC=====================
Match Conditions
Site List: Branch3

Actions:
Accept
=================TLOC=====================
Match Conditions
Site List: Hub_Site

Actions:
Accept
++++++++++++++++++++开始Route策略+++++++++++++++++++++++
=================Route=====================
Match Conditions
Site List: Hub_Site

Actions:
Accept
TLOC List: Hub_vEdge
=================Route=====================
Match Conditions
Site List: Branch2

Actions:
Accept
=================Route=====================
Match Conditions
Site List: Branch3

Actions:
Accept
=================Route=====================
Match Conditions
Site List: Gateway

Actions:
Accept
TLOC List: Hub_vEdge

------------------------------------------
Default Action
Reject  Enabled