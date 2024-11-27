### 创建Centralized Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Topology

+ Add Topology --- Custom Control(Route & TLOC)

Name: Route_Export_IN
Description: Route_Export_IN

++++++++++++++++++++开始Route策略+++++++++++++++++++++++
=================Route=====================
Match Conditions
VPN List: Client VPN

Actions:
Accept
Export To: Service_VPN_100
=================Route=====================
Match Conditions
VPN List: Service_VPN_100

Actions:
Export To: Client VPN

------------------------------------------
Default Action
Accept  Enabled