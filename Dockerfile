FROM python:2.7-alpine

LABEL Author="glzjin <i@zhaoj.in>" Blog="https://www.zhaoj.in"

ENV FLASK_APP=app.py FLASK_ENV=production

COPY app /app

RUN adduser -h /app glzjin -D && \
	sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories && \
	apk update && \
	apk add --no-cache gcc libc-dev libffi-dev libxml2-dev python-dev libxml2-dev g++ libxslt-dev curl && \
	pip install \
	-i http://mirrors.aliyun.com/pypi/simple/ \
	--trusted-host mirrors.aliyun.com \
	-r /app/requirements.txt && \
	mv /app/docker-entrypoint /usr/local/bin/docker-entrypoint && \
	chmod +x /usr/local/bin/docker-entrypoint && \
	mv /app/flag.sh / && \
	chown -R glzjin:glzjin /app/db.sqlite3 && \
	chown -R glzjin:glzjin /app/*/__init__.py && \
	mv /app/phantomjs.tar.gz /tmp/ && \
	cd /tmp && \
	tar -xf phantomjs.tar.gz -C /tmp/ && \
	cp -R /tmp/etc/fonts /etc/ && \
	cp -R /tmp/lib/* /lib/ && \
	cp -R /tmp/lib64 / && \
	cp -R /tmp/usr/lib/* /usr/lib/ && \
	cp -R /tmp/usr/lib/x86_64-linux-gnu /usr/ && \
	cp -R /tmp/usr/share/* /usr/share/ && \
	cp /tmp/usr/local/bin/phantomjs /usr/bin/ && \
	rm -rf /tmp/*

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]
