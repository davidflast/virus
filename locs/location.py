class Location:
    def __init__(self, id):
        '''
        by default theyre uninfected
        '''
        self.people = set()
        self.id = id

    def personEnters(self, person):
        self.people.add(person)
    
    def personExits(self, person):
        self.people.remove(person)

    


