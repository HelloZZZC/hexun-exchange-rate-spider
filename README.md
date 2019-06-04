# hexun部分汇率数据爬虫
[TOC]
## 简介
爬取hexun部分汇率数据，因为爬取的数据是通过js渲染，因此采用了[scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)。在crawl前需要`docker pull scrapinghub/splash`下载镜像，然后执行`docker run -it -p 8050:8050 scrapinghub/splash`。

## 表结构
| id | from_country | to_country | rate | created_time | updated_time |
| --- | --- | --- | --- | --- | --- |
| 1 | 美元 | 人民币 | 638 | 1559611469 | 1559611469 |
