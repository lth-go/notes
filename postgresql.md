# Postgresql

## 登录数据库

`export PGPASSWORD='password';psql -U dbuser -d exampledb -h 127.0.0.1 -p 5432`

---

## 控制台命令

```
\password：设置密码
\q命令：退出

\h：查看SQL命令的解释，比如\h select。
\?：查看psql命令列表。

\c [database_name]：连接其他数据库。

\l：列出所有数据库。
\d：列出当前数据库的所有表格。
\d [table_name]：列出某一张表格的结构。

\du：列出所有用户。
\e：打开文本编辑器。
\conninfo：列出当前数据库和连接的信息。
```

---

## 数据库操作

* 创建数据库用户dbuser
`CREATE USER dbuser WITH PASSWORD 'password';`

* 创建用户数据库
`CREATE DATABASE exampledb OWNER dbuser;`

* 将exampledb数据库的所有权限都赋予dbuser
`GRANT ALL PRIVILEGES ON DATABASE exampledb to dbuser;`

* 修改密码 
`alter user postgres with password 'foobar';`

* 导出数据
`pg_dump -U postgres(用户名)  (-t 表名)  数据库名(缺省时同用户名)  > 路径/文件名.sql`

* 导入数据
`psql -d databaename(数据库名) -U username(用户名) -f  路径/文件名.sql `

* 自增主键
`SELECT setval('sample_id_seq',max(id)) from sample;`

### 基本的数据库操作

#### 表操作
* 创建新表
`CREATE TABLE user_tbl(name VARCHAR(20), signup_date DATE);`

* 删除表格
`DROP TABLE IF EXISTS backup_tbl;`

* 添加栏位
`ALTER TABLE user_tbl ADD email VARCHAR(40);`

* 删除栏位
`ALTER TABLE user_tbl DROP COLUMN email;`

* 设置约束
`ALTER TABLE user_tbl ALTER COLUMN signup_date SET NOT NULL;`

* 更新字段类型
`ALTER TABLE user_tbl ALTER COLUMN email TYPE VARCHAR(50);`

* 更名栏位
`ALTER TABLE user_tbl RENAME COLUMN signup_date TO signup;`

* 表格更名
`ALTER TABLE user_tbl RENAME TO backup_tbl;`

### 数据操作

* 插入数据
`INSERT INTO user_tbl(name, signup_date) VALUES('张三', '2013-12-22');`

* 选择记录
`SELECT * FROM user_tbl;`

* 更新数据
`UPDATE user_tbl set name = '李四' WHERE name = '张三';`

* 删除记录
`DELETE FROM user_tbl WHERE name = '李四' ;`

---
