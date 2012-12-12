import csv

class CSVWriter():

    CSV = 'csvdump/det_experiment.csv'

    WRITER = csv.writer(open(CSV, 'wb'))

    FIELDS = (
                'program_id',
                'category',
                'location',
                'date_aired',
                'speaker_name',
                'speaker_party',
                'speaker_state',
                'speaker_office',
                'syntactic_category',
                'determiner',
                'data_point',
                'full_sentence'
            )

    def __init__(self, transcript, speech):
        self.transcript = transcript
        self.speech = speech

    @property
    def get_transcript_data(self):
        date_aired = unicode(self.transcript.date_aired.ctime())
        row = (
                    self.transcript.program_id,
                    self.transcript.category,
                    self.transcript.location,
                    date_aired,
            )
        return row

    @property
    def get_speaker_data(self):
        for person in self.transcript.people:
            if self.speech.speaker_first_name in person.first_name and self.speech.speaker_last_name in person.last_name:
                row = (
                        person.full_name,
                        person.party,
                        person.state,
                        person.office,
                    )
                return row
            else:
                return False
