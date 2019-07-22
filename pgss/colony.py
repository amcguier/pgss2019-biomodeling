from cell import Cell
import random
class Colony:
    _colony_size = 1000000
    initial_resistant = 3 #Number of forced intial resistant bacteria
    def __init__(self):
        # todo set local variables here



        INITIAL_RESISTANCE_CHANCE = 10000 # 1/10,000
#add the # of cells we want into the colony value
        #run a random percent to get a True/False value assigned to each


        self.cells = []

        new_cell = None

        for i in range(0,self.initial_resistant):
            new_cell = Cell(resistant=True, horizontal_transmission=False, death_rate=.2351, reproduction=.2156453)
            self.cells.append(new_cell)

        for i in range(0,self._colony_size):

            if random.randint(0,INITIAL_RESISTANCE_CHANCE) == 2:
                new_cell = Cell(resistant=True, horizontal_transmission=False, death_rate=.2351, reproduction=.2156453) #resistant=True
            else:
                new_cell = Cell(resistant=False, horizontal_transmission=False, death_rate=.2351, reproduction=.2156453) #resistant=False


            self.cells.append(new_cell)
        for cell in self.cells:
            print(cell.resistant)
    #return colony

colony_var=Colony()
# Cell.resistant = True/False
# variable for probability
    #
