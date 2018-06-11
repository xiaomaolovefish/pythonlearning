from scrapy.spider import BaseSpider

class Bs18Spider(BaseSpider):
    name = "bsl8"
    allowed_domains = ["bsl8.la"]
    start_urls = (
        'http://www.bsl8.la/read/57/57455/',
        )
  
				
    def parse(self,response):
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
		#item['link'] = response.url
		item['title'] = x.select('//title/text()').extract()
		#item['desc'] = x.select('//*[@id="pagecontent"]/text()').extract()
		item['desc'] = x.select('//*[@id="content"]/p').extract()
		return item
