Branch1_vEdge1# sh run policy
```shell
policy
 lists
  prefix-list Prefix_Branch1_BGP_Out
   ip-prefix 10.1.1.0/24
   ip-prefix 172.16.11.0/24
  !
  prefix-list Prefix_Only_MPLS
   ip-prefix 10.1.6.0/24
  !
 !
 route-policy Branch1_BGP_Out
  sequence 1
   match
    address Prefix_Branch1_BGP_Out
   !
   action accept
   !
  !
  default-action reject
 !
 route-policy Branch1_Only_MPLS_Import_VPN10
  sequence 1
   match
    address Prefix_Only_MPLS
   !
   action accept
   !
  !
  default-action reject
 !
!
```

Branch1_vEdge1# sh run vpn 0 
```shell
vpn 0
 dns 202.100.100.200 primary
 router
  bgp 11
   address-family ipv4-unicast
    network 172.16.11.0/24
    redistribute static
   !
   neighbor 172.16.10.254
    no shutdown
    remote-as     254
    ebgp-multihop 255
    address-family ipv4-unicast
     route-policy Branch1_BGP_Out out
    !
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
```

Branch1_vEdge1# sh run vpn 10
```shell
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
 route-import bgp route-policy Branch1_Only_MPLS_Import_VPN10
 route-export connected
!
```