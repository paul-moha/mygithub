### 创建Centralized Policy
Configuration --- Policies --- Centralized Policy

+ Add Policy

略过: Create Groups of Interest

Configure Topology and VPN Membership --- Topology

+ Add Topology --- Import Existing Topology

Policy Type --- Custom Control(Route and TLOC) --- Centralized_Policy_IN
Policy Type --- Custom Control(Route and TLOC) --- Hub_OUT_Hub_Spoke
Policy Type --- Custom Control(Route and TLOC) --- ALL_Branch_OUT_Hub_Spoke

略过: Configure Traffic Rules

Apply Policies to Sites and VPNs

Policy Name: QYT_Centralized_Policy_Hub_Spoke
Policy Description: QYT_Centralized_Policy_Hub_Spoke

Topology

Centralized_Policy_IN
+ New Site List
Inbound Site List: ALL_Site_List

Hub_OUT_Hub_Spoke
+ New Site List
Outbound Site List: Hub_Site

ALL_Branch_OUT_Hub_Spoke
+ New Site List
Outbound Site List: ALL_Branch

最后: Save Policy Chanages

### 激活Centralized Policy

Configuration --- Policies --- Centralized Policy

选择 QYT_Centralized_Policy_Hub_Spoke ... Activate
