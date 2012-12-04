from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from cspan_crawler.items import CSPANItem


def party_getter(list1):
    party = list1.split(']')
    if len(party) > 1:
        return party[0].strip('[')
    else:
        return None

def state_getter(list1):
    state = list1.split(']')
    if len(state) > 1:
        return state[1].strip()
    else:
        return None

def actual_time_getter(list1):
    actual_time = list1.split('(')
    if len(actual_time) > 1:
        return actual_time[0].strip()
    else:
        return None

def transcript_time_getter(list1):
    transcript_time = list1.split('(')
    if len(transcript_time) > 1:
        return transcript_time[1].strip(')')
    else:
        return None

class CSPAN(CrawlSpider):
    name = "cspan"
    allowed_domains = ["cspan.org", "c-spanvideo.org"]

    start_urls = [
            "http://www.c-spanvideo.org/videoLibrary/ajax/ajax-search-results.php?action=program&init=true&page=%s&sort=datereverse&fresh_load=1&query=format:%%22House+Proceeding%%22" %(x,) for x in range(0, 1071)
        ]

    rules = (
            Rule(SgmlLinkExtractor(allow=('program', )), callback='parse1'),
        )

    def parse1(self, response):
        item = CSPANItem()
        hxs = HtmlXPathSelector(response)

        transcript_id = "".join(hxs.select('//p[@class="eventlink meta"]/a/@href').extract())
        details = hxs.select('//div[@id="info"]')[0]
        people = hxs.select('//div[@class="details"]')

        item['program_id'] = " ".join(details.select('div/dl/dd[1]/text()').extract()).strip()
        item['category'] = " ".join(details.select('div/dl/dd[2]/a/text()').extract()).strip()
        item['format'] = " ".join(details.select('div/dl/dd[3]/a/text()').extract()).strip()
        item['location'] = " ".join(details.select('div/dl/dd[4]/text()').extract()).strip()
        item['date_aired'] = " ".join(details.select('div/dl/dd[5]/text()').extract()).strip()
        item['airing_details'] = " ".join(hxs.select('//div[@id="airingDetails"]/dl/dd/strong/text()').extract()).strip()
        item['people'] = []

        for person in people:
            name = " ".join(person.select('h3/a/text()').extract()).strip().split(',')
            item['people'].append({
                                    'name': {
                                             'first': name[1],
                                             'last': name[0],
                                    },
                                    'office': " ".join(person.select('span/i/text()').extract()).strip(),
                                    'party': party_getter(" ".join(person.select('text()').extract()).strip()),
                                    'state': state_getter(" ".join(person.select('text()').extract()).strip()),
            })

        item['tags'] = hxs.select('//div[@id="tags"]/div/ul/li/a/text()').extract()
        item['run_time'] = " ".join(hxs.select('//p[@class="meta bordered"]/span/a/text()').extract()).strip()
        item['source'] = unicode('c-spanvideo.org')
        item['url'] = response.url

        request = Request(url="http://www.c-spanvideo.org/" + transcript_id, callback=self.parse2)
        request.meta['item'] = item

        return request

    def parse2(self, response):
        hxs = HtmlXPathSelector(response)
        oldeventid = "".join(hxs.select('//div[@id="videoWrapper"]/@rel').extract())
        crid = "".join(hxs.select('//div[@id="leftPanelIndex"]/ul/li[1]/@rel').extract())

        request = Request(url="http://www.c-spanvideo.org/videoLibrary/transcript/ajax-transcript.php?action=congressRecords&crid=%s&oldeventid=%s" %(crid, oldeventid), callback=self.parse3)
        request.meta['item'] = response.meta['item']

        return request

    def parse3(self, response):
        item = response.meta['item']
        hxs = HtmlXPathSelector(response)

        turns = hxs.select('//li[@class="transcript_chunk speaker_chunk app_chunk"]')
        item['transcript'] = []

        for turn in turns:
            speaker = " ".join(turn.select('h2/text()').extract()).split(',')[0].split(' ')
            item['transcript'].append({
                                        'speaker': {
                                                    'name': {
                                                            'first': speaker[0],
                                                            'last': speaker[1],
                                                    },
                                        },
                                        'time': {
                                                    'transcript_time': transcript_time_getter(" ".join(turn.select('h3/text()').extract())),
                                                    'actual_time': actual_time_getter(" ".join(turn.select('h3/text()').extract())),
                                        },
                                        'speech': " ".join(turn.select('div[@class="trans_text"]/p/text()').extract())
            })

        return item
