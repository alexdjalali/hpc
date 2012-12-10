import re
from model.corpus import Corpus
#from csvdump.unicsvwriter import UnicodeWriter

############################################################################

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
        )

# Regular expresisons
DET_RE = r'(([A-Za-z]+?)_(DT) ([Rr]epublicans_[A-Z]+?|[Dd]emocrats_[A-Z]+?)) .+?\.'

############################################################################

def get_speaker(transcript, speech):
    for person in transcript.people:
        if speech.speaker_first_name in person.first_name and speech.speaker_last_name in person.last_name:
            return person
        else:
            return False

############################################################################

if __name__ == "__main__":
    transcripts = Corpus().get_transcripts
    for transcript in transcripts:
        for speech in transcript.speeches:
            matches = re.findall(DET_RE, speech.pos_speech)
            if matches:
                speaker = get_speaker(transcript, speech)
                for match in matches:
                    try:
                        date_aired = unicode(transcript.date_aired.month) + ";" + unicode(transcript.date_aired.day) + ";" + unicode(transcript.date_aired.year)
                        syntactic_category = match[2]
                        determiner = match[1].lower(),
                        data_point = re.match(r'(.+?)_[A-Z]+?', match[3]).group(1).lower()
                        fields = (
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
                                )
                        print fields
                    except:
                        pass
        print transcript.program_id + " " + "complete"



