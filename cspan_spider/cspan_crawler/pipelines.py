import json
from scrapy.exceptions import DropItem


class JsonWriterPipeline(object):

    c = 0

    def process_item(self, item, spider):
        file = open('transcripts/house_hearing_transcript%s.json' %(self.c, ), 'wb')
        line = json.dumps(dict(item))
        file.write(line)
        self.c += 1
        return item

class DropItemPipeline(object):

    def process_item(self, item, spider):
        if item['transcript']:
            return item
        else:
            raise DropItem("No transcript.")
