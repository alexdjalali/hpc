from person import Person

class Speech:

    def __init__(self, speech, **kwargs):
        self.speech = speech
        self.speaker = Person(self.speech['speaker'])
        self.actual_time = self.speech['time']['actual_time']
        self.transcript_time = self.speech['time']['transcript_time']
        self.raw_speech = self.speech['speech']
        self.pos_speech = self.speech['pos']


    def __str__(self):
        return self.speaker
