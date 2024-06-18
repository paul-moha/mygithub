### 初始化密码
```shell
viptela 20.3.3 

vsmart login: admin
Password: admin
Welcome to Viptela CLI
admin connected from 127.0.0.1 using console on vsmart
You must set an initial admin password.
Password: admin
Re-enter password: admin
vsmart# 
```

### vSmart1配置脚本
```shell
config t

system
 host-name             vSmart1
 system-ip             2.2.2.1
 site-id               100
 sp-organization-name  testrabbit
 organization-name     testrabbit
 vbond vbond.testrabbit.local
  !
vpn 0
 dns 202.100.100.200 primary
 interface eth0
  ip address 202.100.100.20/24
  tunnel-interface
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.100.254
!
commit

```

### vSmart2配置脚本
```shell
config t

system
 host-name             vSmart2
 system-ip             2.2.2.2
 site-id               200
 sp-organization-name  testrabbit
 organization-name     testrabbit
 vbond vbond.testrabbit.local
  !
vpn 0
 dns 202.100.100.200 primary
 interface eth0
  ip address 202.100.101.20/24
  tunnel-interface
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.101.254
!
commit

```