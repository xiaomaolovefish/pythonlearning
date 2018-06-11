#encoding='utf-8'
import requests
from lxml import etree
import urllib2
import codecs

t=[]
def scanpage(url):
  websiteurl=url
  html = requests.get(websiteurl)
   #html = requests.get(each).content
  print(html.encoding)
   #selector = lxml.html.fromstring(html.text)
  selector = etree.HTML(html.text)
  hrefs = selector.xpath(u"//a/@href")
  
  
  for href in hrefs:
     print href
     t.append(href)
     with open('4.txt','a') as f:
              f.write(href)
              f.write('\n')
              f.close( ) 

scanpage("http://www.jjwxc.net/")


for url in t:
  try:
      scanpage(url)
      
  except:
      print "connect failed"
  else:
      t2=time.time()
      print url
       

      
    

