Hub_vEdge1# show ip route
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
0      0.0.0.0/0           static           -         ge0/0       202.100.41.254   -        -                -                -      F,S     
0      10.1.1.0/24         bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      10.1.2.0/24         bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      10.1.4.0/24         bgp              i         ge0/2       172.16.41.1      -        -                -                -      F,S     
0      10.1.6.0/24         bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      10.1.20.0/24        bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      10.1.141.0/24       connected        -         loopback1   -                -        -                -                -      F,S     
0      10.1.241.0/24       connected        -         loopback2   -                -        -                -                -      F,S     
0      10.10.10.41/32      connected        -         system      -                -        -                -                -      F,S     
0      172.16.10.0/24      bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      172.16.11.0/24      bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      172.16.20.0/24      bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      172.16.41.0/24      connected        -         ge0/2       -                -        -                -                -      F,S     
0      172.16.60.0/24      bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      172.16.141.0/24     bgp              i         -           172.16.141.254   -        -                -                -      I       
0      172.16.141.0/24     connected        -         ge0/1       -                -        -                -                -      F,S     
0      172.16.142.0/24     bgp              i         ge0/1       172.16.141.254   -        -                -                -      F,S     
0      202.100.41.0/24     connected        -         ge0/0       -                -        -                -                -      F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.11      mpls             ipsec  F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.11      public-internet  ipsec  F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.12      mpls             ipsec  F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.12      public-internet  ipsec  F,S     
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      mpls             ipsec  F,S     
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      public-internet  ipsec  F,S     
10     10.1.3.0/24         omp              -         -           -                -        10.10.10.30      public-internet  ipsec  F,S     
10     10.1.4.0/24         bgp              i         ge0/3       10.1.41.1        -        -                -                -      F,S     
10     10.1.5.0/24         omp              -         -           -                -        10.10.10.50      public-internet  ipsec  F,S     
10     10.1.6.0/24         bgp              i         ge0/3       10.1.41.1        -        -                -                -      F,S     
10     10.1.41.0/24        connected        -         ge0/3       -                -        -                -                -      F,S     
10     192.168.0.0/24      omp              -         -           -                -        10.10.10.11      mpls             ipsec  F,S     
10     192.168.0.0/24      omp              -         -           -                -        10.10.10.11      public-internet  ipsec  F,S     
10     192.168.1.0/24      omp              -         -           -                -        10.10.10.11      mpls             ipsec  F,S     
10     192.168.1.0/24      omp              -         -           -                -        10.10.10.11      public-internet  ipsec  F,S   
```

Hub_vEdge2# show ip route
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
0      0.0.0.0/0           static           -         ge0/0       202.100.42.254   -        -                -                -      F,S     
0      10.1.1.0/24         bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      10.1.2.0/24         bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      10.1.4.0/24         bgp              i         ge0/2       172.16.42.1      -        -                -                -      F,S     
0      10.1.6.0/24         bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      10.1.20.0/24        bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      10.1.142.0/24       connected        -         loopback1   -                -        -                -                -      F,S     
0      10.1.242.0/24       connected        -         loopback2   -                -        -                -                -      F,S     
0      10.10.10.42/32      connected        -         system      -                -        -                -                -      F,S     
0      172.16.10.0/24      bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      172.16.11.0/24      bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      172.16.20.0/24      bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      172.16.42.0/24      connected        -         ge0/2       -                -        -                -                -      F,S     
0      172.16.60.0/24      bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      172.16.141.0/24     bgp              i         ge0/1       172.16.142.254   -        -                -                -      F,S     
0      172.16.142.0/24     bgp              i         -           172.16.142.254   -        -                -                -      I       
0      172.16.142.0/24     connected        -         ge0/1       -                -        -                -                -      F,S     
0      202.100.42.0/24     connected        -         ge0/0       -                -        -                -                -      F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.11      mpls             ipsec  F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.11      public-internet  ipsec  F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.12      mpls             ipsec  F,S     
10     10.1.1.0/24         omp              -         -           -                -        10.10.10.12      public-internet  ipsec  F,S     
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      mpls             ipsec  F,S     
10     10.1.2.0/24         omp              -         -           -                -        10.10.10.20      public-internet  ipsec  F,S     
10     10.1.3.0/24         omp              -         -           -                -        10.10.10.30      public-internet  ipsec  F,S     
10     10.1.4.0/24         bgp              i         ge0/3       10.1.42.1        -        -                -                -      F,S     
10     10.1.5.0/24         omp              -         -           -                -        10.10.10.50      public-internet  ipsec  F,S     
10     10.1.6.0/24         bgp              i         ge0/3       10.1.42.1        -        -                -                -      F,S     
10     10.1.42.0/24        connected        -         ge0/3       -                -        -                -                -      F,S     
10     192.168.0.0/24      omp              -         -           -                -        10.10.10.11      mpls             ipsec  F,S     
10     192.168.0.0/24      omp              -         -           -                -        10.10.10.11      public-internet  ipsec  F,S     
10     192.168.1.0/24      omp              -         -           -                -        10.10.10.11      mpls             ipsec  F,S     
10     192.168.1.0/24      omp              -         -           -                -        10.10.10.11      public-internet  ipsec  F,S
```

