#Docker

##Docker Registry

**namespace** 为 library

###获取仓库中所有标签

`GET /v1/repositories/(namespace)/(repository)/tags`

例:
`http docker.jcing.com/v1/repositories/library/mapboom_repo/tags`

###获取指定标签的镜像ID

`GET /v1/repositories/(namespace)/(repository)/tags/(tag*)`

例:
`http 'docker.jcing.com/v1/repositories/library/mapboom_repo/tags/1.0.0'`

###删除指定标签的镜像

`DELETE /v1/repositories/(namespace)/(repository)/tags/(tag*)`

例:
`http delete 'docker.jcing.com/v1/repositories/library/mapboom_repo/tags/1.0.0'`

###上传镜像

`PUT /v1/repositories/reynholm/help-system-server/tags/latest`

参数:
```
namespace – namespace for the repo
repository – name for the repo
tag – name of tag you want to add
```

###删除镜像仓库

`DELETE /v1/repositories/(namespace)/(repository)/`

###搜索

`GET /v1/search`

参数:

```
q – 关键字
n - 每页条数
page - 多少页
```

例:
`http 'docker.jcing.com/v1/search?q=auth&n=1&page=5'`

###状态检查

`GET /v1/_ping`

`http 'docker.jcing.com/v1/_ping'`
