import json
from hpc import MongoConnection
from collections import defaultdict

COLLECTION = MongoConnection('localhost', 27017).query_db()
SPEAKERS = 'speakers.json'

d = defaultdict(int)

for document in COLLECTION:
    for speaker in document['people']:
        d[speaker['name']['first'] + " " + speaker['name']['last']] += 1
    print "Entries written"

with open(SPEAKERS, 'wb') as fp:
    json.dump(d, fp)
