# -*- coding: utf-8 -*- 
from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote, quote_plus

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

request = Request(url + unquote(param))
request.get_method = lambda:'GET'
response_body = urlopen(request).read()
print(response_body)