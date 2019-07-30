import math
import cmath
import random
import matplotlib.pyplot as plt
import numpy as np

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
    #  these are the steepness variables that determines the steepness of the logistic curve, don't change
    k_reproduction = 0.3
    k_death = 0.2

    #  this is the timepoint of the inflection point of the logistic curve
    t_reproduction = 10
    t_reproduction_upper_limit = 30
    t_death = 20

    time_data = []
    resistant_reproduction_probabilities = []
    resistant_death_probabilities = []
    nonresistant_reproduction_probabilities = []
    nonresistant_death_probabilities = []

    #  calculates a generic probability of reproduction from a variable "steepness" that determines the steepness of the logistic curve
    def calculate_reproduction_probability(self, steepness, inflection):
        return self.update_time * self.p_reproduction / (1 + math.exp(steepness * (inflection - self.actual_time)))

    #  same as calculate_reproduction_probability, except for death
    def calculate_death_probability(self, steepness, inflection):
        return self.update_time * self.p_death / (1 + math.exp(steepness * (inflection - self.actual_time)))

    def calculate_inflection_tetracycline_resistant(self):
        factor = -0.556 * self.tetracycline + 1.56
        if factor < 0:
            factor = 0
        elif factor > 1:
            factor = 1
        return (self.t_reproduction - self.t_reproduction_upper_limit) * factor + t_reproduction_upper_limit

    def calculate_inflection_tetracycline_nonresistant(self):
        factor = -0.672 * self.tetracycline + 0.0739
        if factor < 0:
            factor = 0
        elif factor > 1:
            factor = 1
        return (self.t_reproduction - self.t_reproduction_upper_limit) * factor + t_reproduction_upper_limit


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
        colony.cells[j].resistant = colony.cells[i].resistant
    # changes susceptible cell to resistant, assumes the cell is already susceptible
    def mutate_cell(self, colony, i):
        colony.cells[i].resistant = True
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
        '''
        resistant_dp = self.calculate_dp_tetracycline_resistant(self.k_death, self.tetracycline)
        nonresistant_dp = self.calculate_dp_tetracycline_nonresistant(self.k_death, self.tetracycline)
        resistant_rp = self.calculate_rp_tetracycline_resistant(self.k_reproduction, self.tetracycline)
        nonresistant_rp = self.calculate_rp_tetracycline_nonresistant(self.k_reproduction, self.tetracycline)
        '''
        resistant_dp = self.calculate_death_probability(self.k_death, self.t_death)
        nonresistant_dp = self.calculate_death_probability(self.k_death, self.t_death)
        resistant_rp = self.calculate_reproduction_probability(self.k_reproduction,   self.calculate_inflection_tetracycline_resistant()) # self.t_reproduction
        nonresistant_rp = self.calculate_reproduction_probability(self.k_reproduction, self.calculate_inflection_tetracycline_nonresistant())  # self.t_reproduction

        
        # Loops through each cell in the colony
        i = 0
        while i < len(colony.cells):
            x = random.random()
            cell = colony.cells[i]
            #  check if the cell should be killed
            if (cell.resistant and x < resistant_dp) or (not cell.resistant and x < nonresistant_dp):
                self.kill_cell(colony, i)
            #  check if the cell should reproduce
            elif (cell.resistant and x > 1 - resistant_rp) or (not cell.resistant and x > 1 - nonresistant_rp):
                # Cell reproduces
                self.make_new_cell(colony, i)
                i = i + 2
            else:
                # Cell survives,
                #   if the cell is non-resistant, it has a chance of mutating itself to become resistant
                #   if the cell is resistant, it has a chance of transferring its plasmid to another cell
                # y = random.random()
                #  mutate
                # if not cell.resistant and y < self.bacteria_mutation_rate:
                    # self.mutate_cell(colony, i)
                i = i + 1

        # self.Horizontal_Gene_Transfer(colony)
      
        self.time_data.append(self.actual_time)
        self.resistant_reproduction_probabilities.append(resistant_rp)
        self.nonresistant_reproduction_probabilities.append(nonresistant_rp)
        self.resistant_death_probabilities.append(resistant_dp)
        self.nonresistant_death_probabilities.append(nonresistant_dp)

        return self.actual_time

    def plot_probability_rates(self):
        plt.plot(self.time_data, self.resistant_reproduction_probabilities, label='Resistant Reproduction Prob.')
        plt.plot(self.time_data, self.nonresistant_reproduction_probabilities, label='Nonresistant Reproduction Prob.')
        plt.plot(self.time_data, self.resistant_death_probabilities, label='Resistant Death Prob.')
        plt.plot(self.time_data, self.nonresistant_death_probabilities, label='Nonresistant Death Prob.')
        plt.legend(loc='upper left')
        plt.show()
