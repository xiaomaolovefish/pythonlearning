from scrapy.spider import BaseSpider
from myproject.items import MyprojectItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import HtmlResponse
from scrapy.http import Request
class LwxsSpider(BaseSpider):
    name = "lwxs"
    allowed_domains = ["lwxs520.com"]
    start_urls = (
        'http://www.lwxs520.com',
        )
    def parse(self,response):
            m = HtmlXPathSelector(response)
	    #selects = m.select('//*[@id="container"]/div/div[2]/div[1]/h5/a/')
            selects = m.select('//a/@href').extract()
	   # print selects
	    for url in selects:
                if  "index.html" in url:
                    print url
                    #yield self.make_requests_from_url(str(url))
                    yield Request(url=str(url), callback=self.parse_item)
                else:
                    pass
				
    def parse_item(self,response):
		x = HtmlXPathSelector(response)
		#selector =  x.select('//TABLE/a/@href').extract()
		selector =  x.select('//a[contains(@href, "html")]/@href').extract()
		for url in selector:
			url_list = response.url[:-10] + url
                        #url_list = url
			yield Request(url=url_list, callback=self.parse_detail)
			
    def parse_detail(self, response):
		x = HtmlXPathSelector(response)
		item = MyprojectItem()
		item['link'] = response.url
		item['title'] = x.select('//title/text()').extract()
		#item['desc'] = x.select('//*[@id="pagecontent"]/text()').extract()
		item['desc'] = x.select('//*[@id="content"]/p').extract()
		return item
  
