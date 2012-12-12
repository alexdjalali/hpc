import csv

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
                'head_noun',
                'full_sentence'
            )

    def __init__(self):
        pass

    def csv_writer(self, filename):
        return csv.writer(open(filename, 'wb'))

    def get_data(self, transcript, speech):
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
