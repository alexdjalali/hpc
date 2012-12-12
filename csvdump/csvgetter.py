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
                'determiner',
                'det_cat',
                'head_noun',
                'noun_cat',
            )

    def __init__(self):
        pass

    def csv_writer(self, filename):
        return csv.writer(open(filename, 'wb'))

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

    def token_cleaner(self, token):
        parser = re.compile('([A-Za-z]+)_(\S+)', re.UNICODE | re.VERBOSE)
        if token != "":
            match = parser.match(token)
            # Clean token, not token syn-cat
            return match.group(1).lower(), match.group(2)
        else:
            return 'NULL', 'NULL'

