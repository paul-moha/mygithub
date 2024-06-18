```shell
version 16.6
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
!
hostname Center-SW
!
!
vrf definition Mgmt-vrf
 !
 address-family ipv4
 exit-address-family
 !
 address-family ipv6
 exit-address-family
!
!
no aaa new-model
switch 1 provision ws-c3650-24ts
!
!
!
!
ip routing
!
!
!
!
!
!
!
!
!
!
!
!
crypto pki trustpoint TP-self-signed-2069098
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-2069098
 revocation-check none
 rsakeypair TP-self-signed-2069098
!
!
crypto pki certificate chain TP-self-signed-2069098
!
!
!
diagnostic bootup level minimal
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
username admin privilege 15 password 0 Cisc0123
!
redundancy
 mode sso
!
!
transceiver type all
 monitoring
!
!
class-map match-any system-cpp-police-topology-control
  description Topology control
class-map match-any system-cpp-police-sw-forward
  description Sw forwarding, L2 LVX data, LOGGING
class-map match-any system-cpp-default
  description DHCP Snooping, EWLC control, EWCL data 
class-map match-any system-cpp-police-sys-data
  description Learning cache ovfl, Crypto Control, Exception, EGR Exception, NFL SAMPLED DATA, RPF Failed
class-map match-any system-cpp-police-punt-webauth
  description Punt Webauth
class-map match-any system-cpp-police-l2lvx-control
  description L2 LVX control packets
class-map match-any system-cpp-police-forus
  description Forus Address resolution and Forus traffic
class-map match-any system-cpp-police-multicast-end-station
  description MCAST END STATION
class-map match-any system-cpp-police-multicast
  description Transit Traffic and MCAST Data
class-map match-any system-cpp-police-l2-control
  description L2 control
class-map match-any system-cpp-police-dot1x-auth
  description DOT1X Auth
class-map match-any system-cpp-police-data
  description ICMP redirect, ICMP_GEN and BROADCAST
class-map match-any system-cpp-police-stackwise-virt-control
  description Stackwise Virtual
class-map match-any non-client-nrt-class
class-map match-any system-cpp-police-routing-control
  description Routing control
class-map match-any system-cpp-police-protocol-snooping
  description Protocol snooping
class-map match-any system-cpp-police-system-critical
  description System Critical and Gold
!
policy-map system-cpp-policy
!
! 
!
!
!
!
!
!
!
!
!
!
!         
!
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 shutdown
 speed 1000
 negotiation auto
!
interface GigabitEthernet1/0/1
 no switchport
 ip address 192.168.1.1 255.255.255.0
 cts manual 
  sap pmk 0000000000000000000000000000000000000000000000000000000000123456 mode-list gcm-encrypt   
!
interface GigabitEthernet1/0/2
 no switchport
 ip address 192.168.2.1 255.255.255.0
 cts manual 
  sap pmk 0000000000000000000000000000000000000000000000000000000000123456 mode-list gcm-encrypt   
!
interface GigabitEthernet1/0/3
!
interface GigabitEthernet1/0/4
!
interface GigabitEthernet1/0/5
!
interface GigabitEthernet1/0/6
!
interface GigabitEthernet1/0/7
!
interface GigabitEthernet1/0/8
!
interface GigabitEthernet1/0/9
!
interface GigabitEthernet1/0/10
!
interface GigabitEthernet1/0/11
!
interface GigabitEthernet1/0/12
!
interface GigabitEthernet1/0/13
!
interface GigabitEthernet1/0/14
!         
interface GigabitEthernet1/0/15
!
interface GigabitEthernet1/0/16
!
interface GigabitEthernet1/0/17
!
interface GigabitEthernet1/0/18
!
interface GigabitEthernet1/0/19
!
interface GigabitEthernet1/0/20
!
interface GigabitEthernet1/0/21
!
interface GigabitEthernet1/0/22
!
interface GigabitEthernet1/0/23
!
interface GigabitEthernet1/0/24
 switchport mode trunk
!
interface GigabitEthernet1/1/1
!         
interface GigabitEthernet1/1/2
!
interface GigabitEthernet1/1/3
!
interface GigabitEthernet1/1/4
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan100
 ip address 10.1.100.254 255.255.255.0
!
router bgp 100
 bgp log-neighbor-changes
 redistribute connected
 redistribute static
 neighbor 10.1.100.253 remote-as 100
 neighbor 192.168.1.2 remote-as 10
 neighbor 192.168.1.2 ebgp-multihop 255
 neighbor 192.168.2.2 remote-as 20
 neighbor 192.168.2.2 ebgp-multihop 255
 default-information originate
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
ip route 0.0.0.0 0.0.0.0 10.1.100.253
!
!
!
!
!
!
control-plane
 service-policy input system-cpp-policy
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 login
line vty 5 15
 login
!
!
!
!
!
!
!
end
```