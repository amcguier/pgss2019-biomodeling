import math
import cmath
import random
from  colony import Colony
from cell import Cell

class ColonyUpdater:


    # updates every half minute
    update_time = 0.5
    actual_time = 0
    # generation time for mrsa in minutes
    generation_time = 30
    k = math.log(2) / generation_time  # this is the k constant in the equation e^-kt
    cell_reproduction_probability = update_time * k  # this is the probability that the cell will duplicate during the next update time

    # The following "individual methods" kill_cell, make_new_cell, transfer_plasmid, and mutate_cell operate on the individual cell
    # deletes an individual cell at the position i in the colony
    def kill_cell(self, colony, i):
        del colony.cells[i]
    # duplicates an individual cell at the position i, with the same features
    def make_new_cell(self, colony, i):
        old_cell = colony.cells[i]
        new_cell = Cell(old_cell.resistant, old_cell.horizontal_transmission, old_cell.death_rate, old_cell.reproduction)
        colony.cells.insert(i, new_cell)
    # gives a resistance "gene" from a resistant cell at position i in the list to a non-resistant cell at a position j
    # this assumes that the cell at position i is resistant and j is not
    def transfer_plasmid(self, colony, i, j):
        old_cell = colony.cells[j]
        new_cell = Cell(colony[i].resistant, old_cell.horizontal_transmission, old_cell.death_rate, old_cell.reproduction)
        colony.cells.insert(j, new_cell)
        del colony[j+1]
    # changes susceptible cell to resistant, assumes the cell is already susceptible
    def mutate_cell(self, colony, i):
        old_cell = colony.cells[i]
        new_cell = Cell(True, old_cell.horizontal_transmission, old_cell.death_rate, old_cell.reproduction)
        colony.cells.insert(i, new_cell)
        del colony[i+1]


    def updateColony(self,colony):
        self.actual_time += self.update_time

        #  loops through the colony
        i = 0
        while i < len(colony.cells):
            curr_cell = colony.cells[i]
            x = random.random()
            if (x < 0.0000002):
                self.kill_cell(colony, i)
            elif (x > 1 - self.cell_reproduction_probability):
                self.make_new_cell(colony, i)
                i = i + 2
            else:
                i = i + 1


cu = ColonyUpdater()
# initializes the colony
c = Colony()
for i in range(0, 200):
    cu.updateColony(c)
    print(len(c.cells))



'''x = ColonyUpdater()
y = []
for i in range(0, 1000):
    y.append('A')


z = 1000 + x.make_new_cells(1000, y)
for i in range(0, 1000):
    print(z)
    z += x.make_new_cells(z, y) * x.kill_cells(z, y)'''