### 初始化密码
```shell
User Access Verification

Username: admin
Password: 

Default admin password needs to be changed.


Enter new password: 
Confirm password: 
Router#
```

### 查看模式(本次实验快照已经提前切换到了Controller-Managed模式)
Router#show version | in opera
Router operating mode: Controller-Managed

默认为:Router operating mode: Autonomous

### 如何切换到Controller-mode
Router#controller-mode enable
Enabling controller mode will erase the nvram filesystem, remove all configuration files, and reload the box! 
Ensure the BOOT variable points to a valid image 
Continue? [confirm]
% Warning: Bootstrap config file needed for Day-0 boot is missing
Do you want to abort? (yes/[no]): no
 Mode change success
---系统重启---

### 初始化配置
手动配置: Router#config-transaction
然后贴如下配置:
```shell
hostname Branch2_cEdge
!
system
 system-ip             10.10.10.20
 site-id               20
 sp-organization-name  testrabbit
 organization-name     testrabbit
 vbond vbond.testrabbit.local
!

interface GigabitEthernet1
 ip address 202.100.20.1 255.255.255.0
 no shutdown
exit
interface Tunnel1
 ip unnumbered GigabitEthernet1
 tunnel source GigabitEthernet1
 tunnel mode sdwan
exit
ip name-server 202.100.100.200
ip route 0.0.0.0 0.0.0.0 202.100.20.254
!
sdwan
 interface GigabitEthernet1
  tunnel-interface
   encapsulation ipsec
   color public-internet restrict
   allow-service all

commit

```

### 下载根证书
```shell
copy ftp://202.100.100.200/root.cer bootflash:/root.cer

```

### 卸载设备原始的根证书
```shell
request platform software sdwan root-cert-chain uninstall 

```

### 加载根证书
```shell
request platform software sdwan root-cert-chain install bootflash:/root.cer

```

### 复制uuid / otp
Configuration --- Devices --- WAN Edge List --- 选择一个vEdge Cloud -- Generate Bootstrap Configuration --- Cloud-init --- 找一个CSR1000v (复制 uuid / otp)

### 推荐选择 Classis Number
CSR-C5DADDE3-898F-1138-9C9D-EF421E49E8B6

### 激活Edge
```shell
request platform software sdwan vedge_cloud activate chassis-number <uuid> token <opt>

```

### request 举例
```shell
uuid : CSR-94E39A6E-F7B4-DEF9-2333-360F0C1B8FE7
opt  : 41ca622911d94e9cb98245d22cd6ae42
 
request platform software sdwan vedge_cloud activate chassis-number CSR-94E39A6E-F7B4-DEF9-2333-360F0C1B8FE7 token 41ca622911d94e9cb98245d22cd6ae42

```