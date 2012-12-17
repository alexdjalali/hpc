import json
from nltk.stem import WordNetLemmatizer

class TypeGetter():

    # This code is not generalized and can only handle the verb experiment.

    TAGDB = json.load(open('/Users/ajdjalali/Desktop/hpc/json/tags.json'))

    LEMMATIZER = WordNetLemmatizer().lemmatize

    def __init__(self, token):
        self.token = token

    @property
    def __standardize_tagdb(self):
        for word, tags in self.TAGDB.iteritems():
            #Hard code 'v' category
            self.TAGDB[self.wordnet_lemmatize(word, 'v')] = tags
        return self.TAGDB

    # Function taken from Chris Potts
    def wordnet_lemmatize(self, string, tag):
        tag = tag.lower()
        if tag.startswith('v'):    tag = 'v'
        elif tag.startswith('n'):  tag = 'n'
        elif tag.startswith('j'):  tag = 'a'
        elif tag.startswith('r'):  tag = 'r'
        if tag in ('n', 'v', 'a', 'r'):
            return self.LEMMATIZER(string, tag)
        else:
            return string

    @property
    def type(self):
        # Hard code 'v' category
        return self.wordnet_lemmatize(self.token, 'v')

    @property
    def tags(self):
        # Hard code 'v' category
        return self.__standardize_tagdb[self.type]
