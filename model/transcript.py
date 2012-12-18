import re
from speech import Speech
from urlparse import urlparse
from datetime import datetime, timedelta

# Regular expressions
TIME = r'([0-9]+) hours{0,1}, ([0-9]+) minutes{0,1}|([0-9]+) minutes{0,1}'

############################################################################

class Transcript:

    def __init__(self, document):
        self.document = document
        # Get unique CSPAN program ID
        self.program_id = self.document['program_id']
        # Get CSPAN video category
        self.category = self.document['category']
        self.format = self.document['format']
        # Get location of video shoot
        self.location = self.document['location']
        # Get and parse date of airing
        self.date_aired = datetime.strptime(self.document['date_aired'], '%b %d, %Y')
        # Get and parse airing details
        self.airing_details = datetime.strptime(re.sub(r' \(C[12]\)', '', self.document['airing_details']), '%b %d, %Y %H:%M')
        # Get list of video tags
        self.tags = self.document['tags']
        # Get run-time converted to seconds
        re_runtime = re.match(TIME, self.document['run_time'])
        if re_runtime.group(1) != None:
            self.run_time = timedelta(hours=int(re_runtime.group(1)), minutes=int(re_runtime.group(2)), seconds=0).seconds
        else:
            self.run_time = timedelta(hours=0, minutes=int(re_runtime.group(3)), seconds=0).seconds
        # Get source of transcript
        self.source = self.document['source']
        # Get and parse url of transcript
        self.url = urlparse(self.document['url'])
        # Get list of speeches
        self.speeches = [Speech(speech, date_aired=self.date_aired) for speech in self.document['transcript']]

    def __str__(self):
        return "Transcript ID: %s" %(self.program_id)
