### 最基本的中心转发的PSK(注意:我的测试网卡只要激活PSK的FT[security wpa akm ft psk]就肯定连接不了)
### 同时激活WPA2和WPA3的情况下，总是使用WPA2
### 使用SAE
```shell
vlan 30
  name qyt-client-vlan30
!
wireless profile policy qyt-central-wir-profile-policy
 vlan qyt-client-vlan30
 no shutdown
!
wlan qyt-wpa2-psk 1 qyt-wpa2-psk
 security wpa psk set-key ascii 0 Cisc0123.com
 no security wpa akm dot1x
 security wpa akm psk
 no shutdown
!
wlan qyt-wpa2-wap3-psk 2 qyt-wpa2-wap3-psk
 no security ft adaptive
 security wpa psk set-key ascii 0 Cisc0123.com
 no security wpa akm dot1x
 security wpa akm psk
 security wpa akm sae
 security wpa wpa3
 security pmf mandatory
 no shutdown
!
wlan qyt-wap3-psk 3 qyt-wpa3-psk
 no security ft adaptive
 no security wpa wpa2
 security wpa psk set-key ascii 0 Cisc0123.com
 no security wpa akm dot1x
 security wpa akm sae
 security wpa wpa3
 security pmf mandatory
 no shutdown
!
wireless tag policy qyt-central-wir-tag-policy
 wlan qyt-wpa2-psk policy qyt-central-wir-profile-policy
 wlan qyt-wpa2-wap3-psk policy qyt-central-wir-profile-policy
 wlan qyt-wap3-psk policy qyt-central-wir-profile-policy
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
 ap-eth-mac 5486.BC48.09E8
 ap-eth-mac 0c75.bdb5.fcd0
 tag policy qyt-central-wir-tag-policy
 tag rf qyt-wir-tag-rf
 tag site qyt-central-wir-tag-site

```
