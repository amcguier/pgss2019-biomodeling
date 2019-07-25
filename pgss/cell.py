class Cell:

    def __init__(self, resistant, horizontal_transmission, death_probability_rate, reproduction_probability_rate):
        # Initialize cell here
        self.resistant = resistant
        self.horizontal_transmission = horizontal_transmission 
        self.death_probability_rate = death_probability_rate
        self.reproduction_probability_rate = reproduction_probability_rate
        
cell_var = Cell(resistant=True, horizontal_transmission=True, death_probability_rate=.1, reproduction_probability_rate=.15)

#reproduction is equal to one fission every twenty minutes for MRSA, 15-20 hours for TB\

#if resistant = false, then death = true

#Horizontal transfer: if antibiotic presence in simulation is high, then initiate horizontal transfer in sim

#cell age: if cells are from generations previous to the current generation (i.e. have reproduced at least once),
#then said cells are more likely to die