import time
from datetime import datetime, timedelta

############################################################################

class Speech:

    def __init__(self, speech, **kwargs):
        self.speech = speech
        # Get speaker name
        self.speaker_first_name = self.speech['speaker']['name']['first'].strip()
        self.speaker_last_name = self.speech['speaker']['name']['last'].strip()
        self.speaker_full_name = self.speaker_first_name + " " + self.speaker_last_name
        # Get and parse actual time of speech
        try:
            self.actual_time = datetime.strptime(self.speech['time']['actual_time'], "%I:%M:%S %p")
            self.actual_time = self.actual_time.replace(year=kwargs['date_aired'].year,
                    month=kwargs['date_aired'].month, day=kwargs['date_aired'].day)
        except:
            self.actual_time = None
        # Get and parse time in transcript of speech and convert to seconds
        try:
            self.transcript_time = time.strptime(self.speech['time']['transcript_time'], "%H:%M:%S")
            self.transcript_time = timedelta(hours=self.transcript_time.tm_hour, minutes=self.transcript_time.tm_min,
                    seconds=self.transcript_time.tm_sec).seconds
        except ValueError:
            self.transcript_time = time.strptime(self.speech['time']['transcript_time'], "%M:%S")
            self.transcript_time = timedelta(minutes=self.transcript_time.tm_min,
                    seconds=self.transcript_time.tm_sec).seconds
        except:
            self.transcript_time = None
        # Get raw speech
        self.raw_speech = self.speech['speech']
        # Get POS tagged speech
        self.pos_speech = self.speech['pos']
