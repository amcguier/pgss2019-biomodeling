class Cell:

    def __init__(self, resistant, horizontal_transmission, death_rate, reproduction):
        # initialize cell here
        self.resistant = resistant
        self.horizontal_transmission = horizontal_transmission 
        self.death_rate = death_rate
        self.reproduction = reproduction
        
cell_var = Cell(resistant=True, horizontal_transmission=True, death_rate=.465, reproduction=.3405729384750928374)

#reproduction is equal to one fission every twenty minutes for MRSA, 15-20 hours for TB\

#if resistant = false, then death = true

#Horizontal transfer: if antibiotic presence in simulation is high, then initiate horizontal transfer in sim

#cell age: if cells are from generations previous to the current generation (i.e. have reproduced at least once),
#then said cells are more likely to die