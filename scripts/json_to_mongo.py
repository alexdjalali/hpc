import json
from glob import glob
from pymongo import Connection

DB = Connection(host='localhost', port=27017).cspan

DIR = '/Users/ajdjalali/Desktop/hpc/cspan_spider/tagged_transcripts/*.json'

########################################################################

for filename in glob(DIR):
    with open(filename) as fp:
        doc = json.load(fp)

    DB.house_proceedings.save(doc)
