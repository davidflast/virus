class Person:
    def __init__(self, id, dist):
        '''
        by default theyre uninfected
        '''
        self.infected = 0
        self.carrier = 0
        self.id = id
        # bool on whether or not the person is distancing themselves
        self.dist = dist
        
    def isInfected(self):
        # set whether or not the person
        # is 
        return self.infected

    def setLoc(self,locId):
        self.loc = locId

    def getLoc(self):
        # return person's location
        return self.loc

    def getId(self):
        # get person's
        # id #
        return self.id

    def interact(self):
        # returns the infected
        # person's carrirer status
        return self.carrier
    
    def washHands(self):
        # if person is a carrier
        # washing hands stops them
        # from being a carrier
        if self.carrier:
            self.carrier = 1
        
    
    
        
        
