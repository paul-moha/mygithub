### 初始化密码
```shell
viptela 20.3.3 

vedge login: admin
Password: 
Welcome to Viptela CLI
admin connected from 127.0.0.1 using console on vedge
You must set an initial admin password.
Password: 
Re-enter password: 
vedge# 
```

### 初始化配置
```shell
config ter

system
 host-name               Hub_vEdge1
 system-ip               10.10.10.41
 site-id                 40
 sp-organization-name    testrabbit
 organization-name       testrabbit
 vbond vbond.testrabbit.local
  !
vpn 0
 dns 202.100.100.200 primary
 interface ge0/0
  ip address 202.100.41.1/24
  tunnel-interface
   encapsulation ipsec
   color public-internet restrict
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.41.254
!
commit

end

```

### 下载根证书
```shell
vshell
curl -u anonymous:1@2.net 'ftp://202.100.100.200/root.cer' -o ./root.cer

exit

```

### 卸载设备原始的根证书
```shell
request root-cert-chain uninstall 

```

### 加载根证书
```shell
request root-cert-chain install /home/admin/root.cer

```

### 查看根证书
```shell
show certificate root-ca-cert  

```

### 复制uuid / otp
Configuration --- Devices --- WAN Edge List --- 选择一个vEdge Cloud -- Generate Bootstrap Configuration --- Cloud-init --- 找一个vEdge (复制 uuid / otp)

### 推荐选择 Classis Number
c1fe3318-df8d-75c0-e102-f39bd76b121d

### 激活Edge
```shell
request vedge-cloud activate chassis-number <uuid> token <opt>

```

### request 举例
```shell
uuid : c1fe3318-df8d-75c0-e102-f39bd76b121d
opt  : 086a23ee1d5f4648a28505b93dfba419
 
request vedge-cloud activate chassis-number c1fe3318-df8d-75c0-e102-f39bd76b121d token 086a23ee1d5f4648a28505b93dfba419

```