Hub_SW#show ip route
```shell
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 14 subnets, 2 masks
B        10.1.1.0/24 [20/50] via 10.1.41.254, 00:11:56
B        10.1.2.0/24 [20/50] via 10.1.41.254, 00:11:56
B        10.1.3.0/24 [20/50] via 10.1.41.254, 00:17:56
C        10.1.4.0/24 is directly connected, GigabitEthernet1/0
L        10.1.4.254/32 is directly connected, GigabitEthernet1/0
B        10.1.5.0/24 [20/50] via 10.1.41.254, 00:17:56
B        10.1.6.0/24 [20/50] via 172.16.41.254, 00:12:20
B        10.1.20.0/24 [20/50] via 172.16.41.254, 00:12:20
C        10.1.41.0/24 is directly connected, GigabitEthernet0/2
L        10.1.41.1/32 is directly connected, GigabitEthernet0/2
C        10.1.42.0/24 is directly connected, GigabitEthernet0/3
L        10.1.42.1/32 is directly connected, GigabitEthernet0/3
B        10.1.241.0/24 [20/50] via 172.16.41.254, 00:21:36
B        10.1.242.0/24 [20/100] via 172.16.42.254, 00:12:20
      172.16.0.0/16 is variably subnetted, 10 subnets, 2 masks
B        172.16.10.0/24 [20/50] via 172.16.41.254, 00:12:20
B        172.16.11.0/24 [20/50] via 172.16.41.254, 00:12:20
B        172.16.20.0/24 [20/50] via 172.16.41.254, 00:12:20
C        172.16.41.0/24 is directly connected, GigabitEthernet0/0
L        172.16.41.1/32 is directly connected, GigabitEthernet0/0
C        172.16.42.0/24 is directly connected, GigabitEthernet0/1
L        172.16.42.1/32 is directly connected, GigabitEthernet0/1
B        172.16.60.0/24 [20/50] via 172.16.41.254, 00:12:20
B        172.16.141.0/24 [20/50] via 172.16.41.254, 00:12:20
B        172.16.142.0/24 [20/50] via 172.16.41.254, 00:12:20
B     192.168.0.0/24 [20/50] via 10.1.41.254, 00:17:56
B     192.168.1.0/24 [20/50] via 10.1.41.254, 00:17:56
```

Hub_SW# show ip bgp
```shell
BGP table version is 310, local router ID is 172.16.42.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
              x best-external, a additional-path, c RIB-compressed, 
              t secondary path, 
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *    10.1.1.0/24      10.1.42.254            100             0 40 ?
 *>                    10.1.41.254             50             0 40 ?
 *                     172.16.42.254          100             0 140 254 11 ?
 *                     172.16.41.254           50             0 140 254 11 ?
 *    10.1.2.0/24      10.1.42.254            100             0 40 20 ?
 *>                    10.1.41.254             50             0 40 20 ?
 *                     172.16.42.254          100             0 140 254 22 20 i
 *                     172.16.41.254           50             0 140 254 22 20 i
 *    10.1.3.0/24      10.1.42.254            100             0 40 ?
 *>                    10.1.41.254             50             0 40 ?
 *>   10.1.4.0/24      0.0.0.0                  0         32768 i
 *    10.1.5.0/24      10.1.42.254            100             0 40 ?
 *>                    10.1.41.254             50             0 40 ?
     Network          Next Hop            Metric LocPrf Weight Path
 *    10.1.6.0/24      172.16.42.254          100             0 140 254 60 i
 *>                    172.16.41.254           50             0 140 254 60 i
 *    10.1.20.0/24     172.16.42.254          100             0 140 254 22 i
 *>                    172.16.41.254           50             0 140 254 22 i
 *>   10.1.241.0/24    172.16.41.254           50             0 140 i
 *>   10.1.242.0/24    172.16.42.254          100             0 140 i
 *    172.16.10.0/24   172.16.42.254          100             0 140 254 i
 *>                    172.16.41.254           50             0 140 254 i
 *    172.16.11.0/24   172.16.42.254          100             0 140 254 11 i
 *>                    172.16.41.254           50             0 140 254 11 i
 *    172.16.20.0/24   172.16.42.254          100             0 140 254 i
 *>                    172.16.41.254           50             0 140 254 i
 *    172.16.60.0/24   172.16.42.254          100             0 140 254 i
 *>                    172.16.41.254           50             0 140 254 i
 *    172.16.141.0/24  172.16.42.254          100             0 140 254 i
 *>                    172.16.41.254           50             0 140 254 i
 *    172.16.142.0/24  172.16.42.254          100             0 140 254 i
 *>                    172.16.41.254           50             0 140 254 i
 *    192.168.0.0      10.1.42.254            100             0 40 ?
 *>                    10.1.41.254             50             0 40 ?
 *    192.168.1.0      10.1.42.254            100             0 40
```