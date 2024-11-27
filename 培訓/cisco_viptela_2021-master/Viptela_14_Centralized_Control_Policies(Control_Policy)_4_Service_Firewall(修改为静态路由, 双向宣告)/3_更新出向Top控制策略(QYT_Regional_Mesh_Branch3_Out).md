### 更新Topology策略QYT_Regional_Mesh_Branch3_Out
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

QYT_Regional_Mesh_Branch3_Out ... Edit

=================Route=====================
Match Conditions
Site List: Branch2

Actions:
Accept

+++++++删除之前的TLOC策略，添加Service策略++++++

Service: Type       Firewall
Service: VPN        10
Service: TLOC IP    10.10.10.11
Color               public-internet
Encapsulation       IPSEC