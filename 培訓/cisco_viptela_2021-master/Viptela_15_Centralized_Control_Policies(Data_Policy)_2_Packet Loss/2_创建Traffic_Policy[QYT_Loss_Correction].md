### 创建Traffic Policy
Configuration --- Policies --- Custom Options --- Centralized Policy --- Traffic Policy

Traffic Data
+ New Policy

Name: 
QYT_Loss_Correction

Description
QYT_Loss_Correction

=================Cutstom=====================
Match Conditions
Application/Application Family List:       Audio_Video_APPS

Actions:
Accept
Local TLOC List:        :mpls
        Encapsulation   :IPSEC
        Restrict:        勾√

Loss Correction:    FEC Adaptive [选择]
                    FFC Always
                    Packet Duplication

------------------------------------------
Default Action
Accept  Enabled


理论: P 271 (299/608)
```shell
there are two different FEC configuration modes: FEC-always and FEC-adaptive. FEC-always operates
exactly as it sounds: the FEC process takes place unconditionally. FEC-adaptive, on the
other hand, only operates when the loss percentage on the transport link is detected to be
more than 2%. As of 19.2 code, this 2% value is static and is not configurable.
```
