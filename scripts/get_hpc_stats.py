import json

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

print "# of raw tokens: %s" %(str(RAW_TOKEN_COUNT),)
print "# of parsed tokens: %s" %(str(PARSED_TOKEN_COUNT),)
print "Raw vocabulary size: %s" %(str(RAW_VOCAB_COUNT),)
print "Parsed vocabulary size: %s" %(str(PARSED_VOCAB_COUNT),)


