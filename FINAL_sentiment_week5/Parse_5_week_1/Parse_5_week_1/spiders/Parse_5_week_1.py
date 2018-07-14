from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request
import codecs 

class Parse_5_week_1(CrawlSpider):
    name = "Parse_5_week_1"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Category:Machine_learning_algorithms",]

    rules = (
        Rule(LxmlLinkExtractor(restrict_xpaths=('//div[@id="mw-pages"]//a'))),
        Rule(LxmlLinkExtractor(allow=("https://en.wikipedia.org/wiki/Category:Machine_learning_algorithms")), callback='parse_item'),  
     )

    def parse_item(self, response):
        hxs = Selector(response)
        result = hxs.xpath('//div[@id="mw-pages"]/div/div/div/ul/li/a/text()').extract()
        print hxs.xpath('//h1/text()').extract()
        print result 
        with codecs.open('results_1.txt', 'w', 'utf-8') as output_file:
	    if sys.version_info >= (3, 0):
        	''' python 3 '''
        	print(s, end="", file=output_file)
    	    else:
        	''' python 2 '''            
		print >> output_file, u'\n'.join(result)
