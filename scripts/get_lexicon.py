import json
from hpc import MongoConnection
from nltk import word_tokenize
from collections import defaultdict

collection = MongoConnection('localhost', 27017).query_db()

d = defaultdict(int)

for document in collection:
    for speech in document['transcript']:
        tokens = word_tokenize(speech['pos'].lower())
        for token in tokens:
            d[token] += 1
    print "Entries written"

with open('data_parsed.json', 'wb') as fp:
        json.dump(d, fp)

