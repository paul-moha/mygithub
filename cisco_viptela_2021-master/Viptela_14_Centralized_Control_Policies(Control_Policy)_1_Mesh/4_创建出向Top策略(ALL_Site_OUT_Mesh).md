### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: ALL_Site_OUT_Mesh
Description: ALL_Site_OUT_Mesh

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: ALL_Site_List

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
=================Route=====================
Match Conditions
Site List: Hub_Site

Actions:
Accept
TLOC List: Hub_vEdge

------------------------------------------
Default Action
Reject  Enabled