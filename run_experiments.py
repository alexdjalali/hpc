import re
import csv
from model.corpus import Corpus


# Regular expresisons
DET_RE = r'((([A-Za-z]+?)_(DT) ([Rr]epublican[s]{0,1}_[A-Z]+?|[Dd]emocrat[s]{0,1}_[A-Z]+?)) .+?\.)'

############################################################################

if __name__ == "__main__":
    c = 0
    #WRITER.writerow(FIELDS)
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
                        fields = Fields(transcript, speech)
                        row = fields.get_transcript_data
                        row = row + fields.get_speaker_data
                        row = row + (
                                    syntactic_category,
                                    determiner,
                                    data_point,
                                    full_sentence,
                                )
                        #WRITER.writerow(row)
                        c += 1
                        print "Row #%s successfully written to %s" %(c, CSV,)
                    except:
                        pass

