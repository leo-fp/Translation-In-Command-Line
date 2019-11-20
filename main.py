#!/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import parse
import sys

class Creator:
    @classmethod
    def createTranslator(self, transClass):
        transIns = transClass()
        return transIns

# base class
class Translator_ab:
    _TYPE = ""   # type of translator. ONLINE / OFFLINE
    _api = ""    # api
    _query = ""  # content to be translated
    _from = ""   # source language
    _to = ""     # target language

    def __init__(self):
        print "...init..."

    ############################
    # get methods
    ############################
    def getType(self):
        return self.YPE

    def getQuery(self):
        return self._query
    
    def getFrm(self):
        return self._from

    def getTo(self):
        return self.To

    def getApi(self):
        return self._api

    ############################
    # set methods
    ############################
    def setType(self, _TYPE):
        self._TYPE = _TYPE

    def setQuery(self, _query):
        self._query = _query
    
    def setFrm(self, from_):
        self._from = from_

    def setTo(self, *to):
        toLang = 'zh'
        #如果源语种是中文，则换英文输出
        if(self._from == toLang):
            self._to = 'en'

    def setApi(self, api):
        self._api = api

    # base launch
    def launch(self):
        print "base launch"
        

class TransOL(Translator_ab):
    _appid = ""  # APP ID
    _secretKey = ""  # secretKey
    _salt = ""   # rand num
    _sign = ""   # signature
    _tts = ""    # flag of speech synthesis
    _dic = ""    # dictionaries
    _myurl = ""  # request string
    def __init__(self):
        conf = parse.parse_conf()
        self._TYPE = "ONLINE"
        self._appid = conf[0]
        self._secretKey = conf[1]
        self._myurl = '/api/trans/vip/translate'
        self._to = 'zh'
        self._from = 'en'


    # get method
    def getMyurl(self):
        return self._myurl

    def getSecreatKey(self):
        return self._secretKey
    
    def getAppid(self):
        return self._appid

    def getSalt(self):
        return self._salt

    def getSign(self):
        return self._sign

    def getTts(self):
        return self._tts

    def getDic(self):
        return self._dic

    # set method
    def setMyurl(self, *myurl):
        self._myurl = self._myurl+'?appid='+self._appid+'&q='+urllib.quote(self._query)+'&from='+self._from+'&to='+self._to+'&salt='+str(self._salt)+'&sign='+self._sign

    def setSecretKey(self, secretKey):
        self._secretKey = secretKey

    def setAppid(self, appid):
        self._appid = appid

    def setSalt(self, *salt):
        self._salt = random.randint(32768, 65536)

    def setSign(self, *sign):
        sign = self._appid+self._query+str(self._salt)+self._secretKey
        m1 = md5.new()
        m1.update(sign)
        self._sign = m1.hexdigest()

    def setTts(self, tts):
        self._tts = tts

    def setDic(self, dic):
        return self._dic

    # build the request and translate
    # _query: the contents you need to translate
    def launch(self, _query):
        self.setQuery(_query)
        self.setFrm(parse.parse_from(sys.argv[1]))
        self.setTo()
        self.setSalt()
        self.setSign()
        self.setMyurl()
        # print self._TYPE
        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            # print self.getMyurl()
            httpClient.request('GET', self._myurl)
         
            #response是HTTPResponse对象
            response = httpClient.getresponse()
            string = response.read().split("\"")[-2]
            print string.decode('unicode_escape')
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
    
class TransOFL(Translator_ab):
    def __init__(self):
        self.setType("OFFLINE")
        print self.getType()


if __name__ == "__main__":
    transOL = Creator.createTranslator(TransOL)
    transOL.launch(sys.argv[1])
