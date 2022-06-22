from scrapy import Item, Field

class ReviewItem(Item):
    product_name = Field()
    product_price = Field()
    review_title = Field()
    review_score = Field()
    review_content = Field()
