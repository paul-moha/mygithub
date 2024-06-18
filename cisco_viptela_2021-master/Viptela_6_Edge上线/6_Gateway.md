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
 host-name               Gateway
 system-ip               10.10.10.50
 site-id                 50
 sp-organization-name    testrabbit
 organization-name       testrabbit
 vbond vbond.testrabbit.local
  !
vpn 0
 dns 202.100.100.200 primary
 interface ge0/0
  ip address 202.100.50.1/24
  tunnel-interface
   encapsulation ipsec
   color public-internet restrict
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.50.254
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
829344d4-60b4-b862-34a8-54d920d27295

### 激活Edge
```shell
request vedge-cloud activate chassis-number <uuid> token <opt>

```

### request 举例
```shell
uuid : d52798c2-e6e5-e168-a7c5-590dc6e93d50
opt  : 80ba1f8dc4a445ef9caa025760a6a221
 
request vedge-cloud activate chassis-number 074c7092-4121-e1dd-8049-59ceb8caecf8 token 6a673a7ca16b4568b8e4c9de0bc070a2

```
