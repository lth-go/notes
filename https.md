### 创建HTTPS证书

```sh
docker run -it --rm \
    --dns=8.8.8.8 \
    -v "$(pwd)/letsencrypt:/etc/letsencrypt" \
        certbot/certbot certonly \
            --manual \
            --preferred-challenges dns \
            --server https://acme-v02.api.letsencrypt.org/directory \
            -m {mail} \
            -d {domain}
```
