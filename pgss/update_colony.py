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
    generation_time = 20
    k = math.log(2) / generation_time  # this is the k constant in the equation e^-kt
    cell_reproduction_probability = update_time * k  # this is the probability that the cell will duplicate during the next update time

    kill_rate_constant = 0.05
    #  probability of survival is increased 100 fold in an antibiotic environment if the bacteria is antibiotic resistant
    resistant_boost = 100
    #  the factor of chance of life decreases by this much in an antibiotic environment
    nonresistant_decrease = 18

    #  The first antibiotic is introduced if true and is not introduced if false
    antibiotic1 = False


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
        new_cell = Cell(colony.cells[i].resistant, old_cell.horizontal_transmission, old_cell.death_rate, old_cell.reproduction)
        colony.cells[j] = new_cell
    # changes susceptible cell to resistant, assumes the cell is already susceptible
    def mutate_cell(self, colony, i):
        old_cell = colony.cells[i]
        new_cell = Cell(True, old_cell.horizontal_transmission, old_cell.death_rate, old_cell.reproduction)
        colony.cells[i] = new_cell
    def turn_on_antibiotic1(self):
        self.antibiotic1 = True
    def turn_off_antibiotic1(self):
        self.antibiotic1 = False
    def showColonySummary(self,colony):
        print( 'Total number: ' + str(len(colony.cells)))


    def updateColony(self,colony):
        self.actual_time += self.update_time

        #  loops through the colony
        i = 0
        while i < len(colony.cells):
            curr_cell = colony.cells[i]
            x = random.random()

            # make sure to differentiate between resistant or non-resistant cells
            cell_antibiotic_probability == self.kill_rate_constant

            #  changes death rates for non-resistant cells in a toxic, antibiotic environment
            if (antibiotic1 == True && colony.cells[i].resistant == False)
                cell_antibiotic_probability == self.kill_rate_constant * self.non_resistant_decrease

            if (x < cell_antibiotic_probability):
                self.kill_cell(colony, i)
            elif (x > 1 - self.cell_reproduction_probability):
                self.make_new_cell(colony, i)
                i = i + 2
            else:
                i = i + 1

# initializes the colony
c = Colony()
cu = ColonyUpdater()
for i in range(0, 10000):
    cu.updateColony(c)
    cu.showColonySummary(c)