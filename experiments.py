import re
from model.corpus import Corpus
from csvdump.csvgetter import CSVWriter

CSV_FILE = 'csvdump/det_exp.csv'
CSV = CSVWriter()
CSV_WRITER = CSV.csv_writer(CSV_FILE)

# Regular expressions
PARTY_RE = re.compile(r"""
                      ([A-Za-z]+?_DT\s+)?        # Zero or one DT phrases with trailing space.
                      (
                      [Rr]epublican[s]{0,1}_\S+    # Republicans with any tag.
                      |
                      [Dd]emocrat[s]{0,1}_\S+      # Democrats with any tag.
                      )
                      """, re.VERBOSE | re.UNICODE | re.DOTALL | re.M)

############################################################################

if __name__ == "__main__":
    c = 0
    transcripts = Corpus().get_transcripts
    CSV_WRITER.writerow(CSV.FIELDS)
    for transcript in transcripts:
        for speech in transcript.speeches:
            matches = PARTY_RE.findall(speech.pos_speech)
            if matches:
                for match in matches:
                    try:
                        row = CSV.get_row(transcript, speech) + CSV.token_cleaner(match[0]) + CSV.token_cleaner(match[1])
                        CSV_WRITER.writerow(row)
                        c += 1
                        print "Row #%s successfully written to %s" %(c, CSV_FILE)
                    except:
                        pass

