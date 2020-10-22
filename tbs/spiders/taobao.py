import scrapy
from ..items import TbsItem


class TaobaoSpider(scrapy.Spider):
    name = 'tbs'
    allowed_domains = ['taobao.com']
    start_urls = ['https://www.taobao.com/']

    def parse(self, response):
        items = TbsItem()
        lists = response.xpath('//div[@class="service-float"]/div[contains(@style, "display:none")]')
        print(lists)
        for node in lists:
            items['parent_node'] = node.xpath('h5/text()').extract()
            items['child_node'] = node.xpath('p/a/text()').extract()
            yield items

