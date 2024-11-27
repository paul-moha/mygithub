Configuration --- Templates --- Device

模板类型:Device
+ Create Template --- From Feature Template

=========================================================
Device Model: vEdge Cloud
Template Name : Hub_vEdge1
Description : Hub_vEdge1

---------Basic Information---------
OMP : Hub_vEdge_OMP

---------Transport & Management VPN---------
VPN0: Hub_vEdge_VPN_VPN0

+ BGP

BGP: Hub_vEdge1_BGP_VPN0

==============================================

+ VPN Interface

VPN Interface : Hub_vEdge_Interface_GE0/0
VPN Interface : Hub_vEdge_Interface_GE0/1
VPN Interface : Hub_vEdge_Interface_GE0/2
VPN Interface : Hub_vEdge_Interface_loopback1
VPN Interface : Hub_vEdge_Interface_loopback2

==============================================

VPN 512: VPN512

+ VPN Interface

VPN Interface : ETH0

---------Service VPN---------
+ Add VPN

Selected VPN Templates : Hub_vEdge_VPN_VPN10

+ BGP

BGP: Hub_vEdge1_BGP_VPN10

==============================================

+ VPN Interface

VPN Interface : Hub_vEdge_Interface_GE0/3