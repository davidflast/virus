import sys
sys.path.append("..")
from people.person import Person

import random

class Simulation:
    def __init__(self, numPeople, numLocations, numTics):
        self.people = set()
        self.locations = set()
        self.numTics = numTics
        for i in range(numPeople):
            person = Person(i)
            if random() < .1:
                person.infect()
            people.add(person)
        for i in range(numLocations)
            locations.add(Location(i))
    
    def runSimulation()
        for tic in range(numTics):



