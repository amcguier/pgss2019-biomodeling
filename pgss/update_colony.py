import math
import cmath
import random
from pgss.colony import Colony
from pgss.cell import Cell

class ColonyUpdater:

    # Amount of time incremented (in minutes) per iteration of simulation.
    update_time = 0.5

    # Simulation starts at time zero.
    actual_time = 0

    # TODO: switch reproduction/death rates to be stored at the individual cell level, so that we can have variation among cells
    # Generation time in minutes
    generation_time = 30
    reproduction_probability_rate = math.log(2) / generation_time  # this is the k constant in the equation e^-kt
    death_probability_rate = 0.05

    def calculate_reproduction_probability_rates(self, colony):
        # Function of time and other constants for determining current reproduction_probability_rates for each cell
        # Multiplying this value by delta_t (update_time) gives probability of cell reproducing during current update
        pass

    def calculate_death_probability_rates(self, colony):
        # Function of time and other constants for determining current death_probability_rates for each cell
        # Multiplying this value by delta_t (update_time) gives probability of cell dying during current update
        pass


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
        new_cell = Cell(old_cell.resistant, old_cell.horizontal_transmission, old_cell.death_probability_rate, old_cell.reproduction_probability_rate)
        colony.cells.insert(i, new_cell)

    # gives a resistance "gene" from a resistant cell at position i in the list to a non-resistant cell at a position j
    # this assumes that the cell at position i is resistant and j is not
    def transfer_plasmid(self, colony, i, j):
        # TODO: change this so that we are updating the cell in place rather than deleting and creating a new cell.
        old_cell = colony.cells[j]
        new_cell = Cell(colony[i].resistant, old_cell.horizontal_transmission, old_cell.death_probability_rate, old_cell.reproduction_probability_rate)
        colony.cells.insert(j, new_cell)
        del colony[j+1]
    
    # changes susceptible cell to resistant, assumes the cell is already susceptible
    def mutate_cell(self, colony, i):
        # TODO: change this so that we are updating the cell in place rather than deleting and creating a new cell.
        old_cell = colony.cells[i]
        new_cell = Cell(True, old_cell.horizontal_transmission, old_cell.death_probability_rate, old_cell.reproduction_probability_rate)
        colony.cells[i] = new_cell


    def turn_on_antibiotic1(self):
        self.antibiotic1 = True


    def turn_off_antibiotic1(self):
        self.antibiotic1 = False


    def showColonySummary(self, colony):
        print('Total number: ' + str(len(colony.cells)))

    # Updates colony by stochastically selecting if each cell dies, reproduces, or just survives during this iteration.
    def updateColony(self,colony):
        self.actual_time += self.update_time
        self.calculate_death_probability_rates(colony)
        self.calculate_reproduction_probability_rates(colony)

        # Loops through each cell in the colony
        i = 0
        while i < len(colony.cells):
            curr_cell = colony.cells[i]
            x = random.random()

            # make sure to differentiate between resistant or non-resistant cells
            cell_antibiotic_probability == self.kill_rate_constant

            #  changes death rates for non-resistant cells in a toxic, antibiotic environment
            if (antibiotic1 == True && colony.cells[i].resistant == False)
                cell_antibiotic_probability == self.kill_rate_constant * self.non_resistant_decrease

            #if (x < cell_antibiotic_probability):
            if (x < (self.death_probability_rate * self.update_time)):
                # Cell dies
                self.kill_cell(colony, i)
            elif (x > 1 - (self.reproduction_probability_rate * self.update_time)):
                # Cell reproduces
                self.make_new_cell(colony, i)
                i = i + 2
            else:
                # Cell survives
                i = i + 1

        return self.actual_time
