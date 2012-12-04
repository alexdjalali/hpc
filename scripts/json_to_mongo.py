import json
from glob import glob
from pymongo import Connection

db = Connection(host='localhost', port=27017).cspan

for filename in glob('/Users/ajdjalali/Desktop/cspan/tagged_transcripts/*.json'):
    with open(filename) as fp:
        doc = json.load(fp)

    db.house_hearings.save(doc)
