#encoding='utf-8'
#python 2.7.12
#author:xiaomaolovefish

#作业五
import requests
from lxml import etree


url_list=[]
def scanpage(url):
  websiteurl=url
  html = requests.get(websiteurl)
   #html = requests.get(each).content
  print(html.encoding)
   #selector = lxml.html.fromstring(html.text)
  selector = etree.HTML(html.text)
  hrefs = selector.xpath(u"//img/@src")

  #获取pic的URL
  for href in hrefs:
    href = 'http:'+href
    print href
    url_list.append(href)
   
  for each in url_list:
    content = requests.get(each).content
   #获取pic_url内容
    #html = requests.get(each)
  i = 0 
  string ='pictures\\'+str(i) +'.jpg'
  
  with open(string,'wb') as f:
     f.write(content)
     f.close( )
     i+= 1

scanpage("http://jandan.net/pic/page-188#comments")


