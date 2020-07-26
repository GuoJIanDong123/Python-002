## Request爬虫&Scrapy爬虫
### 一、Scrapy核心组件
#### 1、组成
|Scrapy核心组件|简介|
|-|-|
|引擎(Engine)|"大脑"，指挥其他组件协调工作|
|调度器(Scheduler)|调度引擎发过来的请求，按照先后顺序，压入队列，同时去除重复请求|
|下载器(Downloader)|下载器用于下载网页内容，并返回给爬虫|
|爬虫(Spiders)|用于从特定的网页提前需要的信息，即所谓的实体(Item),用户也可以从中提取出链接，让Scrapy继续抓出下一个页面|
|项目管道(Item Pipelines)|项目管道负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性，消除不需要的信息等|
|下载器中间件(Downloader Middlewares)||
|爬虫中间件(Spider Middlewares)||

***
[Scrapy 架构官方文档](https://docs.scrapy.org/en/latest/topics/architecture.html)

#### 2、使用
|组件|对应爬虫三大流程|Scrapy项目是否需要修改|
|-|-|-|
|引擎||无需修改，框架已写好|
|调度器||无需修改，框架已写好|
|下载器|获取网页(request库)|无需修改，框架已写好|
|爬虫器|解析网页(BeautifulSoup库)|需要|
|管道|存储数据(存入csv/txt/Mysql等)|需要|
|下载器中间件|获取网页-个性化部分|一般不用|
|爬虫器中间件|解析网页-个性化部分|一般不用|

