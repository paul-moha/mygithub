Branch2_cEdge#show sdwan running-config 
```shell       
system
 system-ip             10.10.10.20
 overlay-id            1
 site-id               20
 port-offset           1
 control-session-pps   300
 admin-tech-on-failure
 sp-organization-name  testrabbit
 organization-name     testrabbit
 port-hop
 track-transport
 track-default-gateway
 console-baud-rate     19200
 no on-demand enable
 on-demand idle-timeout 10
 vbond vbond.testrabbit.local port 12346
!
service tcp-keepalives-in
service tcp-keepalives-out
no service tcp-small-servers
no service udp-small-servers
hostname Branch2_cEdge
username admin privilege 15 secret 9 $9$3V6L3V6L2VUI2k$ysPnXOdg8RLj9KgMdmfHdSHkdaMmiHzGaUpcqH6pfTo
vrf definition 10
 rd 1:10
 address-family ipv4
  route-target export 2:10
  route-target import 2:10
  exit-address-family
 !
 address-family ipv6
  exit-address-family
 !
!
vrf definition Mgmt-intf
 description Transport VPN
 rd          1:512
 address-family ipv4
  route-target export 2:512
  route-target import 2:512
  exit-address-family
 !
 address-family ipv6
  exit-address-family
 !
!
ip arp proxy disable
no ip finger
no ip rcmd rcp-enable
no ip rcmd rsh-enable
no ip dhcp use class
ip name-server 202.100.100.200
ip route 0.0.0.0 0.0.0.0 10.1.20.2
ip route 0.0.0.0 0.0.0.0 202.100.20.254
ip bootp server
no ip source-route
no ip http server
no ip http secure-server
no ip igmp ssm-map query dns
ip nat settings central-policy
ip nat inside source list nat-dia-vpn-hop-access-list interface GigabitEthernet1 overload
ip nat translation tcp-timeout 3600
ip nat translation udp-timeout 60
ip nat route vrf 10 0.0.0.0 0.0.0.0 global
cdp run
interface GigabitEthernet1
 no shutdown
 arp timeout 1200
 ip address 202.100.20.1 255.255.255.0
 no ip redirects
 ip mtu    1500
 ip nat outside
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet2
 no shutdown
 arp timeout 1200
 ip address 10.1.20.10 255.255.255.0
 no ip redirects
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet3
 no shutdown
 arp timeout 1200
 vrf forwarding 10
 ip address 10.1.20.1 255.255.255.0
 no ip redirects
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet4
 no shutdown
 no ip address
exit
interface Tunnel1
 no shutdown
 ip unnumbered GigabitEthernet1
 no ip redirects
 ipv6 unnumbered GigabitEthernet1
 no ipv6 redirects
 tunnel source GigabitEthernet1
 tunnel mode sdwan
exit
interface Tunnel2
 no shutdown
 ip unnumbered GigabitEthernet2
 no ip redirects
 ipv6 unnumbered GigabitEthernet2
 no ipv6 redirects
 tunnel source GigabitEthernet2
 tunnel mode sdwan
exit
clock timezone UTC 0 0
logging persistent size 104857600 filesize 10485760
logging buffered 512000
logging persistent
aaa authentication login default local
aaa authorization exec default local
no crypto ikev2 diagnose error
no crypto isakmp diagnose error
router bgp 2
 bgp log-neighbor-changes
 distance bgp 20 200 20
 address-family ipv4 unicast vrf 10
  neighbor 10.1.20.254 remote-as 20
  neighbor 10.1.20.254 activate
  neighbor 10.1.20.254 ebgp-multihop 255
  neighbor 10.1.20.254 send-community both
  network 0.0.0.0 mask 0.0.0.0
  propagate-aspath
  exit-address-family
 !
 timers bgp 60 180
!
snmp-server ifindex persist
line con 0
 login authentication default
 speed    19200
 stopbits 1
!
line vty 0 4
 login authentication default
 transport input ssh
!
line vty 5 80
 transport input ssh
!
lldp run
nat64 translation timeout tcp 60
nat64 translation timeout udp 1
sdwan
 interface GigabitEthernet1
  tunnel-interface
   encapsulation ipsec weight 1
   no border
   color public-internet restrict
   no last-resort-circuit
   no low-bandwidth-link
   no vbond-as-stun-server
   vmanage-connection-preference 8
   port-hop
   carrier                       default
   nat-refresh-interval          5
   hello-interval                1000
   hello-tolerance               12
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
   no allow-service snmp
   no allow-service bfd
  exit
 exit
 interface GigabitEthernet2
  tunnel-interface
   encapsulation ipsec weight 1
   no border
   color mpls restrict
   no last-resort-circuit
   no low-bandwidth-link
   no vbond-as-stun-server
   vmanage-connection-preference 5
   port-hop
   carrier                       default
   nat-refresh-interval          5
   hello-interval                1000
   hello-tolerance               12
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
   no allow-service snmp
   no allow-service bfd
  exit
 exit
 appqoe
  no tcpopt enable
 !
 omp
  no shutdown
  overlay-as       100
  send-path-limit  4
  ecmp-limit       4
  graceful-restart
  no as-dot-notation
  timers
   holdtime               60
   advertisement-interval 1
   graceful-restart-timer 43200
   eor-timer              300
  exit
  address-family ipv4
   advertise bgp
  !
  address-family ipv6
   advertise connected
   advertise static
  !
 !
!
licensing config enable false
licensing config privacy hostname false
licensing config privacy version false
licensing config utility utility-enable false
bfd color lte
 hello-interval 1000
 no pmtu-discovery
 multiplier     1
!
bfd app-route multiplier 2
bfd app-route poll-interval 123400
security  
 ipsec
  rekey               86400
  replay-window       512
  authentication-type ah-sha1-hmac sha1-hmac
 !
!
sslproxy
 no enable
 rsa-key-modulus      2048
 certificate-lifetime 730
 eckey-type           P256
 ca-tp-label          PROXY-SIGNING-CA
 settings expired-certificate  drop
 settings untrusted-certificate drop
 settings unknown-status       drop
 settings certificate-revocation-check none
 settings unsupported-protocol-versions drop
 settings unsupported-cipher-suites drop
 settings failure-mode         close
 settings minimum-tls-ver      TLSv1
!
```

Branch2_cEdge#show ip bgp vpnv4 vrf 10 summary 
```shell
BGP router identifier 202.100.20.1, local AS number 2
BGP table version is 13, main routing table version 13
12 network entries using 3072 bytes of memory
12 path entries using 1632 bytes of memory
13/7 BGP path/bestpath attribute entries using 3952 bytes of memory
6 BGP AS-PATH entries using 224 bytes of memory
1 BGP community entries using 24 bytes of memory
1 BGP extended community entries using 24 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 8928 total bytes of memory
BGP activity 12/0 prefixes, 13/1 paths, scan interval 60 secs
12 networks peaked at 02:47:24 Nov 17 2021 UTC (00:04:56.790 ago)

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.1.20.254     4           20      15       9       13    0    0 00:04:56       11
```
