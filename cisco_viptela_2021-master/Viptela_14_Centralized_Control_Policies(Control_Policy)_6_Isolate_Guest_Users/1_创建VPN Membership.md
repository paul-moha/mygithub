### 创建Site List
Configuration --- Policies --- Custom Options --- Centralized Policy --- Lists --- VPN

+ New VPN List

VPN List Name: Enterpise_VPN_10

Add VPN: 10

### 修改Centralized Policy
Configuration --- Policies --- Centralized Policy

QYT_Route_Export ... Edit

Topology --- VPN Membership

+ Add VPN Membership Policy

VPN Membership Name:    Isolate_Guest_Users
Description:            Isolate_Guest_Users
--------------------------------------------
Site List               VPN Lists
ALL_Site_List           Enterpise_VPN_10,Service_VPN_100


注意: Save Policy Chanages
