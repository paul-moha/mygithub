Configuration --- Templates --- Device

模板类型:Device
+ Create Template --- From Feature Template

=========================================================
Device Model: vEdge Cloud
Template Name : Branch1_vEdge2
Description : Branch1_vEdge2

---------Basic Information---------
OMP : Branch1_vEdge_OMP

---------Transport & Management VPN---------
VPN0: Branch1_vEdge_VPN_VPN0_Internet_mpls

+ BGP

BGP: Branch1_vEdge2_BGP_VPN0

==============================================

+ VPN Interface

VPN Interface : Branch1_vEdge_Interface_Internet
VPN Interface : Branch1_vEdge_Interface_mpls
VPN Interface : Branch1_vEdge_Internface_TLOC


==============================================

VPN 512: VPN512

+ VPN Interface

VPN Interface : ETH0

---------Service VPN---------
+ Add VPN

Selected VPN Templates : Branch1_vEdge2_VPN_VPN10

+ VPN Interface

VPN Interface : Branch1_vEdge_Interface_VRRP