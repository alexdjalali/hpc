import json
from hpc import MongoConnection

COLLECTION = MongoConnection('localhost', 27017).query_db()

RAW_LEXICON = json.load(open('/Users/ajdjalali/Desktop/hpc/lexicons/raw_lexicon.json'))
PARSED_LEXICON = json.load(open('/Users/ajdjalali/Desktop/hpc/lexicons/parsed_lexicon.json'))

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

SPEAKERS = []
PARTIES = []
STATES = []

for document in COLLECTION:
    for speaker in document['people']:
        state = speaker['state']
        name = speaker['name']['first'] + " " + speaker['name']['last']
        party = speaker['party']
        if name not in SPEAKERS:
            SPEAKERS.append(name)
        if state not in STATES:
            STATES.append(state)
        if party not in PARTIES:
            PARTIES.append(party)

print PARTIES
print len(PARTIES)
print len(SPEAKERS)
print len(STATES)

#print "# of raw tokens: %s" %(str(RAW_TOKEN_COUNT),)
#print "# of parsed tokens: %s" %(str(PARSED_TOKEN_COUNT),)
#print "Raw vocabulary size: %s" %(str(RAW_VOCAB_COUNT),)
#print "Parsed vocabulary size: %s" %(str(PARSED_VOCAB_COUNT),)



