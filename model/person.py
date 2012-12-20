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

    def __init__(self, person):
        self.person = person
        self.name = self.person['name']
        self.office = 'U.S. Congress'
        self.party = self.person['party']
        self.state = self.person['state']
        self.district = self.person['district']

    def __str__(self):
        return self.name.encode('utf-8') + " " + self.party.encode('utf-8') + " " + self.state.encode('utf-8')
