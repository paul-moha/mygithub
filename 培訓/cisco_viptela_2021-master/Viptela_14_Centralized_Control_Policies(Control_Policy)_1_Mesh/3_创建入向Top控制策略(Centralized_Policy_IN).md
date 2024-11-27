### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: Centralized_Policy_IN
Description: Centralized_Policy_IN

++++++++++++++++++++开始TLOC策略+++++++++++++++++++++++
=================TLOC=====================
Match Conditions
Site List: Branch1

Actions:
Accept
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
OMP Tag: 33
=================Route=====================
Match Conditions
Site List: Gateway

Actions:
Accept
OMP Tag: 33
=================Route=====================
Match Conditions
Site List: Hub_Site

Actions:
Accept

------------------------------------------
Default Action
Reject  Enabled