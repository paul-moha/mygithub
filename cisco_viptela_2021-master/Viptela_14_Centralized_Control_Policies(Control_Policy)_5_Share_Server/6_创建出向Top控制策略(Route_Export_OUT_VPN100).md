### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: Route_Export_OUT_VPN100
Description: Route_Export_OUT_VPN100

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: ALL_Site_List

Actions:
Accept

++++++++++++++++++++开始Route策略+++++++++++++++++++++++
=================Route=====================
Match Conditions
Originator:     10.10.10.11

Actions:
Accept
Preference:     200
=================Route=====================
Match Conditions
Originator:     10.10.10.12

Actions:
Accept
Preference:     100
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
Originator:     10.10.10.41

Actions:
Accept
Preference:     200
=================Route=====================
Match Conditions
Originator:     10.10.10.42

Actions:
Accept
Preference:     100

------------------------------------------
Default Action
Reject  Enabled