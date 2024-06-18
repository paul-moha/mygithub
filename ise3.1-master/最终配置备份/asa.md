```shell
ASA# more system:running-config
: Saved
:
: Serial Number: 9A2HST8XB3A
: Hardware:   ASAv, 4096 MB RAM, CPU Pentium II 2499 MHz, 1 CPU (3 cores)
: Written by enable_15 at 14:16:30.137 UTC Tue Feb 7 2023
!
ASA Version 9.3(1)
!
hostname ASA
enable password 8Ry2YjIyt7RRXU24 encrypted
names
ip local pool sslpool 172.16.1.100-172.16.1.200
!
interface GigabitEthernet0/0
 nameif Outside
 security-level 0
 ip address 202.100.1.10 255.255.255.0
!
interface GigabitEthernet0/1
 nameif Inside
 security-level 100
 ip address 10.1.100.253 255.255.255.0
!
interface GigabitEthernet0/2
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/3
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/4
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/5
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/6
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/7
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/8
 shutdown
 no nameif
 no security-level
 no ip address
!
interface Management0/0
 management-only
 shutdown
 no nameif
 no security-level
 no ip address
!
ftp mode passive
same-security-traffic permit intra-interface
access-list out extended permit ip any any
access-list split standard permit 10.1.100.0 255.255.255.0
access-list split standard permit 10.1.101.0 255.255.255.0
access-list split standard permit 10.1.102.0 255.255.255.0
pager lines 23
mtu Outside 1500
mtu Inside 1500
no failover
icmp unreachable rate-limit 1 burst-size 1
no asdm history enable
arp timeout 14400
no arp permit-nonconnected
access-group out in interface Outside
router bgp 100
 bgp log-neighbor-changes
 address-family ipv4 unicast
  neighbor 10.1.100.254 remote-as 100
  neighbor 10.1.100.254 activate
  network 172.16.1.0 mask 255.255.255.0
  no auto-summary
  no synchronization
 exit-address-family
!
route Outside 0.0.0.0 0.0.0.0 202.100.1.254 1
route Inside 10.1.0.0 255.255.0.0 10.1.100.254 1
timeout xlate 3:00:00
timeout pat-xlate 0:00:30
timeout conn 1:00:00 half-closed 0:10:00 udp 0:02:00 icmp 0:00:02
timeout sunrpc 0:10:00 h323 0:05:00 h225 1:00:00 mgcp 0:05:00 mgcp-pat 0:05:00
timeout sip 0:30:00 sip_media 0:02:00 sip-invite 0:03:00 sip-disconnect 0:02:00
timeout sip-provisional-media 0:02:00 uauth 0:05:00 absolute
timeout tcp-proxy-reassembly 0:01:00
timeout floating-conn 0:00:00
aaa-server ISE protocol radius
aaa-server ISE (Inside) host 10.1.100.241
 key cisco
user-identity default-domain LOCAL
aaa authentication ssh console LOCAL
aaa authentication http console LOCAL
http server enable
http 0.0.0.0 0.0.0.0 Inside
no snmp-server location
no snmp-server contact
crypto ipsec security-association pmtu-aging infinite
crypto ca trustpool policy
telnet timeout 5
no ssh stricthostkeycheck
ssh 0.0.0.0 0.0.0.0 Inside
ssh timeout 5
ssh key-exchange group dh-group1-sha1
console timeout 0
!
tls-proxy maximum-session 500
!
threat-detection basic-threat
threat-detection statistics access-list
no threat-detection statistics tcp-intercept
webvpn
 enable Outside
 anyconnect-essentials
 anyconnect image disk0:/anyconnect-win-4.5.05030-webdeploy-k9.pkg 1
 anyconnect enable
 error-recovery disable
group-policy qyt-ise3 internal
group-policy qyt-ise3 attributes
 vpn-tunnel-protocol ssl-client ssl-clientless
 split-tunnel-policy tunnelspecified
 split-tunnel-network-list value split
 address-pools value sslpool
dynamic-access-policy-record DfltAccessPolicy
username admin password G4qwzPsg17jLVE/S encrypted privilege 15
tunnel-group DefaultWEBVPNGroup general-attributes
 authentication-server-group ISE
!
class-map inspection_default
 match default-inspection-traffic
!
!
policy-map type inspect dns preset_dns_map
 parameters
  message-length maximum client auto
  message-length maximum 512
policy-map global_policy
 class inspection_default
  inspect rtsp
  inspect sunrpc
  inspect xdmcp
  inspect netbios
  inspect tftp
  inspect ip-options
  inspect dns preset_dns_map
  inspect ftp
  inspect h323 h225
  inspect h323 ras
  inspect rsh
  inspect esmtp
  inspect sqlnet
  inspect sip
  inspect skinny
!
service-policy global_policy global
prompt hostname context
no call-home reporting anonymous
Cryptochecksum:46ca7d679fdee447f26c61fa4e958ebd
: end

```