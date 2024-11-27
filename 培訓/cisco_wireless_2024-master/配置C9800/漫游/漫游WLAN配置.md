### Intra Controller Roaming
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
 no shutdown
!
wlan qyt-roaming 1 qyt-roaming
 security ft
 security wpa akm ft dot1x
 security dot1x authentication-list ise_authen
 no shutdown
!
wireless tag policy qyt-central-wir-tag-policy
 wlan qyt-roaming policy qyt-central-wir-profile-policy
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
 ap-eth-mac 5486.bc48.09e8
 ap-eth-mac 0c75.bdb5.fcd0
 ap-eth-mac 00bf.77fa.54e8
 tag policy qyt-central-wir-tag-policy
 tag rf qyt-wir-tag-rf
 tag site qyt-central-wir-tag-site
!
no wireless wps client-exclusion dot11-assoc
no wireless wps client-exclusion dot1x-auth
no wireless wps client-exclusion dot1x-timeout
no wireless wps client-exclusion ip-theft
no wireless wps client-exclusion web-auth

```