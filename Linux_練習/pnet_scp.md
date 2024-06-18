## 安裝sshpass
apt-get  install -y sshpass

## 生成密钥文件
ssh-keygen -f /root/.ssh/id_rsa -P ''

## 修改/etc/hosts
- vim /etc/hosts
- 172.18.199.117 paul-pnet

## 將key copy到目的主機
ssh-copy-id -o StrictHostKeyChecking=no  paul-pnet

## SCP複製
scp -r  /opt/unetlab/addons/qemu/win-10-x64-21H1v1 paul-pnet:/opt/unetlab/addons/qemu/
 > -r 為子目錄




