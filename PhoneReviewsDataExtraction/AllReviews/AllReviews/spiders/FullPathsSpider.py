import time
import scrapy

class PathsSpider(scrapy.Spider):
    name = 'paths'
    start_urls = []
    for i in range(1, 31):
        p = f'https://www.emag.ro/telefoane-mobile/p{i}/c'
        start_urls.append(p)

    def parse(self, response):
        print(response, '--------------------')
        for product in response.css('div.js-products-container.card-collection.list-view-updated.show-me-a-grid div.card-v2-info'):
            #daca produsul are recenzii
            if product.css('div.star-rating-text'):
                product_reviews = product.css('div.star-rating-text span.visible-xs-inline-block::text').get().replace('(','').replace(')','')
                if product_reviews == 0:
                    print("reviews 0.................... :( ")
                else:
                    print("reviews not 0...")
                    product_link = product.css('a::attr(href)')
                    yield {"path": product_link.get().replace('https://www.emag.ro/',
                                                              'https://www.emag.ro/product-feedback/') + 'reviews/list'}
        time.sleep(5)



