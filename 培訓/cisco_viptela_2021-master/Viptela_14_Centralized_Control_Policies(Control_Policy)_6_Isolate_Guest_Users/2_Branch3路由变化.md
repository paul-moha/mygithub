### 配置VPN Membership之前
Branch3_vEdge# show omp route | tab 

                                            PATH                      ATTRIBUTE                                                       
VPN    PREFIX              FROM PEER        ID     LABEL    STATUS    TYPE       TLOC IP          COLOR            ENCAP  PREFERENCE  
--------------------------------------------------------------------------------------------------------------------------------------
20     10.1.2.0/24         2.2.2.1          297    1004     Inv,U     installed  10.10.10.20      mpls             ipsec  -           
                           2.2.2.1          299    1004     C,I,R     installed  10.10.10.20      public-internet  ipsec  -           
20     10.1.3.0/24         0.0.0.0          69     1004     C,Red,R   installed  10.10.10.30      public-internet  ipsec  -           
20     10.1.5.0/24         2.2.2.1          300    1004     C,I,R     installed  10.10.10.50      public-internet  ipsec  -   

### 配置VPN Membership之后[VPN20已经被隔离]
Branch3_vEdge# show omp route | tab
                                            PATH                      ATTRIBUTE                                                       
VPN    PREFIX              FROM PEER        ID     LABEL    STATUS    TYPE       TLOC IP          COLOR            ENCAP  PREFERENCE  
--------------------------------------------------------------------------------------------------------------------------------------
20     10.1.3.0/24         0.0.0.0          69     1004     C,Red,R   installed  10.10.10.30      public-internet  ipsec  -  

### vSmart已经把VPN20的OMP路由设置为非法

vSmart1# show omp route | tab

                                            PATH                      ATTRIBUTE                                                       
VPN    PREFIX              FROM PEER        ID     LABEL    STATUS    TYPE       TLOC IP          COLOR            ENCAP  PREFERENCE  
--------------------------------------------------------------------------------------------------------------------------------------
10     10.1.1.0/24         10.10.10.11      66     1003     C,R       installed  10.10.10.11      mpls             ipsec  -           
                           10.10.10.11      69     1003     C,R       installed  10.10.10.11      public-internet  ipsec  -           
                           10.10.10.12      66     1003     C,R       installed  10.10.10.12      mpls             ipsec  -           
                           10.10.10.12      69     1003     C,R       installed  10.10.10.12      public-internet  ipsec  -           
10     10.1.4.0/24         10.10.10.41      66     1003     C,R       installed  10.10.10.41      mpls             ipsec  -           
                           10.10.10.41      69     1003     C,R       installed  10.10.10.41      public-internet  ipsec  -           
                           10.10.10.42      66     1003     R         installed  10.10.10.42      mpls             ipsec  -           
                           10.10.10.42      69     1003     R         installed  10.10.10.42      public-internet  ipsec  -           
10     10.1.5.0/24         10.10.10.50      92     1004     C,R,Ext   original   10.10.10.50      public-internet  ipsec  -           
                                                                      installed  10.10.10.50      public-internet  ipsec  -           
10     10.1.6.0/24         10.10.10.41      66     1003     C,R       installed  10.10.10.41      mpls             ipsec  -           
                           10.10.10.41      69     1003     C,R       installed  10.10.10.41      public-internet  ipsec  -           
                           10.10.10.42      66     1003     R         installed  10.10.10.42      mpls             ipsec  -           
                           10.10.10.42      69     1003     R         installed  10.10.10.42      public-internet  ipsec  -           
10     192.168.0.0/24      10.10.10.11      66     1003     C,R       installed  10.10.10.11      mpls             ipsec  -           
                           10.10.10.11      69     1003     C,R       installed  10.10.10.11      public-internet  ipsec  -           
10     192.168.1.0/24      10.10.10.11      66     1003     C,R       installed  10.10.10.11      mpls             ipsec  -           
                           10.10.10.11      69     1003     C,R       installed  10.10.10.11      public-internet  ipsec  -           
20     10.1.2.0/24         10.10.10.20      66     1004     Rej,R,Inv installed  10.10.10.20      mpls             ipsec  -           
                           10.10.10.20      69     1004     Rej,R,Inv installed  10.10.10.20      public-internet  ipsec  -           
20     10.1.3.0/24         10.10.10.30      69     1004     Rej,R,Inv installed  10.10.10.30      public-internet  ipsec  -           
20     10.1.5.0/24         10.10.10.50      92     1004     C,R,Ext   original   10.10.10.50      public-internet  ipsec  -           
                                                                      installed  10.10.10.50      public-internet  ipsec  -           
100    10.1.1.0/24         10.10.10.11      89     1003     C,R,Ext   original   10.10.10.11      mpls             ipsec  -           
                                                                      installed  10.10.10.11      mpls             ipsec  -           
                           10.10.10.11      92     1003     C,R,Ext   original   10.10.10.11      public-internet  ipsec  -           
                                                                      installed  10.10.10.11      public-internet  ipsec  -           
                           10.10.10.12      89     1003     C,R,Ext   original   10.10.10.12      mpls             ipsec  -           
                                                                      installed  10.10.10.12      mpls             ipsec  -           
                           10.10.10.12      92     1003     C,R,Ext   original   10.10.10.12      public-internet  ipsec  -           
                                                                      installed  10.10.10.12      public-internet  ipsec  -           
100    10.1.4.0/24         10.10.10.41      89     1003     C,R,Ext   original   10.10.10.41      mpls             ipsec  -           
                                                                      installed  10.10.10.41      mpls             ipsec  -           
                           10.10.10.41      92     1003     C,R,Ext   original   10.10.10.41      public-internet  ipsec  -           
                                                                      installed  10.10.10.41      public-internet  ipsec  -           
100    10.1.5.0/24         10.10.10.50      69     1004     C,R       installed  10.10.10.50      public-internet  ipsec  -           
100    10.1.6.0/24         10.10.10.41      89     1003     C,R,Ext   original   10.10.10.41      mpls             ipsec  -           
                                                                      installed  10.10.10.41      mpls             ipsec  -           
                           10.10.10.41      92     1003     C,R,Ext   original   10.10.10.41      public-internet  ipsec  -           
                                                                      installed  10.10.10.41      public-internet  ipsec  -           
100    192.168.0.0/24      10.10.10.11      89     1003     C,R,Ext   original   10.10.10.11      mpls             ipsec  -           
                                                                      installed  10.10.10.11      mpls             ipsec  -           
                           10.10.10.11      92     1003     C,R,Ext   original   10.10.10.11      public-internet  ipsec  -           
                                                                      installed  10.10.10.11      public-internet  ipsec  -           
100    192.168.1.0/24      10.10.10.11      89     1003     C,R,Ext   original   10.10.10.11      mpls             ipsec  -           
                                                                      installed  10.10.10.11      mpls             ipsec  -           
                           10.10.10.11      92     1003     C,R,Ext   original   10.10.10.11      public-internet  ipsec  -           
                                                                      installed  10.10.10.11      public-internet  ipsec  - 