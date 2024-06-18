### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: ALL_Branch_OUT_Hub_Spoke
Description: ALL_Branch_OUT_Hub_Spoke

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: Hub_Site

Actions:
Accept
++++++++++++++++++++开始Route策略+++++++++++++++++++++++
=================Route=====================
Match Conditions
Site List: Branch1

Actions:
Accept
TLOC List: Hub_vEdge
=================Route=====================
Match Conditions
Site List: Branch2

Actions:
Accept
TLOC List: Hub_vEdge
=================Route=====================
Match Conditions
Site List: Branch3

Actions:
Accept
TLOC List: Hub_vEdge
=================Route=====================
Match Conditions
Site List: Gateway

Actions:
Accept
TLOC List: Hub_vEdge
=================Route=====================
Match Conditions
Site List: Hub_Site

Actions:
Accept
TLOC List: Hub_vEdge

------------------------------------------
Default Action
Reject  Enabled