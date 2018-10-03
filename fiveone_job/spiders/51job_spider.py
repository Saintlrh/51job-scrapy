import scrapy
from fiveone_job.items import FiveoneJobItem
from scrapy import Request

class FiveoneJobSpider(scrapy.Spider):
    name = 'fiveone'
    allowed_domains = ['51job.com']

    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    
    
        
        
    def parse(self,response):
        #item = FiveoneJobItem()
        #items = []
        results = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        for x in results:
            item = FiveoneJobItem()
            item['job'] = x.xpath('.//p/span/a/text()').extract()[0].strip()
            item['company'] = x.xpath('.//span[@class="t2"]/a/text()').extract()[0]
            item['location'] = x.xpath('.//span[@class="t3"]/text()').extract()[0]
            item['money'] = x.xpath('.//span[@class="t4"]/text()').extract()        
            #items.append(item)
        #return items
            yield item

            
        #处理下一页信息
        for i in range(2,10):
            next_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'+str(i)+'.html?'
            yield Request(next_url)

#注意，大坑来了！！！！
    '''def parse(self,reponse):
        items = []
        results = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        for x in results:
            item = FiveoneJobItem()
            item['job'] = x.xpath('.//p/span/a/text()').extract()[0].strip()
            item['company'] = x.xpath('.//span[@class="t2"]/a/text()').extract()[0]
            item['location'] = x.xpath('.//span[@class="t3"]/text()').extract()[0]
            item['money'] = x.xpath('.//span[@class="t4"]/text()').extract()        
            items.append(item)
        return items'''

#若将 item = FiveoneJobItem()放置外面，得到的回事重复数据


            
    
