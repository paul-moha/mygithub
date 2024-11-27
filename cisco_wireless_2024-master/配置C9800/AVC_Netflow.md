### AVC配置
```shell
flow exporter wireless-local-exporter
 destination local wlc
!
flow exporter wireless-external-efk
 destination 10.1.1.101
 transport udp 2055
 template data timeout 30
!
flow monitor wireless-avc-basic
 exporter wireless-local-exporter
 cache timeout active 60
 record wireless avc basic
!
!
flow monitor wireless-avc-basic-ipv6
 exporter wireless-local-exporter
 cache timeout active 60
 record wireless avc ipv6 basic
!
!
flow monitor dwavc_basic
 exporter wireless-local-exporter
 exporter wireless-external-efk
 cache timeout active 60
 record wireless avc basic
!
!
flow monitor dwavc_ipv6_basic
 exporter wireless-local-exporter
 exporter wireless-external-efk
 cache timeout active 60
 record wireless avc ipv6 basic
!
wireless profile policy qyt-central-wir-profile-policy
 shutdown
 ipv4 flow monitor dwavc_basic input
 ipv4 flow monitor dwavc_basic output
 ipv6 flow monitor dwavc_ipv6_basic input
 ipv6 flow monitor dwavc_ipv6_basic output
 no shutdown

```

### 激活NBAR(需要shut/no shut)
```shell
wireless profile policy qyt-central-wir-profile-policy
 shutdown
 ip nbar protocol-discovery
 no shutdown
```

### 查看wireless profile policy详细信息
```shell
qytwlc1#show wireless profile policy detailed qyt-central-wir-profile-policy
~~~忽略其他部分~~~
AVC VISIBILITY                      : Enabled
NBAR Protocol Discovery             : Enabled

```