#-*- coding: utf-8 -*-
import urllib, urllib2
import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ClientCookie
from ClientForm import ParseResponse

url_login='https://nid.naver.com/nidlogin.login'
url_cafe='http://cafe.naver.com/wkqdbsxo14'
url_write='http://cafe.naver.com/ArticleWrite.nhn?clubid=14001943&menuid=433&boardtype=&page=1&specialmenutype=&userDisplay=15&m=write'
url_list='http://cafe.naver.com/ArticleList.nhn'


# 네이버 로그인 주소
id = 'suprimeisgood'
pw = 'sjwkfskTek0'
#xpaths = {'id': "//input[@name='id']", 'pw':"//input[@name='pw']"}

xpaths = {'id': "//input[@name='id']", 'pw':"//input[@name='pw']"}

#mydriver = webdriver.Firefox()
mydriver=webdriver.PhantomJS(executable_path=r'C:\Python27\phantomjs\bin\phantomjs.exe')
# 파이어폭스 path 어쩌고 에러가 나면서 못 찾는다면 일단 본인의 서버에 FireFox를 설치해보자
# (참고 파이어폭스 설치)

mydriver.get(url_login)
mydriver.find_element_by_xpath(xpaths['id']).send_keys(id)
mydriver.find_element_by_xpath(xpaths['pw']).send_keys(pw)
btn = mydriver.find_element_by_css_selector('.int_jogin')


btn.click()
cafe=mydriver.find_element_by_id('svc.cafe')
cafe.click()
#cafe=mydriver.find_element_by_css_selector("a[href='http://cafe.naver.com/wkqdbsxo14']")

#cafe.click()
mydriver.get(url_write)
subject=mydriver.find_element_by_name('subject')
subject.clear()
subject.send_keys('model')
mydriver.find_element_by_name("content")

btn=mydriver.find_element_by_id('cafewritebtn')
btn.click()
print mydriver.title