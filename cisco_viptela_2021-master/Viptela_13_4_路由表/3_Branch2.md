Branch2_cEdge#show ip route vrf 10
```shell
Routing Table: 10
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 0.0.0.0 to network 0.0.0.0

n*Nd  0.0.0.0/0 [6/0], 23:40:23, Null0
      10.0.0.0/8 is variably subnetted, 8 subnets, 2 masks
m        10.1.1.0/24 [251/0] via 10.10.10.12, 00:41:16, Sdwan-system-intf
                     [251/0] via 10.10.10.11, 00:41:16, Sdwan-system-intf
B        10.1.2.0/24 [20/0] via 10.1.20.254, 23:39:34
m        10.1.3.0/24 [251/0] via 10.10.10.30, 23:39:31, Sdwan-system-intf
m        10.1.4.0/24 [251/0] via 10.10.10.42, 00:41:16, Sdwan-system-intf
                     [251/0] via 10.10.10.41, 00:41:16, Sdwan-system-intf
m        10.1.5.0/24 [251/0] via 10.10.10.50, 23:39:31, Sdwan-system-intf
m        10.1.6.0/24 [251/0] via 10.10.10.42, 00:41:16, Sdwan-system-intf
                     [251/0] via 10.10.10.41, 00:41:16, Sdwan-system-intf
C        10.1.20.0/24 is directly connected, GigabitEthernet3
L        10.1.20.1/32 is directly connected, GigabitEthernet3
m     192.168.0.0/24 [251/0] via 10.10.10.11, 23:39:11, Sdwan-system-intf
m     192.168.1.0/24 [251/0] via 10.10.10.11, 23:39:11, Sdwan-system-intf
```

Branch2_SW#show ip route
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

Gateway of last resort is 10.1.20.1 to network 0.0.0.0

B*    0.0.0.0/0 [20/0] via 10.1.20.1, 00:42:20
      10.0.0.0/8 is variably subnetted, 11 subnets, 2 masks
B        10.1.1.0/24 [20/1000] via 10.1.20.1, 00:42:20
C        10.1.2.0/24 is directly connected, GigabitEthernet0/0
L        10.1.2.254/32 is directly connected, GigabitEthernet0/0
B        10.1.3.0/24 [20/1000] via 10.1.20.1, 00:42:20
B        10.1.4.0/24 [20/1000] via 10.1.20.1, 00:42:20
B        10.1.5.0/24 [20/1000] via 10.1.20.1, 00:42:20
B        10.1.6.0/24 [20/0] via 10.1.20.2, 1w3d
C        10.1.20.0/24 is directly connected, Vlan20
L        10.1.20.254/32 is directly connected, Vlan20
B        10.1.241.0/24 [20/0] via 10.1.20.2, 23:48:22
B        10.1.242.0/24 [20/0] via 10.1.20.2, 23:48:22
      172.16.0.0/24 is subnetted, 6 subnets
B        172.16.10.0 [20/0] via 10.1.20.2, 2w2d
B        172.16.11.0 [20/0] via 10.1.20.2, 23:42:22
B        172.16.20.0 [20/0] via 10.1.20.2, 2w2d
B        172.16.60.0 [20/0] via 10.1.20.2, 2w2d
B        172.16.141.0 [20/0] via 10.1.20.2, 2w2d
B        172.16.142.0 [20/0] via 10.1.20.2, 2w2d
B     192.168.0.0/24 [20/1000] via 10.1.20.1, 00:42:20
B     192.168.1.0/24 [20/1000] via 10.1.20.1, 00:42:20
```