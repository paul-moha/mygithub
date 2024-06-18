Branch2_cEdge#sh run | sec route-map
```shell
  neighbor 10.1.20.254 route-map Community88 in
  neighbor 10.1.20.254 route-map No_Export out
route-map Community88 deny 1 
 match community Community88
route-map Community88 permit 65535 
route-map No_Export permit 1 
 set community no-export
route-map No_Export deny 65535 
```

Branch2_cEdge#sh run | sec router
```shell
router omp
router bgp 2
 bgp log-neighbor-changes
 distance bgp 20 200 20
 !
 address-family ipv4 vrf 10
  network 0.0.0.0
  redistribute omp
  propagate-aspath
  neighbor 10.1.20.254 remote-as 20
  neighbor 10.1.20.254 ebgp-multihop 255
  neighbor 10.1.20.254 activate
  neighbor 10.1.20.254 send-community both
  neighbor 10.1.20.254 route-map Community88 in
  neighbor 10.1.20.254 route-map No_Export out
  neighbor 10.1.20.254 maximum-prefix 2147483647 100
 exit-address-family
```

Branch2_cEdge#show ip bgp vpnv4 vrf 10 summary 
```shell
BGP router identifier 202.100.20.1, local AS number 2
BGP table version is 40, main routing table version 40
15 network entries using 3840 bytes of memory
15 path entries using 2040 bytes of memory
16/8 BGP path/bestpath attribute entries using 4864 bytes of memory
13 BGP AS-PATH entries using 488 bytes of memory
1 BGP community entries using 24 bytes of memory
2 BGP extended community entries using 64 bytes of memory
8 BGP route-map cache entries using 576 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 11896 total bytes of memory
BGP activity 16/1 prefixes, 28/13 paths, scan interval 60 secs
16 networks peaked at 11:20:02 Nov 17 2021 UTC (00:02:19.962 ago)

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
10.1.20.254     4           20     589     589       40    0    0 08:34:57        1
```