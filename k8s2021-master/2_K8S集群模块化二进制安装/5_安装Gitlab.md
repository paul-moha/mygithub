### 拉取官方镜像(gitlab)
```shell
docker pull gitlab/gitlab-ce

```
### 运行gitlab(gitlab)
```shell
mkdir /gitlab

sudo docker run --detach \
  --hostname gitlab.qytanghost.com \
  --publish 443:443 --publish 80:80 --publish 2222:22 \
  --name gitlab \
  --restart always \
  --volume /gitlab/config:/etc/gitlab \
  --volume /gitlab/logs:/var/log/gitlab \
  --volume /gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce

```

### 等待直到出现 (health: healthy)(gitlab)
[root@gitlab ~]# docker ps
CONTAINER ID   IMAGE              COMMAND             CREATED         STATUS                   PORTS                                                                                                             NAMES
54198f33e795   gitlab/gitlab-ce   "/assets/wrapper"   5 minutes ago   Up 5 minutes (healthy)   0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp, 0.0.0.0:2222->22/tcp, :::2222->22/tcp   gitlab


### 如果第一次启动出现(health: unhealthy). 尝试重启容器 (gitlab)
```shell
docker restart gitlab

```

### 查询初始化密码(gitlab)
cat /gitlab/config/initial_root_password

忽略其它，下面是密码
Password: UIjScu5Rx8oTG1kv3YOBnhZPfS1owjaJkWB4KKIKAso=


### 登录Gitlab(管理WIN7)[详细操作参考PPT]

### 修改Gitlab密码(管理WIN7)[详细操作参考PPT]