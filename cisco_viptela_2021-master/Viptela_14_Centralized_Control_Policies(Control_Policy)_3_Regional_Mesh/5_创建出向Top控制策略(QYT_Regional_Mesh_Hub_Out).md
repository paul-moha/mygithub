### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: QYT_Regional_Mesh_Hub_Out
Description: QYT_Regional_Mesh_Hub_Out

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: Branch1

Actions:
Accept
=================TLOC=====================
Match Conditions
Site List: Gateway

Actions:
Accept
++++++++++++++++++++开始Route策略+++++++++++++++++++++++

=================Route=====================
Match Conditions
Site List: Branch1

Actions:
Accept
TLOC List: Branch1_vEdge
=================Route=====================
Match Conditions
Site List: Branch2

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

------------------------------------------
Default Action
Reject  Enabled