### 配置dot1x
```shell
aaa new-model
!
aaa session-id common
!
aaa authentication dot1x ise_authen group radius
aaa authentication login qyt-vty local
aaa authorization exec qyt-vty local
aaa authentication login noacs line none
!
line con 0
  login authentication noacs
line vty 0 15
  authorization exec qyt-vty
  login authentication qyt-vty
!
aaa server radius dynamic-author
 client 10.1.1.30
!
radius server ise
 address ipv4 10.1.1.30 auth-port 1812 acct-port 1813
 key Cisc0123
!
vlan 30
  name qyt-client-vlan30
!
vlan 20
  name qyt-client-vlan20
!
wireless profile policy qyt-central-wir-profile-policy
 shutdown
 aaa-override
 nac
 vlan qyt-client-vlan30
 no shutdown
!
wlan qyt-wpa2-dot1x 6 qyt-wpa2-dot1x
 security ft
 security wpa akm ft dot1x
 security dot1x authentication-list ise_authen
 no shutdown
!
wlan qyt-wpa2-wpa3-dot1x 7 qyt-wpa2-wpa3-dot1x
 security ft
 security wpa akm ft dot1x
 security wpa wpa3
 security dot1x authentication-list ise_authen
 security pmf mandatory
 no shutdown
!
wlan qyt-wpa3-dot1x 8 qyt-wpa3-dot1x
 security ft
 no security wpa wpa2
 no security wpa akm dot1x
 security wpa akm ft dot1x
 security wpa wpa3
 security dot1x authentication-list ise_authen
 security pmf mandatory
 no shutdown
!
wireless tag policy qyt-central-wir-tag-policy
 wlan qyt-wpa2-dot1x policy qyt-central-wir-profile-policy
 wlan qyt-wpa2-wpa3-dot1x policy qyt-central-wir-profile-policy
 wlan qyt-wpa3-dot1x policy qyt-central-wir-profile-policy
!
ap profile qyt-ap-profile
 mgmtuser username admin password 0 Cisc0123 secret 0 Cisc0123
!
wireless tag site qyt-central-wir-tag-site
 ap-profile qyt-ap-profile
!
wireless tag rf qyt-wir-tag-rf
 24ghz-rf-policy Typical_Client_Density_rf_24gh
 5ghz-rf-policy Typical_Client_Density_rf_5gh
!
ap location name qyt-central-ap-location
 ap-eth-mac 70d3.79e0.5d20
 ap-eth-mac 0c75.bdb5.fcd0
 tag policy qyt-central-wir-tag-policy
 tag rf qyt-wir-tag-rf
 tag site qyt-central-wir-tag-site
!
no wireless wps client-exclusion dot11-assoc
no wireless wps client-exclusion dot1x-auth
no wireless wps client-exclusion dot1x-timeout
no wireless wps client-exclusion ip-theft
no wireless wps client-exclusion web-auth
!
ip access-list extended wlan-acl
 10 deny icmp any host 10.1.1.102
 20 permit ip any any

```

### 测试AAA
```shell
qytwlc1#test aaa group radius server name ise dot1xuser Cisc0123 new-code
User successfully authenticated

USER ATTRIBUTES

username             0   "dot1xuser"

```

### 配置Flex的Dot1x(需要PSK的配置)
```shell
aaa new-model
!
aaa session-id common
!
aaa authentication dot1x ise_authen group radius
aaa authentication login qyt-vty local
aaa authorization exec qyt-vty local
aaa authentication login noacs line none
!
line con 0
  login authentication noacs
line vty 0 15
  authorization exec qyt-vty
  login authentication qyt-vty
!
aaa server radius dynamic-author
 client 10.1.1.30
!
radius server ise
 address ipv4 10.1.1.30 auth-port 1812 acct-port 1813
 key Cisc0123
!
wlan qyt-flex-wpa2-dot1x 13 qyt-flex-wpa2-dot1x
 security ft
 security wpa akm ft dot1x
 security dot1x authentication-list ise_authen
 no shutdown
!
wireless profile flex qyt-flex-profile
 vlan-name qyt-client-vlan20
  vlan-id 20
!
wireless tag policy qyt-flex-wir-tag-policy
 wlan qyt-flex-wpa2-dot1x policy qyt-flex-wir-profile-policy
!
wireless profile policy qyt-flex-wir-profile-policy
 shutdown
 aaa-override
 nac
 no shutdown

```
