#!/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import parse
import sys


if __name__ == "__main__":
    #print "hello world"
    conf = parse.parse_conf()
    appid = conf[0]
    secretKey = conf[1] 
    #print appid
    #print secretKey
     
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = sys.argv[1]
    #print q
    fromLang = parse.parse_from(sys.argv[1])
    toLang = 'zh'
    #如果源语种是中文，则换英文输出
    if(fromLang == toLang):
        toLang = 'en'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
     
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
     
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        string = response.read().split("\"")[-2]
        print string.decode('unicode_escape')
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
