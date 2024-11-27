#!/bin/bash

# 創建新分支
git branch newbranch
echo "執行成功"


# 切換到新分支
git checkout newbranch
echo "執行成功"

# 將所有更改添加到暫存區
git add .
echo "執行成功"

# 提交更改
git commit -m "更新"
echo "執行成功"

# 切換回主分支
git checkout main
echo "執行成功"

# 將新分支合併到主分支
git merge newbranch
echo "執行成功"

# 推送到遠端主分支
git push -u origin main
echo "執行成功"

# 刪除新分支
git branch -D newbranch
echo "執行成功"

