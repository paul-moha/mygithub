### 查看AP状态 [WLC Console配置]
```shell
qytwlc1#show ap summary
Number of APs: 1

CC = Country Code
RD = Regulatory Domain

AP Name                          Slots AP Model             Ethernet MAC   Radio MAC      CC   RD   IP Address                                State        Location
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
AP70D3.79E0.5D20                 2     AIR-AP1832I-H-K9     70d3.79e0.5d20 70d3.79e1.d320 CN   -H   20.1.1.4                                  Registered   qyt-central-ap-location

```

### 给AP改名字 [WLC Console配置]
```shell
ap name AP70D3.79E0.5D20 name AP1

ap name AP0C75.BDB5.FCD0 name AP2

```

### 配置backup controller
```shell
qytwlc1#ap name AP1 controller primary qytwlc1 100.1.1.101
qytwlc1#ap name AP1 controller secondary qytwlc2 100.1.1.102
```

### 配置AP Priority (1=low, 2=medium, 3=high, 4=critical)
```shell
qytwlc1#ap name AP1 priority 4
```


### 激活AP1(C9130AXI)的slot2
```shell
qytwlc1(config)#ap tri-radio

qytwlc1#ap name AP1 dot11 5ghz dual-radio mode enable
qytwlc1#ap name AP1 no dot11 5ghz slot 2 shutdown

```

### admin shutdown AP
```shell
ap name AP1 shutdown
ap name AP1 no shutdown

```

### 关闭射频口
```shell

ap name AP1 dot11 24ghz shutdown
ap name AP1 no dot11 24ghz shutdown
ap name AP1 dot11 5ghz shutdown
ap name AP1 no dot11 5ghz shutdown

```


### 查看AP配置
```shell
qytwlc1#show ap name AP1 config general

Cisco AP Name   : AP1
=================================================

Cisco AP Identifier                             : 70d3.79e1.d320
Country Code                                    : CN
Regulatory Domain Allowed by Country            : 802.11bg:-CE   802.11a:-CH   802.11 6GHz:
AP Country Code                                 : CN  - China
AP Regulatory Domain
  802.11bg                                      : -E
  802.11a                                       : -H
MAC Address                                     : 70d3.79e0.5d20
IP Address Configuration                        : DHCP
IP Address                                      : 20.1.1.6
IP Netmask                                      : 255.255.255.0
Gateway IP Address                              : 20.1.1.254
Fallback IP Address Being Used                  :
Domain                                          :
Name Server                                     :
CAPWAP Path MTU                                 : 1485
Capwap Active Window Size                       : 1
Telnet State                                    : Disabled
CPU Type                                        :  ARMv7 Processor rev 0 (v7l)
~~~~~~~~~~~忽略其他信息~~~~~~~~~~~
```

### 查看AP dot11 5ghz配置
```shell
qytwlc1#show ap name AP1 config dot11 5ghz
Cisco AP Identifier                             : 70d3.79e1.d320
Cisco AP Name                                   : AP1
Country Code                                    : CN
Regulatory Domain Allowed by Country            : 802.11bg:-CE   802.11a:-CH   802.11 6GHz:
AP Country Code                                 : CN  - China
AP Regulatory Domain                            : -H
MAC Address                                     : 70d3.79e0.5d20
IP Address Configuration                        : DHCP
IP Address                                      : Disabled
Telnet State                                    : Disabled
SSH State                                       : Disabled
Serial Console State                            : Enabled
Cisco AP Location                               : qyt-central-ap-location
Site Tag Name                                   : qyt-central-wir-tag-site
Administrative State                            : Enabled
Operation State                                 : Registered
AP Mode                                         : Local
~~~~~~~~~~~忽略其他信息~~~~~~~~~~~
```
