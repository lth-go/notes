# mongo

```sh
show dbs                       # 查看所有数据库和使用情况
use foo                        # 切换到foo库，发现没有创建之
show collections               # 查看本库下所有集合
db.bar.find()                  # 查询某集合数据
db.bar.drop()                  # 删除某集合
db.dropDatabase()              # 删除某数据库
db.stats()                     # 当前数据库下简单信息 可以查看本库下有多少集合
db.bar.stats()                 # 查看某集合的基础信息
db.runCommand()                # 可以执行某个function()方法
db.help()                      # 查看数据库层面所有操作
db.bar.help()                  # 查看集合层面所有操作
db.listCommands()              # 列举数据库所有命令
db.bar.insert({"name":"haha"}) # 插入一条记录
```
