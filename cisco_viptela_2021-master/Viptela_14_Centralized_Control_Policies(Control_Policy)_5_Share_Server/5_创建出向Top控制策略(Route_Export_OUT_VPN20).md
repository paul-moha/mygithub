### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: Route_Export_OUT_VPN20
Description: Route_Export_OUT_VPN20

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
Site List: Gateway

Actions:
Accept

++++++++++++++++++++开始Route策略+++++++++++++++++++++++
=================Route=====================
Match Conditions
空

Actions:
Accept

------------------------------------------
Default Action
Reject  Enabled