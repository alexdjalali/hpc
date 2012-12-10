import re
import csv
from model.corpus import Corpus

############################################################################

# CSV directory
CSV = 'csv/determiner_experiment.csv'

# Regular expresisons
det_re = r'.+?(([A-Za-z]+?)_DT (([Rr]epublican[s]*)_([A-Z]+?)|([Dd]emocrat[s]*)_([A-Z]+?))) .+?'

############################################################################

def to_csv(re, transcript):
    experiment_writer = csv.writer(open(CSV, 'wb'), delimiter=",", )

def get_speaker(transcript, speech):
    for person in transcript.people:
        if speech.speaker_first_name in person.first_name:
            return speech.speaker_first_name
        else:
            return False

if __name__ == "__main__":
    transcripts = Corpus().get_transcripts
    for transcript in transcripts:
        for speech in transcript.speeches:
            print re.findall(det_re, speech.pos_speech)
        print transcript.program_id + " " + "complete"
