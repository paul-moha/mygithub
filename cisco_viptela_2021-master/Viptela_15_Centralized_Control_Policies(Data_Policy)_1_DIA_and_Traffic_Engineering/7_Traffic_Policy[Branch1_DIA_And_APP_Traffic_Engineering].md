### 创建Traffic Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Traffic Policy

Traffic Data [注意不是Application Aware Routing]
+ New Policy

Name: 
Branch1_DIA_And_APP_Traffic_Engineering

Description
Branch1_DIA_And_APP_Traffic_Engineering

=======================Custom==========================
Match Conditions
Application/Application Family List:       DIA_Application_List

Actions:
Accept
NAT VPN:    VPN ID:     0
Fallback    √
=================Traffic Engineering=====================
Match Conditions
Application/Application Family List:       youku

Actions:
Accept
Local TLOC List:        :public-internet
        Encapsulation   :IPSEC
        Restrict:       不√
=================Traffic Engineering=====================
Match Conditions
Application/Application Family List:       tudou

Actions:
Accept
Local TLOC List:        :mpls
        Encapsulation   :IPSEC
        Restrict:       不√

------------------------------------------
Default Action
Accept  Enabled

