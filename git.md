# Git

## 专用名词

* Workspace：工作区
* Index / Stage：暂存区
* Repository：仓库区（或本地仓库）
* Remote：远程仓库

---

## 配置

Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。

* 显示当前的Git配置
`$ git config --list`

* 设置提交代码时的用户信息
`$ git config [--global] user.name "[name]"`
`$ git config [--global] user.email "[email address]"`

---

## 初始化仓库

* 在当前目录新建一个Git代码库
`$ git init`

* 下载一个项目和它的整个代码历史
`$ git clone <url>`

---

## 增加/删除文件

* 添加指定路径下的内容到暂存区
`$ git add <path>`

* 停止追踪指定文件，但该文件会保留在工作区
`$ git rm --cached [file]`

* 改名文件，并且将这个改名放入暂存区
`$ git mv [file-original] [file-renamed]`

---

## 代码提交

* 提交暂存区到仓库区
`$ git commit -m [message]`

* 使用一次新的commit，替代上一次提交
`$ git commit --amend`

---

## 分支

* 列出所有分支, 远端-r, 所有-a
`$ git branch [-r | -a]`

* 新建一个分支
`$ git branch <分支名> [<起始点>]`

* 新建一个分支，与指定的远程分支建立追踪关系
`$ git branch --track [branch] [remote-branch]`

* 建立追踪关系，在现有分支与指定的远程分支之间
`$ git branch --set-upstream-to=<remote-branch> [branch]`

* 删除分支
`$ git branch -d [branch-name]`

* 删除远程分支
`$ git branch -dr [remote/branch]`

* 切换到指定分支，并更新工作区
`$ git checkout [-b] [branch-name]`

* 合并指定分支到当前分支
`$ git merge [branch]`

---

## 查看信息

* 显示有变更的文件
`$ git status [--ignored]`

### log

* 显示当前分支的版本历史
`$ git log`

* 显示commit历史，以及每次commit发生变更的文件
`$ git log --stat`

* 显示某个文件的版本历史
`$ git log -- [file]`

* 显示指定文件相关的每一次diff
`$ git log -p [file]`

* 显示过去5次提交
`$ git log -5 `

### diff

* 显示暂存区和工作区的差异
`$ git diff`

* 显示暂存区和工作区某个文件差异
`$ git diff -- [file]`

* 显示暂存区和上一个commit的差异
`$ git diff --cached [file]`

* 显示两次提交之间的差异
`$ git diff [first-branch] [second-branch] -- [file]`

### show

* 显示某次提交的元数据和内容变化
`$ git show [commit]`

* 显示某次提交发生变化的文件
`$ git show --name-only [commit]`

* 显示某次提交时，某个文件的内容
`$ git show [commit]:[filename]`

---

## 远程同步

* 下载远程仓库的所有变动
`$ git fetch [remote]`

* 增加一个新的远程仓库，并命名
`$ git remote add [shortname] [url]`

* 显示所有远程仓库
`$ git remote -v`

* 取回远程仓库的变化，并与本地分支合并
`$ git pull [remote] [branch]`

* 上传本地指定分支到远程仓库
`$ git push [--force] [remote] [branch]`

---

## 撤销

* 恢复暂存区的指定文件到工作区
`$ git checkout [file]`

* 恢复某个commit的指定文件到暂存区和工作区
`$ git checkout [commit] [file]`

* 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
`$ git reset [file]`

* 重置暂存区与工作区，与上一次commit保持一致
`$ git reset --hard`

* 重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
`$ git reset [commit]`

* 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
`$ git reset --hard [commit]`

* 重置当前HEAD为指定commit，但保持暂存区和工作区不变
`$ git reset --keep [commit]`

* 新建一个commit，用来撤销指定commit
* 后者的所有变化都将被前者抵消，并且应用到当前分支
`$ git revert [commit]`

* 暂时将未提交的变化移除，稍后再移入
`$ git stash`
`$ git stash pop`

---

## 标签

* 列出所有tag
`$ git tag`

* 新建一个tag在当前commit
`$ git tag [tag]`

* 新建一个tag在指定commit
`$ git tag [tag] [commit]`

* 删除本地tag
`$ git tag -d [tag]`

* 删除远程tag
`$ git push origin :refs/tags/[tagName]`

* 查看tag信息
`$ git show [tag]`

* 提交指定tag
`$ git push [remote] [tag]`

* 提交所有tag
`$ git push [remote] --tags`

* 新建一个分支，指向某个tag
`$ git checkout -b [branch] [tag]`

---

# ManPage

## git reset

+ `git reset [-q] [<tree-ish>] [--] <paths>...`
+ `git reset [<mode>] [<commit>]`

## git checkout

+ `git checkout <branch>`
+ `git checkout -b|-B <new_branch> [<start point>]`

+ `git checkout [<tree-ish>] [--] <pathspec>...`
