### 创建Site List
Configuration --- Policies --- Custom Options --- Centralized Policy --- Lists --- Site

+ New Site List

Site List Name: Branch1

Add Site: 10

+ New Site List

Site List Name: Branch2

Add Site: 20

+ New Site List

Site List Name: Branch3

Add Site: 30

+ New Site List

Site List Name: Hub_Site

Add Site: 40

+ New Site List

Site List Name: Gateway

Add Site: 50

+ New Site List

Site List Name: ALL_Site_List

Add Site: 10,20,30,40,50

+ New Site List

Site List Name: ALL_Branch

Add Site: 10,20,30,50

注意: 一定要Add

### 创建TLOC List
Configuration --- Policies --- Custom Options --- Centralized Policy --- Lists --- TLOC

+ New TLOC List

================================================================================
Branch1_vEdge

TLOC IP             Color                   Encap                   Preference
10.10.10.11         public-internet         ipsec                   200
10.10.10.11         mpls                    ipsec                   200
10.10.10.12         public-internet         ipsec                   100
10.10.10.12         mpls                    ipsec                   100

================================================================================
Hub_vEdge

TLOC IP             Color                   Encap                   Preference
10.10.10.41         public-internet         ipsec                   200
10.10.10.41         mpls                    ipsec                   200
10.10.10.42         public-internet         ipsec                   100
10.10.10.42         mpls                    ipsec                   100
