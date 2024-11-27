### 创建Traffic Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Traffic Policy

Traffic Data [注意不是Application Aware Routing]
+ New Policy

Name: 
Hub_DIA_Policy

Description
Hub_DIA_Policy

=================Custom=====================
Match Conditions
Destination Data Prefix List:       ALL_Site_Data_Prefix_List

Actions:
Accept

=================Custom=====================
Match Conditions
Source Data Prefix List:            Hub_DIA_Prefix

Actions:
Accept
NAT VPN:    VPN ID:     0
Fallback:   不√
------------------------------------------
Default Action
Accept  Enabled

