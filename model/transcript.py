from speech import Speech

class Transcript:

    def __init__(self, document):
        self.document = document
        self.program_id = self.document['program_id']
        self.category = self.document['category']
        self.format = self.document['format']
        self.location = self.document['location']
        self.date_aired = self.document['date_aired']
        self.airing_details = self.document['airing_details']
        self.tags = self.document['tags']
        self.runtime = self.document['run_time']
        self.source = self.document['source']
        self.url = self.document['url']
        self.speeches = [Speech(speech) for speech in self.document['transcript']]

    def __str__(self):
        return "Transcript ID: %s" %(self.program_id)
