# -*- coding: utf-8 -*- 
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

'''
urllib2 
- urllib과 urllib2 차이 : urllib(URL만 수용), urllib2(URL 요청을 위한 헤더를 설정하기 위한 Request 객체 수용) 


'''

# 사망교통사고정보서비스 URL
url = 'http://apis.data.go.kr/B552061/trafficAccidentDeath/getRestTrafficAccidentDeath?'

# 파라미터
param = urlencode({ 
    quote_plus('serviceKey') : "서비스키", 
    quote_plus('searchYear') : '2014', 
    quote_plus('siDo') : '1100', 
    quote_plus('guGun') : '1117', 
    quote_plus('type') : 'xml', 
    quote_plus('numOfRows') : '10', 
    quote_plus('pageNo') : '1' 
})

request = Request(url + param)
request.get_method = lambda:'GET'
response_body = urlopen(request).read()
print(response_body)