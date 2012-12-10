import re
import csv
from model.corpus import Corpus

CSV = 'csvdump/det_experiment.csv'

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

WRITER = csv.writer(open(CSV, 'wb'))

DET_RE = r'((([A-Za-z]+?)_(DT) ([Rr]epublican[s]{0,1}_[A-Z]+?|[Dd]emocrat[s]{0,1}_[A-Z]+?)) .+?\.)'

############################################################################

def get_speaker(transcript, speech):
    for person in transcript.people:
        if speech.speaker_first_name in person.first_name and speech.speaker_last_name in person.last_name:
            return person
        else:
            return False

############################################################################

if __name__ == "__main__":
    WRITER.writerow(FIELDS)
    transcripts = Corpus().get_transcripts
    for transcript in transcripts:
        for speech in transcript.speeches:
            matches = re.findall(DET_RE, speech.pos_speech)
            if matches:
                speaker = get_speaker(transcript, speech)
                for match in matches:
                    try:
                        date_aired = unicode(transcript.date_aired.month) + ";" + unicode(transcript.date_aired.day) + ";" + unicode(transcript.date_aired.year)
                        transcript_time = unicode(speech.transcript_time)
                        syntactic_category = match[3]
                        determiner = match[2].lower()
                        data_point = re.match(r'(.+?)_[A-Z]+?', match[4]).group(1).lower()
                        full_sentence = match[0]
                        row = (
                                    transcript.program_id,
                                    transcript.category,
                                    transcript.location,
                                    date_aired,
                                    speaker.full_name,
                                    speaker.party,
                                    speaker.state,
                                    speaker.office,
                                    syntactic_category,
                                    determiner,
                                    data_point,
                                    full_sentence,
                                )
                        WRITER.writerow(row)
                        print "Row successfully written to %s" %(CSV,)
                    except:
                        pass
        print "Transcript #" + transcript.program_id + " successfully written to %s" %(CSV,)

