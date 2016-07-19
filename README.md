# Zhua
# 基于python scrapy的爬虫去爬取[36氪](http://36kr.com/)以及[TechCrunch中国](http://techcrunch.cn/)的新闻

在Zhua/techcrunch下使用命令<pre><code>scrapy crawl techcrunch</code></pre>去抓取TechCrunch中国的内容。

目前可以抓取新闻标题、时间和url。

Zhua/techcrunch/analysis/key_word_of_the_site.ipynb: 使用jieba对标题进行分词并对TechCrunch中国2014年-2016年的热点单词进行的统计，并且分别
给出了每一年的top热点单词

在Zhua/crawl_36kr下使用命令<pre><code>scrapy crawl 36kr</code></pre>去抓取36kr首页新闻。目前可以抓取新闻标题和url
