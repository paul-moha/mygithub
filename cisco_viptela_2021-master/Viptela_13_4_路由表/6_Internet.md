vyos@IPS-PE:~$ show ip route
```shell
Codes: K - kernel route, C - connected, S - static, R - RIP, O - OSPF,
       I - ISIS, B - BGP, > - selected route, * - FIB route

B>* 0.0.0.0/0 [20/0] via 172.16.141.1, eth3, 23:14:36
B>* 10.1.1.0/24 [20/0] via 172.16.10.1, eth1, 03:01:02
B>* 10.1.2.0/24 [20/0] via 172.16.20.1, eth2, 01w0d05h
B>* 10.1.4.0/24 [20/0] via 172.16.141.1, eth3, 23:15:06
B>* 10.1.6.0/24 [20/0] via 172.16.60.1, eth0, 01w1d00h
B>* 10.1.20.0/24 [20/1] via 172.16.20.1, eth2, 5d00h12m
B>* 10.1.241.0/24 [20/0] via 172.16.141.1, eth3, 23:14:36
B>* 10.1.242.0/24 [20/0] via 172.16.142.1, eth4, 22:41:52
C>* 127.0.0.0/8 is directly connected, lo
C>* 172.16.10.0/24 is directly connected, eth1
B>* 172.16.11.0/24 [20/0] via 172.16.10.1, eth1, 07:10:33
C>* 172.16.20.0/24 is directly connected, eth2
C>* 172.16.60.0/24 is directly connected, eth0
C>* 172.16.141.0/24 is directly connected, eth3
C>* 172.16.142.0/24 is directly connected, eth4
```