#encoding='utf-8'
import requests
import lxml.html
from lxml import etree
import codecs
url_exam = 'http://www.jjwxc.net/onebook.php?novelid=1508652&chapterid=1'
urls=[ ]
for i in range(1,25):
   url_list ='http://www.jjwxc.net/onebook.php?novelid=1508652&chapterid={}'.format(i)
   urls.append(url_list)
for each in urls:
   print(each)
   html = requests.get(each)
   #html = requests.get(each).content
  
   selector = lxml.html.fromstring(html.text)
   #print selector.text_content()
   #selector = etree.HTML(htm)
   #for tag in selector.findall('*div'):
   #    print tag.text_content()
  # 
  
  
   content_text =selector.xpath('//div[@class="noveltext"]/text()')
   
   #print(content_text)  
   
   content = '\n'.join(content_text)
   with codecs.open('1.txt','a',encoding='ISO-8859-1') as f:
              f.write(content)
              f.write('\n')
              f.close( )
