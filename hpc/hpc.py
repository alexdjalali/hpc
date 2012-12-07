import re
import time
from urlparse import urlparse
from pymongo import Connection
from pymongo.database import Database
from pymongo.collection import Collection
from datetime import datetime, timedelta

############################################################################

# Mongo settings
HOST = 'localhost'
PORT = 27017
DB = 'cspan'
COLLECTION = 'house_hearings'

# Regular expressions
TIME = r'([0-9]+) hours{0,1}, ([0-9]+) minutes{0,1}|([0-9]+) minutes{0,1}'

# Political parties
REPUBLICAN = 'R'
DEMOCRAT = 'D'
INDEPENDENT = 'I'
PARTIES = [REPUBLICAN, DEMOCRAT, INDEPENDENT]

# States of Representation
STATES = [
            "Alaska",
            "American Samoa",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Guam",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Northern Marianas Islands",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Puerto Rico",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Virgin Islands",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming",
    ]

############################################################################

class MongoConnection:

    def __init__(self, host, port):
        self.connection = Connection(host, port)

    def __db(self):
        return Database(self.connection, DB)

    def __collection(self):
        return Collection(self.__db(), COLLECTION)

    def query_collection(self, limit=2707):
        return self.__collection().find(timeout=False).limit(limit)

############################################################################

class Corpus:

    def __init__(self, cursor):
        self.cursor = cursor

    @property
    def get_transcripts(self):
        for document in self.cursor:
            yield Transcript(document)

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
        # Get list of speakers
        self.people = [Person(person) for person in self.document['people']]
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

############################################################################

class Person:

    def __init__(self, person, **kwargs):
        self.person = person
        # Get name
        self.first_name = self.person['name']['first']
        self.last_name = self.person['name']['last']
        self.full_name = self.first_name + " " + self.last_name
        # Get political office
        self.office = self.person['office']
        # Validate political party
        self.party = self.__validator(self.person['party'])
        # Validate state of representation
        self.state = self.__validator(self.person['state'])

    def __validator(self, validation):
        if validation in STATES or validation in PARTIES:
            return validation
        else:
            return None

############################################################################

class Speech:

    def __init__(self, speech, **kwargs):
        self.speech = speech
        # Get speaker name
        self.speaker_first_name = self.speech['speaker']['name']['first']
        self.speaker_last_name = self.speech['speaker']['name']['last']
        self.speaker_full_name = self.speaker_first_name + " " + self.speaker_last_name
        # Get and parse actual time of speech
        try:
            self.actual_time = datetime.strptime(self.speech['time']['actual_time'], "%I:%M:%S %p")
            self.actual_time = self.actual_time.replace(year=kwargs['date_aired'].year,
                    month=kwargs['date_aired'].month, day=kwargs['date_aired'].day)
        except:
            self.actual_time = None
        # Get and parse time in transcript of speech and convert to seconds
        try:
            self.transcript_time = time.strptime(self.speech['time']['transcript_time'], "%H:%M:%S")
            self.transcript_time = timedelta(hours=self.transcript_time.tm_hour, minutes=self.transcript_time.tm_min,
                    seconds=self.transcript_time.tm_sec).seconds
        except ValueError:
            self.transcript_time = time.strptime(self.speech['time']['transcript_time'], "%M:%S")
            self.transcript_time = timedelta(minutes=self.transcript_time.tm_min,
                    seconds=self.transcript_time.tm_sec).seconds
        except:
            self.transcript_time = None
        # Get raw speech
        self.raw_speech = self.speech['speech']
        # Get POS tagged speech
        self.pos_speech = self.speech['pos']

