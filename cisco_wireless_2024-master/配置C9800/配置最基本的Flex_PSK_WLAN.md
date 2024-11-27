### 最基本的Flex的PSK
```shell
vlan 30
  name qyt-client-vlan30
!
wireless profile policy qyt-flex-wir-profile-policy
 no central dhcp
 no central switching
 vlan qyt-client-vlan30
 no shutdown
!
wlan qyt-flex 4 qyt-flex
 security wpa psk set-key ascii 0 Cisc0123.com
 no security wpa akm dot1x
 security wpa akm psk
 no shutdown
!
wireless tag policy qyt-flex-wir-tag-policy
 wlan qyt-flex policy qyt-flex-wir-profile-policy
!
wireless profile flex qyt-flex-profile
 native-vlan-id 20
 vlan-name qyt-client-vlan30
  vlan-id 30
!
ap profile qyt-ap-profile
 mgmtuser username admin password 0 Cisc0123 secret 0 Cisc0123
!
wireless tag site qyt-flex-wir-tag-site
 no local-site
 ap-profile qyt-ap-profile
 flex-profile qyt-flex-profile
!
wireless tag rf qyt-wir-tag-rf
 24ghz-rf-policy Typical_Client_Density_rf_24gh
 5ghz-rf-policy Typical_Client_Density_rf_5gh
!
ap location name qyt-flex-ap-location
 ap-eth-mac 5486.BC48.09E8
 ap-eth-mac 0c75.bdb5.fcd0
 tag policy qyt-flex-wir-tag-policy
 tag rf qyt-wir-tag-rf
 tag site qyt-flex-wir-tag-site

```