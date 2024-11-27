### 查看AP1 Inventory
```shell
qytwlc1#show ap name AP1 inventory
NAME: AP1800, DESCR: Cisco Aironet 1800 Series (IEEE 802.11ac) Access Point
PID: AIR-AP1832I-H-K9, VID: 02, SN: KWC211307Q8

```

### 修改AP1 txpower
```shell
qytwlc1#ap name AP1 dot11 24ghz txpower 1

```


### 查看AP2 Inventory
```shell
qytwlc1#show ap name AP2 inventory
NAME: C9130AX, DESCR: Cisco Catalyst 9130AX Series Access Point
PID: C9130AXI-E, VID: 01, SN: KWC23410BGY

```

### 修改AP2 txpower
```shell
qytwlc1#ap name AP2 dot11 24ghz shutdown
qytwlc1#ap name AP2 dot11 24ghz radio role manual client-serving
qytwlc1#ap name AP2 no dot11 24ghz shutdown
qytwlc1#ap name AP2 dot11 24ghz txpower 1
```

### 查看Tx Power信息
```shell
qytwlc1#show ap config slots
~~~忽略其他~~~
  Tx Power
    Number of Supported Power Levels            : 8
    Tx Power Level 1                            : 15 dBm
    Tx Power Level 2                            : 12 dBm
    Tx Power Level 3                            : 9 dBm
    Tx Power Level 4                            : 6 dBm
    Tx Power Level 5                            : 3 dBm
    Tx Power Level 6                            : 0 dBm
    Tx Power Level 7                            : -3 dBm
    Tx Power Level 8                            : -4 dBm
    Tx Power Configuration                      : Customized
    Current Tx Power Level                      : 1
    Tx Power Assigned By                        : User
```

