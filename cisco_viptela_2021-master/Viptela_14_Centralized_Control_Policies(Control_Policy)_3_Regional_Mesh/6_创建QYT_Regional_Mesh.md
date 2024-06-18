### 创建Centralized Policy
Configuration --- Policies --- Centralized Policy

+ Add Policy

略过: Create Groups of Interest

Configure Topology and VPN Membership --- Topology

+ Add Topology --- Import Existing Topology

Policy Type --- Custom Control(Route and TLOC) --- Centralized_Policy_IN
Policy Type --- Custom Control(Route and TLOC) --- QYT_Regional_Mesh_Branch1_Out
Policy Type --- Custom Control(Route and TLOC) --- QYT_Regional_Mesh_Branch2_Out
Policy Type --- Custom Control(Route and TLOC) --- QYT_Regional_Mesh_Branch3_Out
Policy Type --- Custom Control(Route and TLOC) --- QYT_Regional_Mesh_Gateway_Out
Policy Type --- Custom Control(Route and TLOC) --- QYT_Regional_Mesh_Hub_Out

略过: Configure Traffic Rules

Apply Policies to Sites and VPNs

Policy Name: QYT_Regional_Mesh
Policy Description: QYT_Regional_Mesh

Topology

Centralized_Policy_IN
+ New Site List
Inbound Site List: ALL_Site_List

QYT_Regional_Mesh_Branch1_Out
+ New Site List
Outbound Site List: Branch1

QYT_Regional_Mesh_Branch2_Out
+ New Site List
Outbound Site List: Branch2

QYT_Regional_Mesh_Branch3_Out
+ New Site List
Outbound Site List: Branch3

QYT_Regional_Mesh_Gateway_Out
+ New Site List
Outbound Site List: Gateway

QYT_Regional_Mesh_Hub_Out
+ New Site List
Outbound Site List: Hub

最后: Save Policy Chanages

### 激活Centralized Policy

Configuration --- Policies --- Centralized Policy

选择 QYT_Regional_Mesh ... Activate
