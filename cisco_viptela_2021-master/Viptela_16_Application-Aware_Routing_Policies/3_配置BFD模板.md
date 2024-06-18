### 创建Feature模板
Configuration --- Templates --- Feature

模板类型:Feature
设备类型:vEdge_Cloud
模板类型: BASIC INFORMATION --- BFD
名称: vEdge_BFD

----------------COLOR----------------
+ New Color

Color               Hello Interval (milliseconds)           Multiplier          Path MTU Discovery
  
MPLS                1000(默认)                               7(默认)             On(默认)
Public Internet     500(修改)                                7(默认)             On(默认)


### Device调用模板
Configuration --- Templates --- Device

修改如下Device模板:
Branch1_vEdge1
Branch1_vEdge2
Hub_vEdge1
Hub_vEdge2

------------------Basic Information------------------
BFD : vEdge_BFD
