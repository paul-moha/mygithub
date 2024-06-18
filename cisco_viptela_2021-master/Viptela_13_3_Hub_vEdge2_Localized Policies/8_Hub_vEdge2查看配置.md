Hub_vEdge2# sh run vpn 0
```shell
vpn 0
 dns 202.100.100.200 primary
 router
  bgp 140
   address-family ipv4-unicast
    network 0.0.0.0/0
    network 10.1.242.0/24
   !
   neighbor 172.16.42.1
    no shutdown
    remote-as     4
    ebgp-multihop 255
    address-family ipv4-unicast
     route-policy Hub_vEdge2_140_to_4_Out out
    !
   !
   neighbor 172.16.142.254
    no shutdown
    remote-as     254
    ebgp-multihop 255
   !
  !
 !
 interface ge0/0
  ip address 202.100.42.1/24
  nat
  !
  no shutdown
 !
 interface ge0/1
  ip address 172.16.142.1/24
  no shutdown
 !
 interface ge0/2
  ip address 172.16.42.254/24
  no shutdown
 !
 interface loopback1
  ip address 10.1.142.1/24
  tunnel-interface
   encapsulation ipsec
   color public-internet restrict
   vmanage-connection-preference 8
   bind                          ge0/0
   allow-service all
   no allow-service bgp
   allow-service dhcp
   allow-service dns
   allow-service icmp
   no allow-service sshd
   no allow-service netconf
   no allow-service ntp
   no allow-service ospf
   no allow-service stun
   allow-service https
  !
  no shutdown
 !
 interface loopback2
  ip address 10.1.242.1/24
  tunnel-interface
   encapsulation ipsec
   color mpls restrict
   max-control-connections 0
   bind                    ge0/1
   allow-service all
   no allow-service bgp
   allow-service dhcp
   allow-service dns
   allow-service icmp
   no allow-service sshd
   no allow-service netconf
   no allow-service ntp
   no allow-service ospf
   no allow-service stun
   allow-service https
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.42.254
!
```
Hub_vEdge2# sh run vpn 10
```shell
vpn 10
 router
  bgp 40
   propagate-aspath
   address-family ipv4-unicast
    network 0.0.0.0/0
    redistribute omp
   !
   neighbor 10.1.42.1
    no shutdown
    remote-as     4
    ebgp-multihop 255
    address-family ipv4-unicast
     route-policy Hub_vEdge2_40_to_4_Out out
    !
   !
  !
 !
 interface ge0/3
  ip address 10.1.42.254/24
  no shutdown
 !
 ip route 0.0.0.0/0 vpn 0
!
```

Hub_vEdge2# show bgp summary 
```shell
vpn                    0
bgp-router-identifier  10.10.10.42
local-as               140
rib-entries            23
rib-memory             2576
total-peers            2
peer-memory            9632
Local-soo              SoO:0:40
ignore-soo             
                       MSG       MSG       OUT                     PREFIX  PREFIX  PREFIX                
NEIGHBOR         AS    RCVD      SENT      Q      UPTIME           RCVD    VALID   INSTALLED  STATE      
---------------------------------------------------------------------------------------------------------
172.16.42.1      4     1510      1368      0      0:22:31:29       1       1       1          established
172.16.142.254   254   1361      1356      0      0:22:31:28       10      10      10         established


vpn                    10
bgp-router-identifier  10.10.10.42
local-as               40
rib-entries            12
rib-memory             1344
total-peers            1
peer-memory            4816
Local-soo              SoO:0:40
ignore-soo             
                       MSG       MSG       OUT                     PREFIX  PREFIX  PREFIX                
NEIGHBOR         AS    RCVD      SENT      Q      UPTIME           RCVD    VALID   INSTALLED  STATE      
---------------------------------------------------------------------------------------------------------
10.1.42.1        4     1517      1358      0      0:22:31:29       2       2       2          established
```