```shell
version 16.6
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
!
hostname Site2-SW
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
aaa new-model
!
!
aaa group server radius ISE
 server name psn-2
 server name pan-p
 server name pan-s
!
aaa group server tacacs+ qytang-tac-group
 server name qyt-tac
!
aaa authentication login noise line none
aaa authentication login qytangise group qytang-tac-group
aaa authentication dot1x default group ISE
aaa authorization exec qytangise group qytang-tac-group 
aaa authorization commands 1 qytcmd group qytang-tac-group 
aaa authorization commands 15 qytcmd group qytang-tac-group 
aaa authorization network default group ISE 
aaa accounting dot1x default start-stop group ISE
aaa accounting exec qytaccoun start-stop group qytang-tac-group
aaa accounting commands 1 qytcmd start-stop group qytang-tac-group
aaa accounting commands 15 qytcmd start-stop group qytang-tac-group
!
!         
!
!
!
aaa server radius dynamic-author
 client 10.1.20.241 server-key cisco
 client 10.1.100.241 server-key cisco
 client 10.1.100.242 server-key cisco
!
aaa session-id common
switch 1 provision ws-c3650-24ts
!
!
!
!
ip routing
!
ip name-server 10.1.100.200
!
!
!
!
!
!         
!
!
device-sensor accounting
!
!
device-tracking tracking
!
device-tracking policy IPDT_MAX_10
 limit address-count 10
 no protocol udp
 tracking enable
!
!
crypto pki trustpoint TP-self-signed-3753158802
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-3753158802
 revocation-check none
 rsakeypair TP-self-signed-3753158802
!
!
crypto pki certificate chain TP-self-signed-3753158802
!
dot1x system-auth-control
!
!
diagnostic bootup level minimal
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
username rejected
username ATTRIBUTES
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
 description QYT-Router
 switchport access vlan 102
 switchport mode access
 switchport voice vlan 99
 device-tracking attach-policy IPDT_MAX_10
 ip access-group ACL-DEFAULT in
 authentication event fail action next-method
 authentication event server dead action authorize vlan 102
 authentication event server alive action reinitialize 
 authentication host-mode multi-auth
 authentication open
 authentication order mab dot1x
 authentication priority dot1x mab
 authentication port-control auto
 authentication violation restrict
 mab
 dot1x pae authenticator
 spanning-tree portfast
!
interface GigabitEthernet1/0/2
 no switchport
 ip address 192.168.2.2 255.255.255.0
 cts manual 
  sap pmk 0000000000000000000000000000000000000000000000000000000000123456 mode-list gcm-encrypt   
!
interface GigabitEthernet1/0/3
 switchport access vlan 20
 switchport mode access
 spanning-tree portfast
!
interface GigabitEthernet1/0/4
!
interface GigabitEthernet1/0/5
!
interface GigabitEthernet1/0/6
 switchport access vlan 102
 switchport mode access
 device-tracking
 macsec   
 authentication port-control auto
 authentication violation protect
 dot1x pae authenticator
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
 shutdown
!
interface Vlan20
 ip address 10.1.20.254 255.255.255.0
!
interface Vlan99
 ip address 10.1.99.254 255.255.255.0
 ip helper-address 10.1.100.200
 ip helper-address 10.1.20.241
!
interface Vlan102
 ip address 10.1.102.254 255.255.255.0
 ip helper-address 10.1.100.200
!
router bgp 20
 bgp log-neighbor-changes
 redistribute connected
 neighbor 192.168.2.1 remote-as 100
 neighbor 192.168.2.1 ebgp-multihop 255
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
!
!
ip access-list extended ACL-DEFAULT
 remark DHCP
 permit udp any eq bootpc any eq bootps
 remark DNS
 permit udp any any eq domain
 remark Ping
 permit icmp any any
 remark TFTP
 permit udp any any eq tftp
 remark Drop all the rest
 deny   ip any any
ip access-list extended WEB-REDIRECT
 deny   udp any any eq domain
 deny   udp any host 10.1.20.241 eq 8905
 deny   udp any host 10.1.20.241 eq 8906
 deny   udp any host 10.1.20.241 eq 8909
 deny   tcp any host 10.1.20.241 eq 8905
 deny   tcp any host 10.1.20.241 eq 8909
 deny   tcp any host 10.1.20.241 eq 8443
 deny   udp any host 10.1.20.254 eq 8905
 deny   tcp any host 10.1.20.254 eq 8905
 permit ip any any
!
!
!
snmp-server community qytangro RO
snmp-server community qytangrw RW
snmp-server enable traps snmp linkdown linkup
snmp-server host 10.1.100.241 version 2c Site2-SW 
snmp-server host 10.1.100.242 version 2c Site2-SW 
snmp-server host 10.1.20.241 version 2c Site2-SW 
tacacs server qyt-tac
 address ipv4 10.1.20.241
 key cisco
!
radius-server attribute 6 on-for-login-auth
radius-server attribute 8 include-in-access-req
radius-server dead-criteria time 5 tries 3
!
radius server psn-2
 address ipv4 10.1.20.241 auth-port 1645 acct-port 1646
 key cisco
!
radius server pan-p
 address ipv4 10.1.100.241 auth-port 1645 acct-port 1646
 key cisco
!
radius server pan-s
 address ipv4 10.1.100.242 auth-port 1645 acct-port 1646
 key cisco
!
!
control-plane
 service-policy input system-cpp-policy
!
privilege exec level 1 show running-config
privilege exec level 1 show
!
line con 0
 exec-timeout 0 0
 password cisco
 login authentication noise
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 authorization commands 1 qytcmd
 authorization commands 15 qytcmd
 authorization exec qytangise
 accounting commands 1 qytcmd
 accounting commands 15 qytcmd
 accounting exec qytaccoun
 login authentication qytangise
line vty 5 15
 authorization commands 1 qytcmd
 authorization commands 15 qytcmd
 authorization exec qytangise
 accounting commands 1 qytcmd
 accounting commands 15 qytcmd
 accounting exec qytaccoun
 login authentication qytangise
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