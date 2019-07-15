# CISCN 2019 华东南 Web9

## 题目详情

- **2019 CISCN 2019 华东南 Web9**

## 感谢
- 华东南赛区的南溟师傅备份题目并提供给我复现。
- Decade 师傅和出题人师傅提供 exp 让我能偷懒不写 exp 了。

## 考点

- 储存型XSS
- 任意文件上传

## 启动

	docker-compose up -d
	open http://127.0.0.1:8083/

## WriteUp & Exp

1. XSS 拿到管理员 Cokkie。
2. 任意文件上传，覆盖 __init__.py，让程序重启加载，把 flag 写到静态资源目录。

exp 文件夹自取。

## 版权

该题目复现环境尚未取得主办方及出题人相关授权，如果侵权，请联系本人删除（ i@zhaoj.in ）
