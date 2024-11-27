### 配置QoS策略
```shell
class-map match-all qyt-qos-class-map-match-ftp
  description qyt-qos-class-map-match-ftp
 match protocol ftp
class-map match-any qyt-qos-class-map-match-youtube-and-facebook
  description qyt-qos-class-map-match-youtube-and-facebook
 match protocol youtube
 match protocol facebook
policy-map qyt-qos-policy
 class qyt-qos-class-map-match-ftp
  police cir 100000
   conform-action transmit
   exceed-action drop
 class qyt-qos-class-map-match-youtube-and-facebook
  police cir 8000
   conform-action drop
   exceed-action drop

wireless profile policy qyt-central-wir-profile-policy
 shutdown
 service-policy input qyt-qos-policy
 service-policy output qyt-qos-policy
 service-policy client input qyt-qos-policy
 service-policy client output qyt-qos-policy
 no shutdown

```

### 可以在Service-Template中添加QoS
```shell
service-template qyt-service-template
 access-group wlan-acl
 vlan 30
 service-policy qos input qyt-qos-policy
 service-policy qos output qyt-qos-policy

```
