import json
from hpc import MongoConnection
from nltk import word_tokenize
from collections import defaultdict

COLLECTION = MongoConnection('localhost', 27017).query_db()
PARSED_LEXICON = 'parsed_lexicon.json'

d = defaultdict(int)

for document in COLLECTION:
    for speech in document['transcript']:
        tokens = word_tokenize(speech['pos'].lower())
        for token in tokens:
            d[token] += 1
    print "Entries written"

with open(PARSED_LEXICON, 'wb') as fp:
        json.dump(d, fp)

