import math
import cmath

class ColonyUpdater:


    # Kill cells
        # if no antibiotics:
            # number of rate of death / chance of death
        # if yes antibiotics:
            # different for both resistant or susceptible

    # Make new cells
        # see kill cells

    # Transfer plasmid
        # depends on location from a resistant bacteria and chance should be low

    # Mutate cells
        # mutation rate for susceptible


    # updates every half minute
    update_time = 0.5
    # actual time
    actual_time = 0
    # k constant
    k = 0.5
    carrying_capacity = 100000
    kill_rate = 1000
    generation_time = 30  # for mrsa
    def updateColony(self,colony):
        self.actual_time += self.update_time
        self.make_new_cells(self, P, colony)
        self.kill_cells(self, P, colony)


        # for cell in colony:
            #Kill cells
            #Make new cells
            #Transfer plasmid
            #Mutate cells

    def make_new_cells(self, P, colony):
        k = math.log(2) / self.generation_time
        deltaP = self.update_time * k * P
        return deltaP
    def kill_cells(self, P, colony):
        k = 1 - P / self.carrying_capacity
        return k



x = ColonyUpdater()
y = []
for i in range(0, 1000):
    y.append('A')


z = 1000 + x.make_new_cells(1000, y)
for i in range(0, 1000):
    print(z)
    z += x.make_new_cells(z, y) * x.kill_cells(z, y)

