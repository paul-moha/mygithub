### 创建Centralized Policy
Configuration --- Policies --- Centralized Policy

+ Add Policy

略过: Create Groups of Interest

Configure Topology and VPN Membership --- Topology

+ Add Topology --- Import Existing Topology

Policy Type --- Custom Control(Route and TLOC) --- Route_Export_IN
Policy Type --- Custom Control(Route and TLOC) --- Route_Export_OUT_VPN10
Policy Type --- Custom Control(Route and TLOC) --- Route_Export_OUT_VPN20
Policy Type --- Custom Control(Route and TLOC) --- Route_Export_OUT_VPN100

略过: Configure Traffic Rules

Apply Policies to Sites and VPNs

Policy Name: QYT_Route_Export
Policy Description: QYT_Route_Export

Topology

Route_Export_IN
+ New Site List
Inbound Site List: ALL_Site_List

Route_Export_OUT_VPN10
+ New Site List
Outbound Site List: Hub_Site,Branch1

Route_Export_OUT_VPN20
+ New Site List
Outbound Site List: Branch2,Branch3

Route_Export_OUT_VPN100
+ New Site List
Outbound Site List: Gateway

最后: Save Policy Chanages

### 激活Centralized Policy

Configuration --- Policies --- Centralized Policy

选择 QYT_Route_Export ... Activate
