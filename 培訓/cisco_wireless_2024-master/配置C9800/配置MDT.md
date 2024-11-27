### 配置MDT (gnmi访问的域名要和证书的CN一致)
```shell
gnxi
gnxi secure-password-auth
gnxi secure-trustpoint WLC_TP
gnxi secure-server
gnxi server
netconf-yang
restconf

```

### 查看gnxi状态
```shell
qytwlc1#show gnxi state detail
Settings
========
  Server: Enabled
  Server port: 50052
  Secure server: Enabled
  Secure server port: 9339
  Secure client authentication: Disabled
  Secure trustpoint: WLC_TP
  Secure client trustpoint:
  Secure password authentication: Enabled

GNMI
====
  Admin state: Enabled
  Oper status: Up
  State: Provisioned

  gRPC Server
  -----------
    Admin state: Enabled
    Oper status: Up

  Configuration service
  ---------------------
    Admin state: Enabled
    Oper status: Up

  Telemetry service
  -----------------
    Admin state: Enabled
    Oper status: Up

GNOI
====

  Cert Management service
  -----------------
    Admin state: Enabled
    Oper status: Up

  OS Image service
  ----------------
    Admin state: Disabled
    Oper status: Up
    Supported: Not supported on this platform

  Factory Reset service
  ---------------------
    Admin state: Enabled
    Oper status: Up
    Supported: Not supported on this platform

```