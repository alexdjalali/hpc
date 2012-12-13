import re
from model.corpus import Corpus
from csvdump.csvgetter import CSVWriter

CSV_FILE = 'csvdump/det_exp.csv'
CSV = CSVWriter()
CSV_WRITER = CSV.csv_writer(CSV_FILE)

# Regular expressions
DETEXP_RE = re.compile(r"""
                        ([A-Za-z]+?_DT\s+)?              # Zero or one DT phrases with trailing space.
                        ((?:\S+_(?:JJ|RB|VBG)\S*\s+)*)   # Zero or more modifiers.
                        (
                        [Rr]epublican[s]{0,1}_N\S*       # Republicans with any tag.
                        |                                # or
                        [Dd]emocrat[s]{0,1}_N\S*         # Democrats with any tag.
                        )
                        """, re.VERBOSE | re.UNICODE | re.DOTALL | re.M)

############################################################################

if __name__ == "__main__":
    c = 0
    transcripts = Corpus().get_transcripts
    CSV_WRITER.writerow(CSV.FIELDS)
    for transcript in transcripts:
        for speech in transcript.speeches:
            matches = DETEXP_RE.findall(speech.pos_speech)
            if matches:
                for match in matches:
                    try:
                        row = CSV.get_row(transcript, speech)
                        row += CSV.get_token(match[0]) + CSV.get_token(match[len(match)-1])
                        CSV_WRITER.writerow(row)
                        c += 1
                        print "Row #%s successfully written" %(c,)
                    except:
                        pass
