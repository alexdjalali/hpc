from model.corpus import Corpus
from csvdump.csvgetter import CSVWriter
from regexes.regexes import RegularExpressions
#from lexicalresources.typegetter import TypeGetter

CSV_FILE = 'csvdump/det_exp_revised.csv'
CSV = CSVWriter()
CSV_WRITER = CSV.csv_writer(CSV_FILE)

#Regular expressions. (Experiments rely on matching groups of regular expressions.)
DET_RE = RegularExpressions().det_regex
VERB_RE = RegularExpressions().verb_regex

############################################################################

if __name__ == "__main__":
    c = 0
    transcripts = Corpus().get_transcripts
    # Determiner experiment
    CSV_WRITER.writerow(CSV.det_fields)
    # Verb experiment
    #CSV_WRITER.writerow(CSV.verb_fields)
    for transcript in transcripts:
        for speech in transcript.speeches:
            # Determiner experiment
            matches = DET_RE.findall(speech.pos_speech)
            # Verb experiment
            #matches = VERB_RE.findall(speech.pos_speech)
            if matches:
                for match in matches:
                    # Determiner experiment
                    determiner_token = CSV.get_token(match[0])
                    noun_token = CSV.get_token(match[2])
                    # Verb experiment
                    #noun_token = CSV.get_token(match[2])
                    #verb_token = CSV.get_token(match[4])
                    #verb_type = TypeGetter(verb_token['token']).type
                    #verb_tags = TypeGetter(verb_token['token']).tags

                    try:
                        # Fix. Determiner experiment
                        row = CSV.get_row(transcript, speech)
                        row += (
                                    determiner_token['token'],
                                    determiner_token['cat'],
                                    noun_token['token'],
                                    noun_token['cat'],
                            )
                        CSV_WRITER.writerow(row)
                        c += 1
                        print "Row #%s successfully written" %(c,)
                    #try:
                        ## Verb experiment
                        #row = CSV.get_row(transcript, speech)
                        ## Fix. verb_tags tied to structure of tags
                        #row += (
                                    #noun_token['token'],
                                    #noun_token['cat'],
                                    #verb_token['token'],
                                    #verb_type,
                                    #verb_token['cat'],
                                    #verb_tags[0],
                                    #verb_tags[1],
                            #)
                        #CSV_WRITER.writerow(row)
                        #c += 1
                        #print "Row #%s successfully written" %(c,)
                    except:
                        pass
