import json
from nltk.stem import WordNetLemmatizer

TAGS = json.load(open('Users/ajdjalali/Desktop/hpc/json/tags.json'))

class TypeGetter():

    LEMMATIZER = WordNetLemmatizer().lemmatize

    def __init__(self, token):
        self.token = token

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
    def tags(self):
        pass
