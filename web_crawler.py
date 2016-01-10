#-*- coding: utf-8 -*-
import urllib
import urllib2
import BeautifulSoup
import ClientCookie
from ClientForm import ParseResponse

#naver login
url_login='https://nid.naver.com/nidlogin.login'
url_cafe='http://cafe.naver.com/wkqdbsxo14'
url_write='http://cafe.naver.com/ArticleWrite.nhn'
url_list='http://cafe.naver.com/ArticleList.nhn'

forms = ParseResponse(urllib2.urlopen(url_login))
form = forms[0]

#print 'enter naver id'
form['id'] = 'suprimeisgood'
#print 'enter naver password'
#form['pw'] = raw_input()
form['pw'] = 'sjwkfskTek0'

request = form.click()
response = ClientCookie.urlopen(request)



#open naver cafe

response = urllib2.urlopen(url_cafe)

#get cafe clubid
#parsing
#assign clubid and menuid

soup = BeautifulSoup.BeautifulSoup(response)
forms = soup.findAll('form', attrs={'name':'notifrm'})
clubid = forms[0].find('input')['value']
menuid = '433'

title = 'model title'
content = 'model body'
referer = url_list+"?search.clubid="+clubid+"&search.menuid="+menuid+"&search.boardtype=L#"
#put title & content in form
#body = str(form)
body='temp'

#Request ArticleWrite.nhn

#add header clubid, menuid
#add body
#request
#referer = ArticleList.nhn
url='http://cafe.naver.com/ArticleWrite.nhn'

data = {'search.clubid':clubid, 'search.menuid':menuid,'search.boardtype':'L#'}
data = urllib.urlencode(data)

req = urllib2.Request(url, data)

req.add_header("referer", referer)

req.add_data(body)

response = urllib2.urlopen(req)
#Request TempsavePost.nhn

#add header clubid, menuid, referer
#add body
#request

#referer = ArticleWrite
url='http://cafe.naver.com/TempsavePost.nhn'

data = {'search.clubid':clubid, 'search.menuid':menuid,'search.boardtype':'L#'}
data = urllib.urlencode(data)

req = urllib2.Request(url, data)

referer = url_write+"?search.clubid="+clubid+"&search.menuid="+menuid+"&search.boardtype=L#"
req.add_header("referer", referer)

req.add_data(body)

response = urllib2.urlopen(req)
#Request ArticlePost.nhn
#add header clubid, menuid, referer
#add body
#request

#referer = ArticleWrite
url='http://cafe.naver.com/ArticlePost.nhn'

data = {'search.clubid':clubid, 'search.menuid':menuid,'search.boardtype':'L#'}
data = urllib.urlencode(data)

req = urllib2.Request(url, data)

req.add_header("referer", referer)

req.add_data(body)

response = urllib2.urlopen(req)
print 'last'

#board list add/delete
#writing attribute picture
#writing delay
