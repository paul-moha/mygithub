Branch1_vEdge1# show ip route
```shell
Codes Proto-sub-type:
  IA -> ospf-intra-area, IE -> ospf-inter-area,
  E1 -> ospf-external1, E2 -> ospf-external2,
  N1 -> ospf-nssa-external1, N2 -> ospf-nssa-external2,
  e -> bgp-external, i -> bgp-internal
Codes Status flags:
  F -> fib, S -> selected, I -> inactive,
  B -> blackhole, R -> recursive, L -> import

                                            PROTOCOL  NEXTHOP     NEXTHOP          NEXTHOP                                                   
VPN    PREFIX              PROTOCOL         SUB TYPE  IF NAME     ADDR             VPN      TLOC IP          COLOR            ENCAP  STATUS  
---------------------------------------------------------------------------------------------------------------------------------------------
0      0.0.0.0/0           static           -         ge0/3       10.1.10.254      -        -                -                -      F,S     
0      0.0.0.0/0           static           -         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      10.1.1.0/24         static           -         -           -                10       -                -                -      F,S,L   
0      10.1.2.0/24         bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      10.1.4.0/24         bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      10.1.6.0/24         bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      10.1.10.0/24        connected        -         ge0/3       -                -        -                -                -      F,S     
0      10.1.20.0/24        bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      10.1.241.0/24       bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      10.1.242.0/24       bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      10.10.10.11/32      connected        -         system      -                -        -                -                -      F,S     
0      172.16.10.0/24      bgp              i         -           172.16.10.254    -        -                -                -      I       
0      172.16.10.0/24      connected        -         ge0/0       -                -        -                -                -      F,S     
0      172.16.11.0/24      connected        -         ge0/2       -                -        -                -                -      F,S     
0      172.16.20.0/24      bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      172.16.60.0/24      bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      172.16.141.0/24     bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      172.16.142.0/24     bgp              i         ge0/0       172.16.10.254    -        -                -                -      F,S     
0      192.168.0.0/24      static           -         -           -                10       -                -                -      F,S,L   
0      192.168.1.0/24      static           -         -           -                10       -                -                -      F,S,L   
10     10.1.1.0/24         connected        -         ge0/1       -                -        -                -                -      F,S     
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      mpls             ipsec  -       
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      public-internet  ipsec  -       
10     10.1.2.0/24         static           -         -           -                0        -                -                -      F,S,L   
10     10.1.3.0/24         omp              -         -           -                -        10.10.10.30      public-internet  ipsec  F,S     
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.41      mpls             ipsec  -       
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.41      public-internet  ipsec  -       
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.42      mpls             ipsec  -       
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.42      public-internet  ipsec  -       
10     10.1.4.0/24         static           -         -           -                0        -                -                -      F,S,L   
10     10.1.5.0/24         omp              -         -           -                -        10.10.10.50      public-internet  ipsec  F,S     
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.41      mpls             ipsec  -       
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.41      public-internet  ipsec  -       
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.42      mpls             ipsec  -       
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.42      public-internet  ipsec  -       
10     10.1.6.0/24         static           -         -           -                0        -                -                -      F,S,L   
10     10.1.20.0/24        static           -         -           -                0        -                -                -      F,S,L   
10     10.1.241.0/24       static           -         -           -                0        -                -                -      F,S,L   
10     10.1.242.0/24       static           -         -           -                0        -                -                -      F,S,L   
10     172.16.20.0/24      static           -         -           -                0        -                -                -      F,S,L   
10     172.16.60.0/24      static           -         -           -                0        -                -                -      F,S,L   
10     172.16.141.0/24     static           -         -           -                0        -                -                -      F,S,L   
10     172.16.142.0/24     static           -         -           -                0        -                -                -      F,S,L   
10     192.168.0.0/24      connected        -         ge0/4       -                -        -                -                -      F,S     
10     192.168.1.0/24      connected        -         ge0/5       -                -        -                -                -      F,S  
```

