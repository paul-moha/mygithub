# 開啟FTP服務
sudo yum install vsftpd

# 啟動 FTP 伺服器服務並設置它在開機時自動啟動
- sudo systemctl start vsftpd
- sudo systemctl enable vsftpd

# 創建FTP帳號 "ISE"，並設置密碼
- sudo useradd ISE
- echo 'P@ssw0rd!QAZ' | sudo passwd --stdin ISE

# 設置FTP的預設目錄為ISE帳號的家目錄。編輯 vsftpd 的配置文件
sudo vim  /etc/vsftpd/vsftpd.conf
# 在配置文件中，將以下行添加或編輯如下
chroot_local_user=YES
local_root=/home/$USER

# 重啟服務
sudo systemctl start vsftpd
sudo systemctl enable vsftpd

# FTP 建立user shell
``````
#!/bin/bash

# 提示用戶輸入帳號名稱
read -p "請輸入新的FTP帳號名稱: " username

# 提示用戶輸入密碼
read -p "請輸入新的FTP帳號密碼: " password

# 創建FTP帳號並設置密碼
sudo useradd $username
echo "$password" | sudo passwd --stdin $username

echo "FTP帳號 $username 創建完成，密碼已設定
``````