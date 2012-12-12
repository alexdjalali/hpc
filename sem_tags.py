from nltk.stem.lancaster import LancasterStemmer

class TypeGetter():

    ST = LancasterStemmer()

    SEM_TAGS = {
                'hole': [
                            'say', 'mention', 'tell', 'ask', 'promise',
                            'warn', 'request', 'order', 'accuse', 'criticize',
                            'blame', 'believe', 'think', 'doubt', 'suspect',
                            'hope', 'know'
                    ],
                'plug': [
                            'know', 'regret', 'understand', 'surprise', 'begin',
                            'stop', 'continue', 'manage', 'avoid', 'force', 'prevent',
                            'hesitate', 'seem',
                    ],
                'factive': [
                            'know', 'forget', 'realize', 'regret',

                    ]
                }

    def __init__(self, token):
        self.token = token

    @property
    def stemmed(self):
        return self.ST.stem(self.token)

    @property
    def tags(self):
        SemTags = dict([(key, [self.ST.stem(token) for token in self.ST.values()]) for key, value in self.SEM_TAGS])
        return [key for key in SemTags.keys() if self.token.stemmed in SemTags[key]]

print TypeGetter('knew').tags

