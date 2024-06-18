### 初始化密码(Branch1_vEdge1和Branch1_vEdge2)
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

### 注意 Branch1_vEdge1的VPN0默认有GE0/0配置, 初始化时删除[GE0/0]

### 初始化配置(Branch1_vEdge1)
```shell
config ter

system
 host-name               Branch1_vEdge1
 system-ip               10.10.10.11
 site-id                 10
 sp-organization-name    testrabbit
 organization-name       testrabbit
 vbond vbond.testrabbit.local
  !
vpn 0
 dns 202.100.100.200 primary
 interface ge0/3
  ip address 10.1.10.1/24
  tunnel-interface
   encapsulation ipsec
   color public-internet restrict
   allow-service all
  !
  no shutdown
 !
 ip route 0.0.0.0/0 10.1.10.254
!
commit

end

```

### 初始化配置(Branch1_vEdge2)
```shell
config ter

system
 host-name               Branch1_vEdge2
 system-ip               10.10.10.12
 site-id                 10
 sp-organization-name    testrabbit
 organization-name       testrabbit
 vbond vbond.testrabbit.local
  !
vpn 0
 dns 202.100.100.200 primary
 interface ge0/0
  ip address 202.100.10.1/24
  nat
  !
  tunnel-interface
   encapsulation ipsec
   color public-internet restrict
   allow-service all
  !
  no shutdown
 !
 interface ge0/3
  ip address 10.1.10.254/24
  tloc-extension ge0/0
  no shutdown
 !
 ip route 0.0.0.0/0 202.100.10.254
!
commit

end

```

### 下载根证书(Branch1_vEdge2)
```shell
vshell
curl -u anonymous:1@2.net 'ftp://202.100.100.200/root.cer' -o ./root.cer

exit

```

### 卸载设备原始的根证书(Branch1_vEdge2)
```shell
request root-cert-chain uninstall 

```

### 加载根证书(Branch1_vEdge2)
```shell
request root-cert-chain install /home/admin/root.cer

```

### 查看根证书(Branch1_vEdge2)
```shell
show certificate root-ca-cert  

```

### 复制uuid / otp (Branch1_vEdge2)
Configuration --- Devices --- WAN Edge List --- 选择一个vEdge Cloud -- Generate Bootstrap Configuration --- Cloud-init --- 找一个vEdge (复制 uuid / otp)

### 推荐选择 Chassis Number
111b0562-313a-b7e1-9b64-8cb3fa511031

### 激活Edge (Branch1_vEdge2)
```shell
request vedge-cloud activate chassis-number <uuid> token <opt>

```

### request 举例(Branch1_vEdge2)
```shell
uuid : d52798c2-e6e5-e168-a7c5-590dc6e93d50
opt  : 80ba1f8dc4a445ef9caa025760a6a221
 
request vedge-cloud activate chassis-number d52798c2-e6e5-e168-a7c5-590dc6e93d50 token 80ba1f8dc4a445ef9caa025760a6a221

```

### 注意:一定要确认Branch1_vEdge2先上线,数据层面才能转发

### 下载根证书(Branch1_vEdge1)
```shell
vshell
curl -u anonymous:1@2.net 'ftp://202.100.100.200/root.cer' -o ./root.cer

exit

```

### 卸载设备原始的根证书(Branch1_vEdge1)
```shell
request root-cert-chain uninstall 

```

### 加载根证书(Branch1_vEdge1)
```shell
request root-cert-chain install /home/admin/root.cer

```

### 查看根证书(Branch1_vEdge1)
```shell
show certificate root-ca-cert  

```

### 复制uuid / otp (Branch1_vEdge1)
Configuration --- Devices --- WAN Edge List --- 选择一个vEdge Cloud -- Generate Bootstrap Configuration --- Cloud-init --- 找一个vEdge (复制 uuid / otp)

### 推荐选择 Classis Number
01b2c99a-7215-5408-b45d-25fa5d8b8584

### 激活Edge (Branch1_vEdge1)
```shell
request vedge-cloud activate chassis-number <uuid> token <opt>

```

### request 举例(Branch1_vEdge1)
```shell
uuid : d52798c2-e6e5-e168-a7c5-590dc6e93d50
opt  : 80ba1f8dc4a445ef9caa025760a6a221
 
request vedge-cloud activate chassis-number e1ed748d-a7d4-633d-9691-ee8476bc693b token 03fa844560d9434ea51326b31cbc9b58

```