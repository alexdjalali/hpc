import csv
import re

class CSVWriter():

    FIELDS = (
                'program_id',
                'category',
                'location',
                'date_aired',
                'speaker_name',
                'speaker_party',
                'speaker_state',
                'speaker_office',
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
        return self.FIELD + fields

    @property
    def verb_fields(self):

        fields = (
                    'noun',
                    'noun_cat',
                    'verb_token',
                    'verb_type',
                    'verb_cat',
                    'factivity',
                    'presuppositional_behavior',
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
        for person in transcript.people:
            if speech.speaker_first_name in person.first_name and speech.speaker_last_name in person.last_name:

                # Transcript data
                row = (
                        transcript.program_id,
                        transcript.category,
                        transcript.location,
                        unicode(transcript.date_aired.ctime()),
            )
                # Speaker data
                row = row + (
                                person.full_name,
                                person.party,
                                person.state,
                                person.office,
                    )
                return row
            else:
                return False
