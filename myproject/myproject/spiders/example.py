from scrapy.spider import BaseSpider
from myproject.items import MyprojectItem
from scrapy.selector import HtmlXPathSelector
class ExampleSpider(BaseSpider):
    name = "example"
    allowed_domains = ["ggdown.com"]
    start_urls = (
        'http://www.ggdown.com/39/39423',
        'http://www.ggdown.com/39/39423/12440651.html'
        )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = MyprojectItem()
            item['title'] = site.select('//*[@id="BookCon"]/h1/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('//*[@id="pagecontent"]/text()').extract()
            items.append(item)
        return items
