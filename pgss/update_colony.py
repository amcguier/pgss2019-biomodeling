import math
import cmath
import random
from pgss.colony import Colony
from pgss.cell import Cell

class ColonyUpdater:
    hgt_probability = 1000 #Probability of hgt
    resistant_index = []

    # Amount of time incremented (in minutes) per iteration of simulation.
    update_time = 0.5
    # Simulation starts at time zero.
    actual_time = 0
    #  nonresistant growth rate starts decreasing after -1.5; resistant growth rate after 1
    #  In log scale (so -1 corresponds to 1/10 of a ug/mL of tetracycline
    tetracycline = 2
    #  chance of mutation
    bacteria_mutation_rate = 0.0001
    #  these are the horizontal asymtotes, the death and reproduction rates should approach 0.5 as time goes to infinity
    p_reproduction = 0.5
    p_death = 0.5
    #  these are the steepness variables that determines the steepness of the logistic curve
    k_reproduction = 0.3
    k_death = 0.2
    #  these are the response times for something to happen
    t_reproduction = 10
    t_death = 20

    #  calculates a generic probability of reproduction from a variable "steepness" that determines the steepness of the logistic curve
    def calculate_reproduction_probability(self, steepness):
        return self.update_time * self.p_reproduction / (1 + math.exp(steepness * (self.t_reproduction - self.actual_time)))

    #  same as calculate_reproduction_probability_rate, except for death
    def calculate_death_probability(self, steepness):
        return self.update_time * self.p_death / (1 + math.exp(steepness * (self.t_death - self.actual_time)))

    def calculate_rp_tetracycline_resistant(self, steepness, concentration):
        factor = -0.556 * concentration + 1.56
        if factor < 0:
            factor = 0
        elif factor > 1:
            factor = 1
        #  x is our new reproduction rate
        x = self.k_death + (self.k_reproduction - self.k_death) * factor
        return self.calculate_reproduction_probability(x)

    def calculate_rp_tetracycline_nonresistant(self, steepness, concentration):
        factor = -0.672 * concentration + 0.0739
        if factor < 0:
            factor = 0
        elif factor > 1:
            factor = 1
        #  x is our new reproduction rate
        x = self.k_death + (self.k_reproduction - self.k_death) * factor
        return self.calculate_reproduction_probability(x)
    def calculate_dp_tetracycline_resistant(self, steepness, concentration):
        return self.calculate_death_probability(steepness)
    def calculate_dp_tetracycline_nonresistant(self, steepness, concentration):
        return self.calculate_death_probability(steepness)


    '''def calculate_reproduction_probability_rate(self, colony, steepness):
        # Function of time and other constants for determining current reproduction_probability_rates for each cell
        # Multiplying this value by delta_t (update_time) gives probability of cell reproducing during current update
        return self.update_time * self.p_d / (1 + math.exp(steepness * (self.t_d - self.actual_time)))

    def calculate_reproduction_probability_rate_tetracycline_resistant(self, colony, steepness, concentration):
        factor = -0.556 * concentration + 1.56
        return self.update_time * self.p_d / (1 + math.exp(steepness * (self.t_d - self.actual_time)))

    # tester for tetracycline
    def calculate_reproduction_probability_rate_tetracycline_nonresistant(self, colony, steepness, concentration):
        factor = -0.672 * concentration + 0.0739
        return self.update_time * self.p_d / (1 + math.exp(steepness * (self.t_d - self.actual_time)))

    def calculate_death_probability_rate(self, colony, steepness):
        # Function of time and other constants for determining current death_probability_rates for each resistant cell
        # Multiplying this value by delta_t (update_time) gives probability of cell dying during current up
        return self.update_time * self.p_m / (1 + math.exp(steepness * (self.t_m - self.actual_time)) )

    def calculate_resistant_death_probability_rate(self, colony, concentration, steepness):
        # Function of time and other constants for determining current death_probability_rates for each resistant cell
        # Multiplying this value by delta_t (update_time) gives probability of cell dying during current up
        # return self.update_time * self.p_m / (1 + math.exp(self.k_m * (self.t_m - self.actual_time)) )
        return self.calculate_death_probability_rate(colony, steepness)

    def calculate_nonresistant_death_probability_rate(self, colony, concentration, steepness):
        # Function of time and other constants for determining current death_probability_rates for each resistant cell
        # Multiplying this value by delta_t (update_time) gives probability of cell dying during current up
        return self.calculate_death_probability_rate(colony, steepness)
    '''
    '''
        if self.tetracycline > -2:  #  if there is sufficient amount of tetracycline to make a difference
            return self.update_time * self.p_m / (1 + math.exp(self.k_m * (self.t_m - self.actual_time)) ) #* 2  #  100 times more likely to die in antibiotic environment
        else:
            return self.update_time * self.p_m / (1 + math.exp(self.k_m * (self.t_m - self.actual_time)))
    '''



    # The following "individual methods" kill_cell, make_new_cell, transfer_plasmid, and mutate_cell operate on the individual cell

    # deletes an individual cell at the position i in the colonypass
    def kill_cell(self, colony, i):
        del colony.cells[i]

    # duplicates an individual cell at the position i, with the same features
    def make_new_cell(self, colony, i):
        old_cell = colony.cells[i]
        new_cell = Cell(old_cell.resistant, old_cell.death_probability_rate, old_cell.reproduction_probability_rate)
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

    def Horizontal_Gene_Transfer(self,colony):
        for i in range(0,len(colony.cells)):
            cell = colony.cells[i]
            if cell.resistant:
                self.resistant_index.append(i)

        for i in range (0,len(self.resistant_index)):
            x = random.randint(0,self.hgt_probability)
            if x == 2:
                if self.resistant_index[i] > 0:
                    self.transfer_plasmid(colony,self.resistant_index[i],self.resistant_index[i]-1) #run transfer left

            else:
                if x == 3:
                    if self.resistant_index[i]<= len(colony.cells)-2:
                        self.transfer_plasmid(colony,self.resistant_index[i],self.resistant_index[i]+1) #run transfer right

    #Todo: add end behavior
        self.resistant_index = []


    # Updates colony by stochastically selecting if each cell dies, reproduces, or just survives during this iteration.
    def updateColony(self,colony):
        self.actual_time += self.update_time
        resistant_dpr = self.calculate_dp_tetracycline_resistant(self.k_death, self.tetracycline)
        nonresistant_dpr = self.calculate_dp_tetracycline_nonresistant(self.k_death, self.tetracycline)
        resistant_rpr = self.calculate_rp_tetracycline_resistant( self.calculate_rp_tetracycline_resistant(self.k_reproduction, self.tetracycline), self.tetracycline)
        nonresistant_rpr = self.calculate_rp_tetracycline_nonresistant( self.calculate_rp_tetracycline_nonresistant(self.k_reproduction, self.tetracycline), self.tetracycline)

        # Loops through each cell in the colony
        i = 0
        while i < len(colony.cells):
            x = random.random()
            cell = colony.cells[i]
            #  check if the cell should be killed
            if (cell.resistant and x < resistant_dpr) or (not cell.resistant and x < nonresistant_dpr):
                self.kill_cell(colony, i)
            #  check if the cell should reproduce
            elif (cell.resistant and x > 1 - resistant_rpr) or (not cell.resistant and x > 1 - nonresistant_rpr):
                # Cell reproduces
                self.make_new_cell(colony, i)
                i = i + 2
            else:
                # Cell survives,
                #   if the cell is non-resistant, it has a chance of mutating itself to become resistant
                #   if the cell is resistant, it has a chance of transferring its plasmid to another cell
                y = random.random()
                #  mutate
                if not cell.resistant and y < self.bacteria_mutation_rate:
                    self.mutate_cell(colony, i)
                i = i + 1
        self.Horizontal_Gene_Transfer(colony)

        return self.actual_time
