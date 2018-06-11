#encoding='utf-8'
import requests
import lxml.html
from lxml import etree
import codecs
import re
import sys
print sys.stdout.encoding

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
def get_novelid():
    pat=re.compile('novelid=(.+?)&chapterid')
    a=list()
    #file=open('4.txt')#old file
    with open('4.txt') as file:
        for line in file:
           match=pat.search(line)
   
           if match:#find"<content>xxx</content>"
        #print(match.group(1))#write to the new file
               novelid=match.group(1)
               a.append(novelid)
      
        #print(a)
              
    file.close()#close old file
    return(a)


url_exam = 'http://www.jjwxc.net/onebook.php?novelid=1508652&chapterid=1'
urls = [ ]
def get_url(a):
    
    for novel_id in a:
    
    #print novel_id
        for j in range(1,25):
            #url_list ='http://www.jjwxc.net/onebook.php?novelid='+ novel_id + '&chapterid={}'.format(j)
            url_list ='http://www.jjwxc.net/onebook.php?novelid=%s&chapterid=%d' %( novel_id ,j)
            
            urls.append(url_list)
            #print(urls)
    return(urls)


def get_content(urls):
    
   html = requests.get(each)
   #html = requests.get(each).content
   selector = lxml.html.fromstring(html.text)
   content_text =selector.xpath('//div[@class="noveltext"]/text()')
   return(content_text)
   #print selector.text_content()
   #selector = etree.HTML(htm)
   #for tag in selector.findall('*div'):
   #    print tag.text_content()
  # 
  
   
   #print(content_text)

def write_content(each,content_text):
    print len(each)
    if len(each) > 60:
        filename = each[-20:-13]+'.txt'
    else:
        filename = each[-19:-12]+'.txt'
    content = '\n'.join(content_text)
    content = content.encode('ISO-8859-1','ignore')
  # with codecs.open('1.txt','a',encoding='ISO-8859-1') as f:
    with open(filename,'a') as f:
              f.write(content)
              f.write('\n')
              f.close( )

if __name__ == '__main__':  
       
    a = get_novelid()
    print(a)
    urls = get_url(a)
    for each in urls:
        print(each)
        content_text = get_content(each) 
        write_content(each,content_text)
