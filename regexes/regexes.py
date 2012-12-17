import re

class RegularExpressions():

    def __init__(self):
        pass

    def __det_regex(self):

        det_re = r"""
                    ([A-Za-z]+?_DT\s+)?              # Zero or one DT phrases with trailing space.
                    ((?:\S+_(?:JJ|RB|VBG)\S*\s+)*)   # Zero or more modifiers.
                    (
                    [Rr]epublican[s]{0,1}_N\S*       # Republicans with any tag.
                    |                                # or
                    [Dd]emocrat[s]{0,1}_N\S*         # Democrats with any tag.
                    )
                """

        return re.compile(det_re, re.VERBOSE | re.UNICODE | re.DOTALL | re.M)

    def __verb_regex(self):

        irregular_verbs = [
                            'forg[eo]t[s]{0,1}', 'sa(?:y|id)', '(?:tell|told)',
                            'beg[ia]n[s]{0,1}', 'stop[s]{0,1}(?:ped)',
                            'underst(?:a|oo)nd[s]{0,1}', 'kn[eo]w[s]{0,1}',
                            'th(?:ink[s]{0,1}|ought)'
                        ]

        ed_verbs = [verb + '(?:s|ed{0,1})' for verb in
                        [
                            'prevent', 'seem', 'regret', 'avoid', 'doubt', 'suspect'
                            'mention', 'request', 'order', 'ask', 'warn'
                        ]
                    ]

        d_verbs = [verb + '(?:s|[d]{0,1})' for verb in
                    [
                        'force', 'manage', 'promise', 'hesitate', 'surprise'
                        'hope', 'blame', 'believe', 'continue', 'accuse'
                        'criticize', 'realize',
                    ]
                ]

        verb_re = r"""
                    ([A-Za-z]+?_DT\s+)?
                    ((?:\S+_(?:JJ|RB|VBG)\S*\s+)*)
                    (
                    [Rr]epublican[s]{0,1}_N\S*
                    |
                    [Dd]emocrat[s]{0,1}_N\S*
                    )\s+
                    ((?:\S+_(?:RB)\S*\s+)*)
                    (
                """

        verbs = irregular_verbs + ed_verbs + d_verbs

        for verb in verbs:
            verb_re = verb_re + verb + "_V\S+|"

        verb_re = verb_re + 'continue[d]{0,1}_V\S+).+?\.'

        return re.compile(verb_re, re.VERBOSE | re.UNICODE | re.DOTALL | re.M)
