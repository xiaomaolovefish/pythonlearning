from scrapy.spider import BaseSpider
#from scrapy.spider import  Rule
from myproject.items import MyprojectItem
from scrapy.selector import HtmlXPathSelector
#from scrapy.contrib.linkextractors import LinkExtractor
#from scrapy.linkextractors import LinkExtractor
#from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import HtmlResponse
from scrapy.http import Request
class GgownSpider(BaseSpider):
	name = "ggown"
	allowed_domains = ["ggdown.com"]
	start_urls = (
		'http://www.ggdown.com/41/41128/',
	   
		)
	
   # rules = [Rule(LinkExtractor(allow=['/\d+/\d+[^/]+/$'])),
	#         Rule(LinkExtractor(allow=['/\d+/\d+[^/]+/$']), 'parse_item')]
	
	def start_requests(self): 
            for u in self.start_urls:
                r = Request(url = u, dont_filter=True, callback=self.parse)
                r.meta['dont_redirect'] = True
                yield r
	def parse(self,response):
            m = HtmlXPathSelector(response)
	    #selects = m.select('//*[@id="container"]/div/div[2]/div[1]/h5/a/')
            selects = m.select('//a/@href').extract()
	    print selects
	    for url in selects:
                print url
		yield self.make_requests_from_url(str(url))
		yield Request(url=str(url), callback=self.parse_item)
				
	def parse_item(self,response):
		x = HtmlXPathSelector(response)
		selector =  x.select('//a/@href').extract()
		for url in selector:
			#url_list = response.url + url
                        url_list = url
			yield Request(url=url_list, callback=self.parse_detail)
			
	def parse_detail(self, response):
		x = HtmlXPathSelector(response)
		item = MyprojectItem()
		item['link'] = response.url
		item['title'] = x.select('//*[@id="BookCon"]/h1/text()').extract()
		#item['desc'] = x.select('//*[@id="pagecontent"]/text()').extract()
		item['desc'] = x.select('//div[contains(@id, "pagecontent")]/text()').extract()
		return item
  
