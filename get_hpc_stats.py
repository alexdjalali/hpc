import json
import datetime
from hpc import MongoConnection

COLLECTION = MongoConnection('localhost', 27017).query_db()

RAW_LEXICON = json.load(open('/Users/ajdjalali/Desktop/hpc/json/raw_lexicon.json'))
PARSED_LEXICON = json.load(open('/Users/ajdjalali/Desktop/hpc/json/parsed_lexicon.json'))
SPEAKERS = json.load(open('/Users/ajdjalali/Desktop/hpc/json/speakers.json'))

VERBS = ['know', 'believe', 'say', 'think', 'hope', 'wish', 'mention',
            'tell', 'ask', 'promise', 'warn', 'request', 'order', 'accuse',
            'criticize', 'blame', 'regret', 'understand', 'surprise',
            'begin', 'stop', 'stop', 'continue', 'manage', 'avoid',
            'force', 'prevent', 'hesitate', 'seem',
        ]

DETERMINERS = ['this', 'that', 'these', 'those', 'the']

RAW_TOKEN_COUNT = sum(RAW_LEXICON.values())
PARSED_TOKEN_COUNT = sum(PARSED_LEXICON.values())
RAW_VOCAB_COUNT = len(RAW_LEXICON.keys())
PARSED_VOCAB_COUNT = len(PARSED_LEXICON.keys())
SPEAKER_COUNT = len(SPEAKERS.keys())

print "House Proceedings Corpus (HPC) stats"
print str(datetime.datetime.now())
print "##################################\n"
print "Transcript count: 2707"
print "Speaker count: %s" %(SPEAKER_COUNT,)
print "Raw token count: %s" %(str(RAW_TOKEN_COUNT),)
print "Parsed token count: %s" %(str(PARSED_TOKEN_COUNT),)
print "Raw vocabulary count: %s" %(str(RAW_VOCAB_COUNT),)
print "Parsed vocabulary count: %s" %(str(PARSED_VOCAB_COUNT),)




