import sys
sys.path.append("..")
from people.person import Person

import random

class Simulation:
    def __init__(self, numPeople, numLocations, numTics):
        self.people = set()
        self.locations = set()
        self.numTics = numTics
        self.numPeople = numPeople
        
        for i in range(numPeople):
            person = Person(i)
            if random() < .1:
                person.infect()
            people.add(person)
        for i in range(numLocations)
            locations.add(Location(i))
    
    def runSimulation(self):
        for tic in range(numTics):
            for person in self.people:
                runTic(person)

    def runTic(self, person):
        isInfected = person.isInfected()

        p_move = 0. # 0% chance of the person moving

        p_wash = 0.25 # 25% of washing hands
        p_interact = 0.5 # 50% chance of interacting with a different person

        wash_dum = random.uniform(0,1)

        if wash_dum < p_wash:
            person.carrier = 0
            
        interact_dum = random.uniform(0,1)
        if interact_dum < p_interact:
            carrier_flag = person.interact()
            p_spread = 0.1 # 10% chance of spreading
            spread_dum = random.uniform(0,1)

            if spread_dum < p_spread:
                infect_id = random.randint(0,self.numPeople)
                
                p_carrirer = 0.1
                carrier_dum = random.uniform(0,1)
                if carrier_dum < p_carrier:
                    self.people[infect_id].carrier = 1
                if carrier_dum >= p_carrier:
                    self.people[infect_id].infected = 1
        
            
        
        
        
        



