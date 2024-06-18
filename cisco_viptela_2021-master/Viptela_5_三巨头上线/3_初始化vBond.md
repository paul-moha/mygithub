### 初始化密码
```shell
viptela 20.3.3 

vedge login: admin
Password: admin
Welcome to Viptela CLI
admin connected from 127.0.0.1 using console on vedge
You must set an initial admin password.
Password: admin
Re-enter password: admin
vedge# 
```

### vBond1配置脚本
```shell
config t

system
 host-name               vBond1
 system-ip               3.3.3.1
 site-id                 100
 sp-organization-name    testrabbit
 organization-name       testrabbit
 vbond vbond.testrabbit.local local
  !
vpn 0
 dns 202.100.100.200 primary
 interface ge0/0
  ip address 202.100.100.30/24
  tunnel-interface
   encapsulation ipsec
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.100.254
!
commit

```

### vBond2配置脚本
```shell
config t

system
 host-name               vBond2
 system-ip               3.3.3.2
 site-id                 200
 sp-organization-name    testrabbit
 organization-name       testrabbit
 vbond vbond.testrabbit.local local
  !
vpn 0
 dns 202.100.100.200 primary
 interface ge0/0
  ip address 202.100.101.30/24
  tunnel-interface
   encapsulation ipsec
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.101.254
!
commit

```