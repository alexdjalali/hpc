import json
from glob import glob
from pymongo import Connection

########################################################################

# Mongo DB connection & collection
COLLECTION = Connection(host='localhost', port=27017).cspan

# Transcript directory
DIR = '/Users/ajdjalali/Desktop/cspan/tagged_transcripts/*.json'

########################################################################

for filename in glob(DIR):
    with open(filename) as fp:
        doc = json.load(fp)

    COLLECTION.house_hearings.save(doc)
