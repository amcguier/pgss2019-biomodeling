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

    #  The first antibiotic is introduced if true and is not introduced if false
    antibiotic1 = False
    #  chance of mutation
    bacteria_mutation_rate = 0.0001
    horizontal_gene_transfer_rate = 0.01


    # TODO: switch reproduction/death rates to be stored at the individual cell level, so that we can have variation among cells
    # Generation time in minutes
    generation_time = 30
    reproduction_probability_rate = math.log(2) / generation_time  # this is the k constant in the equation e^-kt
    death_probability_rate = 0.05

    p_d = 0.5
    p_m = 0.5
    k_d = 0.3
    k_m = 0.2
    t_d = 10
    t_m = 20
    def calculate_reproduction_probability_rate(self, colony):
        # Function of time and other constants for determining current reproduction_probability_rates for each cell
        # Multiplying this value by delta_t (update_time) gives probability of cell reproducing during current update
        return self.update_time * self.p_d / ( 1 + math.exp(self.k_d * (self.t_d - self.actual_time)) )

    def calculate_resistant_death_probability_rate(self, colony):
        # Function of time and other constants for determining current death_probability_rates for each resistant cell
        # Multiplying this value by delta_t (update_time) gives probability of cell dying during current up
        return self.update_time * self.p_m / (1 + math.exp(self.k_m * (self.t_m - self.actual_time)) )

    def calculate_nonresistant_death_probability_rate(self, colony):
        # Function of time and other constants for determining current death_probability_rates for each resistant cell
        # Multiplying this value by delta_t (update_time) gives probability of cell dying during current up
        if self.antibiotic1 == True:
            return self.update_time * self.p_m / (1 + math.exp(self.k_m * (self.t_m - self.actual_time)) ) * 100  #  100 times more likely to die in antibiotic environment
        else:
            return self.update_time * self.p_m / (1 + math.exp(self.k_m * (self.t_m - self.actual_time)))




    # The following "individual methods" kill_cell, make_new_cell, transfer_plasmid, and mutate_cell operate on the individual cell
    
    # deletes an individual cell at the position i in the colonypass
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
        colony.cells[j].resistant = colony.cells[i].resistant
    
    # changes susceptible cell to resistant, assumes the cell is already susceptible
    def mutate_cell(self, colony, i):
        # TODO: change this so that we are updating the cell in place rather than deleting and creating a new cell.
       colony.cells[i].resistant = True

    def turn_on_antibiotic1(self):
        self.antibiotic1 = True


    def turn_off_antibiotic1(self):
        self.antibiotic1 = False


    def showColonySummary(self, colony):
        print('Total number: ' + str(len(colony.cells)))

    # Updates colony by stochastically selecting if each cell dies, reproduces, or just survives during this iteration.
    def updateColony(self,colony):
        self.actual_time += self.update_time
        resistant_dpr = self.calculate_resistant_death_probability_rate(colony)
        nonresistant_dpr = self.calculate_nonresistant_death_probability_rate(colony)
        rpr = self.calculate_reproduction_probability_rate(colony)

        # Loops through each cell in the colony
        i = 0
        while i < len(colony.cells):
            x = random.random()
            #  check if the cell should be killed
            if colony.cells[i].resistant == True and x < resistant_dpr or colony.cells[i].resistant == False and x < nonresistant_dpr:
                self.kill_cell(colony, i)
            #  check if the cell should reproduce
            elif (x > 1 - rpr):
                # Cell reproduces
                self.make_new_cell(colony, i)
                i = i + 2
            else:
                # Cell survives,
                #   if the cell is non-resistant, it has a chance of mutating itself to become resistant
                #   if the cell is resistant, it has a chance of transferring its plasmid to another cell
                y = random.random()
                #  mutate
                if colony.cells[i].resistant == False and y < self.bacteria_mutation_rate:
                    self.mutate_cell(colony, i)
                #  transfer plasmid
                '''elif y < 1 - colony.cells[i].resistant == True and y > 1 - horizontal_gene_transfer_rate:
                    self.transfer_plasmid(colony, i, i + 1)'''

                i = i + 1

        return self.actual_time