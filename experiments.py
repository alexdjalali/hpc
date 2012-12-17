from model.corpus import Corpus
from csvdump.csvgetter import CSVWriter
from regexes.regexes import RegularExpressions

CSV_FILE = 'csvdump/det_exp.csv'
CSV = CSVWriter()
CSV_WRITER = CSV.csv_writer(CSV_FILE)

DET_RE = RegularExpressions().det_regex
VERB_RE = RegularExpressions().verb_regex

############################################################################

if __name__ == "__main__":
    c = 0
    transcripts = Corpus().get_transcripts
    CSV_WRITER.writerow(CSV.FIELDS)
    for transcript in transcripts:
        for speech in transcript.speeches:
            matches = VERB_RE.findall(speech.pos_speech)
            if matches:
                for match in matches:
                    print match
                    #try:
                        #row = CSV.get_row(transcript, speech)
                        #row += CSV.get_token(match[0]) + CSV.get_token(match[len(match)-1])
                        #CSV_WRITER.writerow(row)
                        #c += 1
                        #print "Row #%s successfully written" %(c,)
                    #except:
                        #pass
