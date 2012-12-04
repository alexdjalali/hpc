from scrapy.item import Item, Field

class CSPANItem(Item):
    program_id = Field()
    category = Field()
    format = Field()
    location = Field()
    date_aired = Field()
    airing_details = Field()
    people = Field()
    tags = Field()
    run_time = Field()
    source = Field()
    url = Field()
    transcript = Field()
