# Docker

## Repo proxy

### docker.io镜像加速

```
docker pull xxx:yyy
docker pull docker.mirrors.ustc.edu.cn/library/xxx:yyy
docker pull dockerhub.azk8s.cn/library/xxx:yyy

docker pull xxx/yyy:zz
docker pull docker.mirrors.ustc.edu.cn/xxx/yyy:zz
docker pull dockerhub.azk8s.cn/xxx/yyy:zz
```


### gcr.io镜像加速

```
docker pull gcr.io/xxx/yyy:zzz
docker pull gcr.mirrors.ustc.edu.cn/xxx/yyy:zzz
docker pull gcr.mirrors.ustc.edu.cn/xxx/yyy:zzz
```

### k8s.gcr.io镜像加速

```
docker pull k8s.gcr.io/xxx:yyy
docker pull gcr.io/google-containers/xxx:yyy
docker pull gcr.mirrors.ustc.edu.cn/google-containers/xxx:yyy

docker pull k8s.gcr.io/xxx:yyy
docker pull gcr.io/google-containers/xxx:yyy
docker pull gcr.azk8s.cn/google-containers/xxx:yyy
```

### quay.io镜像加速

```
docker pull quay.io/xxx/yyy:zzz
docker pull quay.azk8s.cn/xxx/yyy:zzz
```

## Docker Registry v2

### List all repositories (effectively images)

```
curl -X GET /v2/_catalog
> {"repositories":["redis","ubuntu"]}
```

### List all tags for a repository

```
curl -X GET /v2/{namespace}/repository/tags/list
> {"name":"ubuntu","tags":["14.04"]}
```

## Docker Registry v1

**namespace** 为 library

### 获取仓库中所有标签

`GET /v1/repositories/(namespace)/(repository)/tags`

例:
`http docker.jcing.com/v1/repositories/library/mapboom_repo/tags`

### 获取指定标签的镜像ID

`GET /v1/repositories/(namespace)/(repository)/tags/(tag*)`

例:
`http 'docker.jcing.com/v1/repositories/library/mapboom_repo/tags/1.0.0'`

### 删除指定标签的镜像

`DELETE /v1/repositories/(namespace)/(repository)/tags/(tag*)`

例:
`http delete 'docker.jcing.com/v1/repositories/library/mapboom_repo/tags/1.0.0'`

### 上传镜像

`PUT /v1/repositories/reynholm/help-system-server/tags/latest`

参数:
```
namespace – namespace for the repo
repository – name for the repo
tag – name of tag you want to add
```

### 删除镜像仓库

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
