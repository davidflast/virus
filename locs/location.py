class location:
    def __init__(self, id):
        '''
        by default theyre uninfected
        '''
        self.people = set()
        self.id = id

    def person_enters(person):
        self.people.add(person)
    
    def person_exits(person):
        self.people.remove(person)

    


