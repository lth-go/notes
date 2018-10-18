# 加法

```
awk 'BEGIN{summ=0}{summ=summ+$1+$2}END{print summ}' test.log
```

