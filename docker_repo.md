# Docker

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
