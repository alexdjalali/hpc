import json
import datetime

########################### JSON ##############################################

raw_lexicon = json.load(open('/Users/ajdjalali/Desktop/hpc/json/raw_lexicon.json'))
parsed_lexicon = json.load(open('/Users/ajdjalali/Desktop/hpc/json/parsed_lexicon.json'))
speakers = json.load(open('/Users/ajdjalali/Desktop/hpc/json/speakers.json'))

########################### COUNTS ##############################################

raw_token_count = sum(raw_lexicon.values())
parsed_token_count = sum(parsed_lexicon.values())
raw_vocab_count = len(raw_lexicon.keys())
parsed_vocab_count = len(parsed_lexicon.keys())
speaker_count = len(speakers.keys())

##########################################################################


if __name__ == "__main__":

    print "House Proceedings Corpus (HPC) stats"
    print str(datetime.datetime.now())
    print "##################################\n"
    print "Transcript count: 2707"
    print "Speaker count: %s" %(speaker_count,)
    print "Raw token count: %s" %(str(raw_token_count),)
    print "Parsed token count: %s" %(str(parsed_token_count),)
    print "Raw vocabulary count: %s" %(str(raw_vocab_count),)
    print "Parsed vocabulary count: %s" %(str(parsed_vocab_count),)
