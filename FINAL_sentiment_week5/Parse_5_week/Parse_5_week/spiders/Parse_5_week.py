#from scrapy.spider import BaseSpider
from scrapy.spiders import Spider
#from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
import codecs 

class Parse_5_week(Spider):
    name = "Parse_5_week"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Bias-variance_tradeoff",]

    def parse(self, response):
        hxs = Selector(response)
        result = hxs.xpath('//h1/text()').extract()
        print(result) 
        with codecs.open('results.txt', 'w', 'utf-8') as output_file:
	    if sys.version_info >= (3, 0):
        	''' python 3 '''
        	print(s, end="", file=output_file)
    	    else:
        	''' python 2 '''	            
		print >> output_file, u'\n'.join(result)
