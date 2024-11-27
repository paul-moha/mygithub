Gateway# sh run vpn 0
```shell
vpn 0
 dns 202.100.100.200 primary
 interface ge0/0
  ip address 202.100.50.1/24
  nat
  !
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
 ip route 0.0.0.0/0 202.100.50.254
```

Gateway# sh run vpn 10
```shell
vpn 10
 interface ge0/1
  ip address 10.1.5.1/24
  no shutdown
 !
 ip route 0.0.0.0/0 vpn 0
!
```

Gateway# sh run omp
```shell
omp
 no shutdown
 overlay-as       100
 graceful-restart
 advertise connected
!
```