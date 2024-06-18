-------------控制总结---------------

=============入方向============

1. Branch2 BGP 2 入方向控制 --- 非本地Prefix，都会在Branch2_SW上打上88:88。确保本地Prefix进入！
   通过communirty 88:88  
   action : reject 

=============出方向=============

1.  Branch2 BGP 2 出方向 控制  --- 来自于SDWAN OMP重分布进入BGP的路由，不要出Branch2_SW的AS 20
    通过community: no-export





