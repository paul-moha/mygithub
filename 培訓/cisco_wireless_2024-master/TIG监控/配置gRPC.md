### Grafana 官方的Dashboard
https://grafana.com/grafana/dashboards/12468-catalyst-9800-client-stats/

### c9800 配置gRPC
```shell
telemetry ietf subscription 1
 encoding encode-kvgpb
 filter xpath /wireless-client-oper:client-oper-data/dot11-oper-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 2
 encoding encode-kvgpb
 filter xpath /wireless-client-oper:client-oper-data/traffic-stats
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 3
 encoding encode-kvgpb
 filter xpath /wireless-client-oper:client-oper-data/dc-info
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 4
 encoding encode-kvgpb
 filter xpath /wireless-client-oper:client-oper-data/sisf-db-mac
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 5
 encoding encode-kvgpb
 filter xpath /wireless-client-oper:client-oper-data/client-wsa-info
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 6
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/radio-oper-stats
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 7
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/ap-name-mac-map
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 8
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/capwap-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 9
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/radio-oper-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 10
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/ssid-counters
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 11
 encoding encode-kvgpb
 filter xpath /wireless-client-oper:client-oper-data/common-oper-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 12
 encoding encode-kvgpb
 filter xpath /wireless-rrm-oper:rrm-oper-data/rrm-measurement
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 13
 encoding encode-kvgpb
 filter xpath /wireless-mobility-oper:mobility-oper-data/mobility-node-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 14
 encoding encode-kvgpb
 filter xpath /wireless-mobility-oper:mobility-oper-data/wlan-client-limit
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 15
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 16
 encoding encode-kvgpb
 filter xpath /wireless-client-oper:client-oper-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 17
 encoding encode-kvgpb
 filter xpath /wireless-location-oper:location-oper-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 18
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/oper-data
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 19
 encoding encode-kvgpb
 filter xpath /wireless-access-point-oper:access-point-oper-data/radio-oper-data/vap-oper-config
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 1001
 encoding encode-kvgpb
 filter xpath /process-cpu-ios-xe-oper:cpu-usage/cpu-utilization
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 1002
 encoding encode-kvgpb
 filter xpath /memory-ios-xe-oper:memory-statistics/memory-statistic
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

telemetry ietf subscription 1003
 encoding encode-kvgpb
 filter xpath /interfaces-ios-xe-oper:interfaces/interface/statistics
 source-address 10.1.1.50
 stream yang-push
 update-policy periodic 3000
 receiver ip address 10.1.1.101 57000 protocol grpc-tcp

```