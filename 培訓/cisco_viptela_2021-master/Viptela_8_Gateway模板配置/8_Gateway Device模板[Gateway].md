Configuration --- Templates --- Device

模板类型:Device
+ Create Template --- From Feature Template

=========================================================
Device Model: vEdge Cloud
Template Name : Gateway
Description : Gateway

---------Basic Information---------
OMP : Gateway_vEdge_OMP

---------Transport & Management VPN---------
VPN0: Gateway_vEdge_VPN0

+ VPN Interface

VPN Interface : Gateway_vEdge_Interface_GE0/0

==============================================

VPN 512: VPN512

+ VPN Interface

VPN Interface : ETH0

---------Service VPN---------
+ Add VPN

Selected VPN Templates : Gateway_vEdge_VPN10

+ VPN Interface

VPN Interface : Gateway_vEdge_Interface_GE0/1


### 模板 Attach Device
Selected Devices: Gateway

注意: 导入csv的时候需要替换csv-deviceId为Chassis Number