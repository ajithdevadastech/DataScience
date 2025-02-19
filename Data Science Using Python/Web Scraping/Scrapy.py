import scrapy
from scrapy.crawler import CrawlerRunner # To Run our spider

#2. Setting up crochet
#To run spiders smoothly scrapy uses twisted library internally. But the problem is the twisted reactor can only be instantiated once. Therefore, crochet is used so that we can test our spider easily.

import crochet
# from crochet import setup, run_in_reactor
# setup()
crochet.setup()

"""
3. Inspecting the webpage
- Goto http://books.toscrape.com
- Inspect the first title of the book
"""

#4. Building the Spider

class BookSpider(scrapy.Spider):
    name = 'BookSpider'  # used to invoke spider

    # Used to start the requests
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html',
                  'http://books.toscrape.com/catalogue/page-2.html',
                  'http://books.toscrape.com/catalogue/page-3.html']

    ''' 
    Invoked by scrapy engine for every url
    Here we will use selectors to scrap the website
    '''

    def parse(self, response):
        book_list = response.css('article.product_pod>h3>a::attr(title)').getall()

        for i in book_list:
            print(i)

#5. Crawling with spider

process = CrawlerRunner({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
})

@crochet.wait_for(10.0)
def run_spider():
    return process.crawl(BookSpider)

run_spider()



