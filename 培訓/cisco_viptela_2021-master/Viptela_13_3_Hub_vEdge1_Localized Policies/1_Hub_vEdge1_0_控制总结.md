-------------控制总结---------------

=============BGP 140 到 BGP 4 出方向=============

1.  Hub_vEdge1 BGP 140 到 BGP 4 方向控制 [设置Metric 50(确保优选), 保留66:66(最终会进入OMP), 其他设置no-export]
    sequence1: 
     match community 66:66
     set metric: 50
    
    sequcence2:
     set community: no-export 
     metric: 50


=============BGP 40 到 BGP 4 出方向============

1.  Hub_vEdge1 BGP 40 到 BGP 4 方向控制 [设置Metric 50(确保优选), 保留33:33(最终进入MPLS), 其他设置no-export]
    sequence1: 
     match community 33:33
     set metric: 50
    
    sequcence2:
     set community: no-export 
     metric: 50

2.  Hub_vEdge1 OMP 重分布到 BGP 40 [重分布OMP(SDWAN网络)进入BGP, 把OMP Tag 33换为Community 33:33]
    sequence1: 
     match OMP Tag 33
     set community: 33:33


