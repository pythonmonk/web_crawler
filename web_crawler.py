#-*- coding: utf-8 -*-
import cookielib, urllib2, urllib

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

params = urllib.urlencode({"mode":"login", "pixiv_id":"hwanisgood", "pass":"suprimeisgood"})
req = urllib2.Request("http://www.naver.com", params)

data = urllib.urlopen('http://cafe.naver.com/joonggonara')
#decode
result = data.decode('utf-8')
#html = res.read()
print result.read()
print ('테스트');

# "www.daum.net" 로그인
import urllib
import urllib2
import ClientCookie

form = { id: '아이디', pw: '비밀번호 }
# 파라미터
qstring = urllib.urlencode(form)
# 다음 로그인 페이지
request = urllib2.Request('https://logins.daum.net/Mail-bin/login.cgi?%s' % qstring)
response = ClientCookie.urlopen(request)

# 로그인 되었는지 확인할 사용자 정보 페이지
request = urllib2.Request('https://user.daum.net/daumuser/loginUserInfo.daum?t__nil_loginbox=modify')
response = ClientCookie.urlopen(request)
print response.read()