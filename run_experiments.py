import re
import csv
from model.corpus import Corpus

############################################################################

# CSV File
CSV = 'csvdump/det_experiment.csv'

# CSV fields
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

# CSV writer
WRITER = csv.writer(open(CSV, 'wb'))

# Regular expresisons
DET_RE = r'((([A-Za-z]+?)_(DT) ([Rr]epublican[s]{0,1}_[A-Z]+?|[Dd]emocrat[s]{0,1}_[A-Z]+?)) .+?\.)'

############################################################################

def get_transcript_data(transcript):
    date_aired = unicode(transcript.date_aired.ctime())
    row = (
                transcript.program_id,
                transcript.category,
                transcript.location,
                date_aired,
        )
    return row

def get_speaker_data(transcript, speech):
    for person in transcript.people:
        if speech.speaker_first_name in person.first_name and speech.speaker_last_name in person.last_name:
            row = (
                    person.full_name,
                    person.party,
                    person.state,
                    person.office,
                )
            return row
        else:
            return False

############################################################################

if __name__ == "__main__":
    c = 0
    WRITER.writerow(FIELDS)
    transcripts = Corpus().get_transcripts
    for transcript in transcripts:
        for speech in transcript.speeches:
            matches = re.findall(DET_RE, speech.pos_speech)
            if matches:
                for match in matches:
                    syntactic_category = match[3]
                    determiner = match[2].lower()
                    data_point = re.match(r'(.+?)_[A-Z]+?', match[4]).group(1).lower()
                    full_sentence = match[0]
                    try:
                        row = get_transcript_data(transcript)
                        row = row + get_speaker_data(transcript, speech)
                        row = row + (
                                    syntactic_category,
                                    determiner,
                                    data_point,
                                    full_sentence,
                                )
                        WRITER.writerow(row)
                        c += 1
                        print "Row #%s successfully written to %s" %(c, CSV,)
                    except:
                        pass

