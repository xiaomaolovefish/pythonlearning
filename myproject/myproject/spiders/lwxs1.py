from scrapy.spider import BaseSpider
from myproject.items import MyprojectItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import HtmlResponse
from scrapy.http import Request
class LwxsSpider(BaseSpider):
    name = "lwxs1"
    allowed_domains = ["bsl8.la"]
    start_urls = (
        'http://www.bsl8.la/read/57/57455/',
        )
  
				
    def parse(self,response):
		x = HtmlXPathSelector(response)
		#selector =  x.select('//TABLE/a/@href').extract()
		selector =  x.select('//a[contains(@href, "html")]/@href').extract()
		for url in selector:
			url_list = response.url + url
                        #url_list = url
			yield Request(url=url_list, callback=self.parse_detail)
			
    def parse_detail(self, response):
		x = HtmlXPathSelector(response)
		item = MyprojectItem()
		#item['link'] = response.url
		item['title'] = x.select('//title/text()').extract()
		#item['desc'] = x.select('//*[@id="pagecontent"]/text()').extract()
		#item['desc'] = x.select('//*[@id="content"]/p').extract()
		item['desc'] = x.select('//*[@id="content"]/text()').extract()
		return item
  
