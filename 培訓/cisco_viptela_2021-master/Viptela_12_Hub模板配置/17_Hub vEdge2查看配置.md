Hub_vEdge1# show run vpn 0
```shell
vpn 0
 dns 202.100.100.200 primary
 router
  bgp 140
   address-family ipv4-unicast
    network 0.0.0.0/0
    network 10.1.241.0/24
   !
   neighbor 172.16.41.1
    no shutdown
    remote-as     4
    ebgp-multihop 255
   !
   neighbor 172.16.141.254
    no shutdown
    remote-as     254
    ebgp-multihop 255
   !
  !
 !
 interface ge0/0
  ip address 202.100.41.1/24
  nat
  !
  no shutdown
 !
 interface ge0/1
  ip address 172.16.141.1/24
  no shutdown
 !
 interface ge0/2
  ip address 172.16.41.254/24
  no shutdown
 !
 interface loopback1
  ip address 10.1.141.1/24
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
  ip address 10.1.241.1/24
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
 ip route 0.0.0.0/0 202.100.41.254
!
```

Hub_vEdge1# sh run vpn 10
```shell
vpn 10
 router
  bgp 40
   propagate-aspath
   address-family ipv4-unicast
    network 0.0.0.0/0
   !
   neighbor 10.1.41.1
    no shutdown
    remote-as     4
    ebgp-multihop 255
   !
  !
 !
 interface ge0/3
  ip address 10.1.41.254/24
  no shutdown
 !
 ip route 0.0.0.0/0 vpn 0
!
```

Hub_vEdge1# sh run omp
```shell
omp
 no shutdown
 overlay-as       100
 graceful-restart
 advertise bgp
!
```

Hub_vEdge1# show bgp summary 
```shell
vpn                    0
bgp-router-identifier  10.10.10.41
local-as               140
rib-entries            19
rib-memory             2128
total-peers            2
peer-memory            9632
Local-soo              SoO:0:40
ignore-soo             
                       MSG       MSG       OUT                     PREFIX  PREFIX  PREFIX                
NEIGHBOR         AS    RCVD      SENT      Q      UPTIME           RCVD    VALID   INSTALLED  STATE      
---------------------------------------------------------------------------------------------------------
172.16.41.1      4     6         9         0      0:00:01:24       2       2       1          established
172.16.141.254   254   7         6         0      0:00:01:24       8       8       8          established


vpn                    10
bgp-router-identifier  10.10.10.41
local-as               40
rib-entries            19
rib-memory             2128
total-peers            1
peer-memory            4816
Local-soo              SoO:0:40
ignore-soo             
                       MSG       MSG       OUT                     PREFIX  PREFIX  PREFIX                
NEIGHBOR         AS    RCVD      SENT      Q      UPTIME           RCVD    VALID   INSTALLED  STATE      
---------------------------------------------------------------------------------------------------------
10.1.41.1        4     11        6         0      0:00:01:20       10      10      10         established
```