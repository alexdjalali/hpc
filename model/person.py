REPUBLICAN = 'R'
DEMOCRAT = 'D'
INDEPENDENT = 'I'
PARTIES = [REPUBLICAN, DEMOCRAT, INDEPENDENT]

STATES = [
            "Alaska",
            "American Samoa",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Guam",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Northern Marianas Islands",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Puerto Rico",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Virgin Islands",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming",
    ]

############################################################################

class Person:

    def __init__(self, person, **kwargs):
        self.person = person
        # Get cleaned name
        self.first_name = self.person['name']['first'].strip()
        self.last_name = self.person['name']['last'].strip()
        self.full_name = self.first_name + " " + self.last_name
        # Get political office
        self.office = 'U.S. Congress'
        # Validate political party
        self.party = self.__validator(self.person['party'])
        # Validate state of representation
        self.state = self.__validator(self.person['state'])
        self.district = self.person['district']

    def __validator(self, validation):
        if validation in STATES or validation in PARTIES:
            return validation
        else:
            return ''
