import csv
import re

class CSVWriter():

    FIELDS = (
                'program_id',
                'category',
                'location',
                'date_aired',
                'speaker_name',
                'speaker_office',
                'speaker_party',
                'speaker_state',
                'speaker_district',
            )

    def __init__(self):
        pass

    def csv_writer(self, filename):
        return csv.writer(open(filename, 'wb'))

    @property
    def det_fields(self):

        fields = (
                    'determiner',
                    'det_cat',
                    'head_noun',
                    'noun_cat',
                )

        return self.FIELDS + fields

    @property
    def verb_fields(self):

        fields = (
                    'noun',
                    'noun_cat',
                    'verb_token',
                    'verb_type',
                    'verb_cat',
                    'presuppositional_behavior',
                    'factivity',
                )

        return self.FIELDS + fields

    def get_token(self, token):
        parser = re.compile('(?:([A-Za-z]+)_(\S+)\s*)', re.UNICODE | re.VERBOSE)
        d = {}
        if token != "":
            match = parser.match(token)
            # Clean token, not token's syn-cat
            d['token'] = match.group(1).lower()
            d['cat'] = match.group(2)
        else:
            d['token'] = 'NULL'
            d['cat'] = 'NULL'
        return d

    def get_row(self, transcript, speech):
        # Transcript data
        row = (
                transcript.program_id,
                transcript.category,
                transcript.location,
                transcript.date_aired,
            )

        # Speaker data
        row = row + (
                        speech.speaker.name,
                        speech.speaker.office,
                        speech.speaker.party,
                        speech.speaker.state,
                        speech.speaker.district,
            )
        return row
