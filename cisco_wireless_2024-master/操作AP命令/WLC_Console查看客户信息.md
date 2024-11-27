### 查看客户
```shell
qytwlc1#show wireless client summary
Number of Clients: 1

MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
-------------------------------------------------------------------------------------------------------------------------
a063.91bb.cffc AP1                                            WLAN 3    Run               11n(2.4) Dot1x      Local

```

### 查看客户详细信息
```shell
qytwlc1#show wireless client summary detail
Number of Clients: 1

MAC Address    SSID                             AP Name                          State         IP Address                                 Device-type                      VLAN  BSSID          Auth Method                    Created          Connected        Protocol Channel Width   SGI NSS Rate   CAP   Username                                                         Rx packets      Tx packets      Rx bytes        Tx bytes      6E capability
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a063.91bb.cffc qyt-dot1x                        AP1                              Run           30.1.1.1                                                                    30    70d3.79e1.d321 [802.1x]                       30:07            30:11            11n(2.4) 6        20/20  Y/Y 2/2 m7     E     dot1xuser                                                        659              284              85808            57219            N
                                                                                               fe80::f570:a2c9:ad8c:d8ff
```

### 查询特定用户名的client
```shell
qytwlc1#show wireless client username dot1xuser
Number of Clients: 1

MAC Address         AP Name                           Status             Type  ID             Auth  Protocol
-------------------------------------------------------------------------------------------------------------
a063.91bb.cffc      AP2                               Run                WLAN  3              Yes   11n(2.4)
```

### 查看客户详细信息
```shell
qytwlc1#show wireless client mac-address a063.91bb.cffc detail

Client MAC Address : a063.91bb.cffc
Client MAC Type : Universally Administered Address
Client DUID: NA
Client IPv4 Address : 30.1.1.1
Client IPv6 Addresses : fe80::f570:a2c9:ad8c:d8ff
Client Username : dot1xuser
AP MAC Address : 0c75.bdb3.b8a0
AP Name: AP2
AP slot : 0
Client State : Associated
Policy Profile : qyt-central-wir-profile-policy
Flex Profile : N/A
Wireless LAN Id: 3
WLAN Profile Name: qyt-dot1x
Wireless LAN Network Name (SSID): qyt-dot1x
BSSID : 0c75.bdb3.b8a1
Connected For : 569 seconds
Protocol : 802.11n - 2.4 GHz
Channel : 1
Client IIF-ID : 0xa0000001
Association Id : 1
Authentication Algorithm : Open System
Idle state timeout : N/A
Re-Authentication Timeout : 1800 sec (Remaining time: 1233 sec)
Session Warning Time : Timer not running
Input Policy Name  : None
Input Policy State : None
Input Policy Source : None
Output Policy Name  : None
Output Policy State : None
Output Policy Source : None
WMM Support : Enabled
U-APSD Support : Disabled
Fastlane Support : Disabled
Client Active State : Active
Power Save : OFF
Current Rate : m15
Supported Rates : 9.0,12.0,18.0,24.0,36.0,48.0,54.0
AAA QoS Rate Limit Parameters:
  QoS Average Data Rate Upstream             : 0 (kbps)
  QoS Realtime Average Data Rate Upstream    : 0 (kbps)
  QoS Burst Data Rate Upstream               : 0 (kbps)
  QoS Realtime Burst Data Rate Upstream      : 0 (kbps)
  QoS Average Data Rate Downstream           : 0 (kbps)
  QoS Realtime Average Data Rate Downstream  : 0 (kbps)
  QoS Burst Data Rate Downstream             : 0 (kbps)
  QoS Realtime Burst Data Rate Downstream    : 0 (kbps)
Mobility:
  Move Count                  : 0
  Mobility Role               : Local
  Mobility Roam Type          : None
  Mobility Complete Timestamp : 06/01/2024 20:19:29 GMT
Client Join Time:
  Join Time Of Client : 06/01/2024 20:49:50 GMT
Client State Servers : None
Client ACLs : None
Policy Manager State: Run
Last Policy Manager State : IP Learn Complete
Client Entry Create Time : 2390 seconds
Policy Type : WPA2
Encryption Cipher : CCMP (AES)
Authentication Key Management : 802.1x
Transition Disable Bitmap : None
User Defined (Private) Network : Disabled
User Defined (Private) Network Drop Unicast : Disabled
Encrypted Traffic Analytics : No
Protected Management Frame - 802.11w : No
EAP Type : PEAP
VLAN Override after Webauth : No
VLAN : qyt-client-vlan30
Multicast VLAN : 0
WiFi Direct Capabilities:
  WiFi Direct Capable           : No
Central NAT : DISABLED
Session Manager:
  Point of Attachment : capwap_90000002
  IIF ID             : 0x90000002
  Authorized         : TRUE
  Session timeout    : 1800
  Common Session ID: 3201010A00000012D3BD890B
  Acct Session ID  : 0x00000000
  Last Tried Aaa Server Details:
        Server IP : 10.1.1.30
  Auth Method Status List
        Method : Dot1x
                SM State         : AUTHENTICATED
                SM Bend State    : IDLE
  Local Policies:
        Service Template : wlan_svc_qyt-central-wir-profile-policy_local (priority 254)
                VLAN             : qyt-client-vlan30
                Absolute-Timer   : 1800
  Server Policies:
  Resultant Policies:
                VLAN Name        : qyt-client-vlan30
                VLAN             : 30
                Absolute-Timer   : 1800
DNS Snooped IPv4 Addresses : None
DNS Snooped IPv6 Addresses : None
Client Capabilities
  CF Pollable : Not implemented
  CF Poll Request : Not implemented
  Short Preamble : Not implemented
  PBCC : Not implemented
  Channel Agility : Not implemented
  Listen Interval : 0
Fast BSS Transition Details :
  Reassociation Timeout : 20
11v BSS Transition : Not implemented
11v DMS Capable : No
QoS Map Capable : No
FlexConnect Data Switching : N/A
FlexConnect Dhcp Status : N/A
FlexConnect Authentication : N/A
Client Statistics:
  Number of Bytes Received from Client : 179239
  Number of Bytes Sent to Client : 118596
  Number of Packets Received from Client : 1404
  Number of Packets Sent to Client : 734
  Number of Policy Errors : 0
  Radio Signal Strength Indicator : -37 dBm
  Signal to Noise Ratio : 62 dB
Fabric status : Disabled
Radio Measurement Enabled Capabilities
  Capabilities: None
Client Scan Report Time : Timer not running
Client Scan Reports
Assisted Roaming Neighbor List
Nearby AP Statistics:
EoGRE : Pending Classification
Max Client Protocol Capability: 802.11n
WiFi to Cellular Steering : Not implemented
Cellular Capability : N/A
Advanced Scheduling Requests Details:
  Apple Specific Requests(ASR) Capabilities/Statistics:
    Regular ASR support: DISABLED

```


### 查看漫游信息
```shell
qytwlc1#show wireless client mac-address a063.91bb.cffc mobility history

Recent association history (most recent on top):

AP Name                                       BSSID           AP Slot    Assoc Time               Instance   Mobility Role   Run Latency (ms)     Dot11 Roam Type
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
AP2                                           0c75.bdb3.b8a1  0          06/01/2024 20:49:50      0          Local           2042                 802.11i Slow
AP1                                           70d3.79e1.d321  0          06/01/2024 20:19:25      0          Local           4139                 N/A
```