Branch1_vEdge2# show ip route
```shell
 Codes Proto-sub-type:
  IA -> ospf-intra-area, IE -> ospf-inter-area,
  E1 -> ospf-external1, E2 -> ospf-external2,
  N1 -> ospf-nssa-external1, N2 -> ospf-nssa-external2,
  e -> bgp-external, i -> bgp-internal
Codes Status flags:
  F -> fib, S -> selected, I -> inactive,
  B -> blackhole, R -> recursive, L -> import

                                            PROTOCOL  NEXTHOP     NEXTHOP          NEXTHOP                                                   
VPN    PREFIX              PROTOCOL         SUB TYPE  IF NAME     ADDR             VPN      TLOC IP          COLOR            ENCAP  STATUS  
---------------------------------------------------------------------------------------------------------------------------------------------
0      0.0.0.0/0           static           -         ge0/0       202.100.10.254   -        -                -                -      F,S     
0      0.0.0.0/0           static           -         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.1.1.0/24         static           -         -           -                10       -                -                -      L       
0      10.1.1.0/24         bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.1.2.0/24         bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.1.4.0/24         bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.1.6.0/24         bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.1.10.0/24        connected        -         ge0/3       -                -        -                -                -      F,S     
0      10.1.20.0/24        bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.1.241.0/24       bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.1.242.0/24       bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      10.10.10.12/32      connected        -         system      -                -        -                -                -      F,S     
0      172.16.10.0/24      bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      172.16.11.0/24      bgp              i         -           172.16.11.254    -        -                -                -      I       
0      172.16.11.0/24      connected        -         ge0/2       -                -        -                -                -      F,S     
0      172.16.20.0/24      bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      172.16.60.0/24      bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      172.16.141.0/24     bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      172.16.142.0/24     bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      192.168.0.0/24      bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      192.168.1.0/24      bgp              i         ge0/2       172.16.11.254    -        -                -                -      F,S     
0      202.100.10.0/24     connected        -         ge0/0       -                -        -                -                -      F,S     
10     10.1.1.0/24         connected        -         ge0/1       -                -        -                -                -      F,S     
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      mpls             ipsec  -       
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      public-internet  ipsec  -       
10     10.1.2.0/24         static           -         -           -                0        -                -                -      F,S,L   
10     10.1.3.0/24         omp              -         -           -                -        10.10.10.30      public-internet  ipsec  F,S     
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.41      mpls             ipsec  -       
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.41      public-internet  ipsec  -       
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.42      mpls             ipsec  -       
10     10.1.4.0/24         omp              -         -           -                -        10.10.10.42      public-internet  ipsec  -       
10     10.1.4.0/24         static           -         -           -                0        -                -                -      F,S,L   
10     10.1.5.0/24         omp              -         -           -                -        10.10.10.50      public-internet  ipsec  F,S     
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.41      mpls             ipsec  -       
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.41      public-internet  ipsec  -       
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.42      mpls             ipsec  -       
10     10.1.6.0/24         omp              -         -           -                -        10.10.10.42      public-internet  ipsec  -       
10     10.1.6.0/24         static           -         -           -                0        -                -                -      F,S,L   
10     10.1.20.0/24        static           -         -           -                0        -                -                -      F,S,L   
10     10.1.241.0/24       static           -         -           -                0        -                -                -      F,S,L   
10     10.1.242.0/24       static           -         -           -                0        -                -                -      F,S,L   
10     172.16.10.0/24      static           -         -           -                0        -                -                -      F,S,L   
10     172.16.20.0/24      static           -         -           -                0        -                -                -      F,S,L   
10     172.16.60.0/24      static           -         -           -                0        -                -                -      F,S,L   
10     172.16.141.0/24     static           -         -           -                0        -                -                -      F,S,L   
10     172.16.142.0/24     static           -         -           -                0        -                -                -      F,S,L   
10     192.168.0.0/24      static           -         -           -                0        -                -                -      F,S,L   
10     192.168.1.0/24      static           -         -           -                0        -                -                -      F,S,L 
```