"""A spider to crawl 36kr.com"""

import re
import scrapy
from crawl_36kr.items import Crawl36KrItem


class Spider36kr(scrapy.Spider):
    name = "36kr"
    allowed_domains = ["36kr.com/"]
    start_urls = ["http://36kr.com/"]
    max_pages = 10000
    crawl_pages = 0
    crawl_url = []

    def parse(self, response):
        item = Crawl36KrItem()
        item["title"] = response.xpath("/html/head/title/text()").extract()
        item["url"] = response.url
        yield item

        page = response.body.decode()
        url_root = "http://36kr.com/p/"
        ids = re.findall(
            '"id":"(\d*)","column_id":"(\d*)","related_company_id"', page)
        ids = [x[0] for x in ids]
        for url_id in ids:
            url = url_root + url_id
            if url in self.crawl_url:
                continue
            self.crawl_url.append(url)
            self.crawl_pages += 1
            if self.crawl_pages > self.max_pages:
                break
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
