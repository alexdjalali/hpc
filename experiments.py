# coding=UTF
import re
from model.corpus import Corpus
from csvdump.csvgetter import CSVWriter

# CSV WRITER
CSV_FILE = 'csvdump/test.csv'
CSV = CSVWriter()
CSV_WRITER = CSV.csv_writer(CSV_FILE)

PARTY_RE = re.compile(r'(?:[A-Za-z]+?_DT\s+)?(?:[Rr]epublican[s]{0,1}_\S+|[Dd]emocrat[s]{0,1}_\S+)│.+?_\.', re.VERBOSE | re.UNICODE | re.DOTALL | re.M)
DET_RE = r'((([A-Za-z]+?)_(DT) ([Rr]epublican[s]{0,1}_[A-Z]+?|[Dd]emocrat[s]{0,1}_[A-Z]+?)) .+?\.)'

############################################################################

if __name__ == "__main__":
    c = 0
    transcripts = Corpus().get_transcripts
    CSV_WRITER.writerow(CSV.FIELDS)
    for transcript in transcripts:
        for speech in transcript.speeches:
            matches = re.findall(DET_RE, speech.pos_speech)
            print matches
            #if matches:
                #for match in matches:
                    #syntactic_category = match[3]
                    #determiner = match[2].lower()
                    #data_point = re.match(r'(.+?)_[A-Z]+?', match[4]).group(1).lower()
                    #full_sentence = match[0]
                    #try:
                        #row = CSV.get_partialdata(transcript, speech)
                        #row = row + (
                                    #syntactic_category,
                                    #determiner,
                                    #data_point,
                                    #full_sentence,
                                #)
                        #CSV_WRITER.writerow(row)
                        #c += 1
                        #print "Row #%s successfully written %s" %(c, CSV)
                    #except:
                        #pass
