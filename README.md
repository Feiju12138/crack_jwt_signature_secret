
## 下载依赖

```shell
pip3 install pyjwt
```

## 准备字典

- dict.txt

```txt
123
456
...
```

## 暴力破解

```shell
python3 crack_jwt_signature_secret.py dict.txt xxx.xxx.xxx HS256
```
