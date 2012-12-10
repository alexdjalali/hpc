from transcript import Transcript
from mongo_connection import MongoConnection

############################################################################

class Corpus:

    def __init__(self):
        self.cursor = MongoConnection().query_collection()

    @property
    def get_transcripts(self):
        for document in self.cursor:
            yield Transcript(document)
