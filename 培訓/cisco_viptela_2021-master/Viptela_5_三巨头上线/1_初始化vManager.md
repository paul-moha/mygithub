### 初始化硬盘
```shell
viptela 20.3.3.1 

vmanage login: admin
Password: admin
Welcome to Viptela CLI
admin connected from 127.0.0.1 using console on vmanage
You must set an initial admin password.
Password: admin
Re-enter password: admin
Available storage devices:
sdb     200GB
1) sdb
Select storage device to use: 1
Would you like to format sdb? (y/n): y
```

### vManager1配置脚本
```shell
config t

system
 host-name             vManage1
 system-ip             1.1.1.1
 site-id               100
 sp-organization-name  testrabbit
 organization-name     testrabbit
 vbond vbond.testrabbit.local
!
vpn 0
 dns 202.100.100.200 primary
 interface eth0
  ip address 202.100.100.11/24
  tunnel-interface
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.100.254
!
commit

```

### vManager2配置脚本
```shell
config t

system
 host-name             vManage2
 system-ip             1.1.1.2
 site-id               100
 sp-organization-name  testrabbit
 organization-name     testrabbit
 vbond vbond.testrabbit.local
!
vpn 0
 dns 202.100.100.200 primary
 interface eth0
  ip address 202.100.100.12/24
  tunnel-interface
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.100.254
!
commit

```

### vManager3配置脚本
```shell
config t

system
 host-name             vManage3
 system-ip             1.1.1.3
 site-id               100
 sp-organization-name  testrabbit
 organization-name     testrabbit
 vbond vbond.testrabbit.local
!
vpn 0
 dns 202.100.100.200 primary
 interface eth0
  ip address 202.100.100.13/24
  tunnel-interface
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.100.254
!
commit

```