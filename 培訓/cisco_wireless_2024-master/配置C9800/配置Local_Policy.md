### 配置Local Policy
```shell
ip access-list extended wlan-acl
 10 deny icmp 30.1.1.0 0.0.0.255 host 10.1.1.102
 20 permit ip any any
!
service-template qyt-service-template
 access-group wlan-acl
 vlan 30
!
parameter-map type subscriber attribute-to-service qytang-policy-map-param
 1 map device-type eq "Microsoft-Workstation" username eq "iseuser"
  1 service-template qyt-service-template
!
policy-map type control subscriber qytang-policy-map
 event identity-update match-all
  1 class always do-until-failure
   1 map attribute-to-service table qytang-policy-map-param
!
device classifier
!
wireless profile policy qyt-central-wir-profile-policy
 shutdown
 dhcp-tlv-caching
 http-tlv-caching
 radius-profiling
 subscriber-policy-name qytang-policy-map
 vlan qyt-client-vlan30
 no shutdown

```

### 查看设备识别的效果
```shell
qytwlc1#show wireless client device summary
Number of Clients: 1
Active classified device summary

MAC Address       Device-type                       User-role                             Protocol-map
------------------------------------------------------------------------------------------------------
44af.2865.4096    Microsoft-Workstation                                                             41

qytwlc1#show wireless client device cache
Cached classified device info

MAC Address       Device-type                       User-role                             Protocol-map
------------------------------------------------------------------------------------------------------
44af.2865.4096    Microsoft-Workstation                                                             41

```

### 查看Local Policy引用到客户的效果
```shell
qytwlc1#show wireless client mac-address 44af.2865.4096 detail

~~~忽略大量输出~~~

Session Manager:
  Point of Attachment : capwap_90000005
  IIF ID             : 0x90000005
  Authorized         : TRUE
  Session timeout    : 1800
  Common Session ID: 0000000000000028EDC1F645
  Acct Session ID  : 0x00000000
  Auth Method Status List
        Method : Dot1x
                SM State         : AUTHENTICATED
                SM Bend State    : IDLE
  Local Policies:
        Service Template : qyt-service-template (priority 150)
                Filter-ID    : wlan-acl
                VLAN             : 30
        Service Template : wlan_svc_qyt-central-wir-profile-policy_local (priority 254)
                Absolute-Timer   : 1800
  Server Policies:
  Resultant Policies:
                Filter-ID        : wlan-acl
                VLAN Name        : qyt-client-vlan30
                VLAN             : 30
                Absolute-Timer   : 1800
```

