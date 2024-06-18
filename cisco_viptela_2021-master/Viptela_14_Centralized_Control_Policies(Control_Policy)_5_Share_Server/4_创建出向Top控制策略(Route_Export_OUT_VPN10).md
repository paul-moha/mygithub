### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: Route_Export_OUT_VPN10
Description: Route_Export_OUT_VPN10

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: Branch1

Actions:
Accept
=================TLOC=====================
Match Conditions
Site List: Hub_Site

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
Site List:      Branch1

Actions:
Accept
TLOC List:      Branch1_vEdge
=================Route=====================
Match Conditions
Site List:      Gateway

Actions:
Accept
OMP Tag:        33
=================Route=====================
Match Conditions
Site List:      Hub_Site

Actions:
Accept
TLOC List:      Hub_vEdge

------------------------------------------
Default Action
Reject  Enabled