```shell
version 16.6
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
!
hostname Site1-SW
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
crypto pki trustpoint TP-self-signed-3340664954
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-3340664954
 revocation-check none
 rsakeypair TP-self-signed-3340664954
!
!
crypto pki certificate chain TP-self-signed-3340664954
!
!
!
diagnostic bootup level minimal
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
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
 speed 1000
 negotiation auto
!
interface GigabitEthernet1/0/1
 no switchport
 ip address 192.168.1.2 255.255.255.0
 cts manual 
  sap pmk 0000000000000000000000000000000000000000000000000000000000123456 mode-list gcm-encrypt   
!
interface GigabitEthernet1/0/2
 description to AP
 switchport trunk native vlan 12
 switchport mode trunk
!
interface GigabitEthernet1/0/3
 description to PSN-1
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/4
 description to C9800-CL
 switchport trunk native vlan 11
 switchport mode trunk
!
interface GigabitEthernet1/0/5
!
interface GigabitEthernet1/0/6
 description to WIN10-1
 switchport access vlan 101
 switchport mode access
 spanning-tree portfast
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
 shutdown
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
!
interface Vlan10
 ip address 10.1.10.254 255.255.255.0
!
interface Vlan11
 ip address 10.1.11.254 255.255.255.0
!
interface Vlan12
 ip address 10.1.12.254 255.255.255.0
 ip helper-address 10.1.100.200
!
interface Vlan101
 ip address 10.1.101.254 255.255.255.0
 ip helper-address 10.1.100.200
!
router bgp 10
 bgp log-neighbor-changes
 redistribute connected
 neighbor 192.168.1.1 remote-as 100
 neighbor 192.168.1.1 ebgp-multihop 255
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
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
mac address-table notification mac-move
!
!
!
!
!
end
```