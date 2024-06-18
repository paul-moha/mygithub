Branch1_vEdge1# sh run vpn 0
```shell
vpn 0
 dns 202.100.100.200 primary
 router
  bgp 11
   address-family ipv4-unicast
    network 172.16.11.0/24
   !
   neighbor 172.16.10.254
    no shutdown
    remote-as     254
    ebgp-multihop 255
   !
   neighbor 172.16.11.1
    no shutdown
    remote-as     12
    ebgp-multihop 255
   !
  !
 !
 interface ge0/0
  ip address 172.16.10.1/24
  tunnel-interface
   encapsulation ipsec
   color mpls restrict
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
 interface ge0/2
  ip address 172.16.11.254/24
  tloc-extension ge0/0
  no shutdown
 !
 interface ge0/3
  ip address 10.1.10.1/24
  tunnel-interface
   encapsulation ipsec
   color public-internet restrict
   vmanage-connection-preference 8
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
 ip route 0.0.0.0/0 10.1.10.254
 ip route 0.0.0.0/0 172.16.10.254
!
Branch1_vEdge1# sh run vpn 10
vpn 10
 interface ge0/1
  ip address 10.1.1.252/24
  no shutdown
  vrrp 10
   priority  110
   track-omp
   ipv4 10.1.1.254
  !
 !
 ip route 0.0.0.0/0 vpn 0
!
```
Branch1_vEdge1# sh run omp
```shell
omp
 no shutdown
 overlay-as       100
 graceful-restart
 advertise connected
!
```

Branch1_vEdge1# show bgp summary 
```shell
vpn                    0
bgp-router-identifier  10.10.10.11
local-as               11
rib-entries            21
rib-memory             2352
total-peers            2
peer-memory            9632
Local-soo              SoO:0:10
ignore-soo             
                       MSG       MSG       OUT                     PREFIX  PREFIX  PREFIX                
NEIGHBOR         AS    RCVD      SENT      Q      UPTIME           RCVD    VALID   INSTALLED  STATE      
---------------------------------------------------------------------------------------------------------
172.16.10.254    254   25        19        0      0:00:16:13       12      12      12         established
172.16.11.1      12    2         10        0      0:00:01:40       0       0       0          established
```

Branch1_vEdge1# show vrrp 
```shell
vrrp vpn 10
 interfaces ge0/1
  groups 10
   virtual-ip             10.1.1.254
   virtual-mac            00:00:5e:00:01:0a
   priority               110
   vrrp-state             master
   omp-state              up
   advertisement-timer    1
   master-down-timer      3
   last-state-change-time 2021-11-17T04:50:21+00:00
```