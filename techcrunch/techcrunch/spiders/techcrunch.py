"""Crawl http://techcrunch.cn/ to get the
titles, dates and urls of all technology news"""

# -*- coding: utf-8 -*-
import scrapy
from techcrunch.items import TechcrunchItem


class TechcrunchSpider(scrapy.Spider):
    """A spider to crawl techcrunch.cn"""
    name = "techcrunch"
    allowed_domains = ["techcrunch.cn/"]
    start_urls = (
        'http://techcrunch.cn/%E6%96%B0%E9%97%BB/',
    )
    max_pages = 100000  # the max page to be crawled
    crawl_pages = 0
    crawl_url = []

    def parse(self, response):
        """parse the html page and extract date, title and url"""
        item = TechcrunchItem()
        item["title"] = response.xpath("/html/head/title/text()").extract()[0]
        item["url"] = response.url
        date = response.xpath("//time/text()").extract()
        if date == []:
            date = None
        elif (len(date) > 1) or (type(date) is list):
            date = date[0]
        item["date"] = date
        yield item

        urls = response.xpath("//@href").extract()
        urls = self._rm_dup_urls(urls)
        if len(urls) > 0:
            for url in urls:
                if (not url.startswith("http://techcrunch.cn/")) and \
                        (not url.startswith("https://techcrunch.cn/")):
                    continue
                if url in self.crawl_url:
                    continue
                self.crawl_url.append(url)
                self.crawl_pages += 1
                if self.crawl_pages > self.max_pages:
                    break
                yield scrapy.Request(url, callback=self.parse,
                                     dont_filter=True)

    def _rm_dup_urls(self, urls):
        """
        remove duplicated urls
        :param urls: list, the list of urls
        :return: list, the list of urls
        """
        urls = [self._remove_hash(x) for x in urls]
        urls = [self._remove_amp(x) for x in urls]
        urls = set(urls)
        return urls

    def _remove_hash(self, x):
        """
        remove the strings after # of a url
        :param x: string, url
        :return: string, url
        """
        return x.split('#')[0]

    def _remove_amp(self, x):
        """
        remove /amp or /amp/
        :param x: string, url
        :return: string, url
        """
        if x.endswith("amp"):
            return (x[:-3])
        if x.endswith("amp/"):
            return (x[:-4])
        return x
