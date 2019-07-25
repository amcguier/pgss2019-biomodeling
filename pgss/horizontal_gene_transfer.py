#file for housing gene transfer
from pgss.cell import Cell
from pgss.colony import Colony
from pgss.update_colony import update_colony

class Horizontal_Gene_Transfer:
    hgt_probability = 1000 #Probability of hgt
    def __init__(self):
        self.resistant_index = []
    #create a probability that horizontal transfer turns on
    #run a for loop for probability of turning on the transfer for all num_cells
    #make another for loop for cells that have the transfer turned on
    #run through the list of all, if they are turned on, then check the cells

    for i in (0,Colony._colony_size):
        if Cell.resistant = True:
            self.resistant_index.append(i)

    for i in (0,self.resistant_index):
        x = random.randint(0,self.hgt_probability)
        if x == 2:
            if self.resistant_index[i] > 0:
                self.transfer_plasmid(self, colony,self.resistant_index[i],self.resistant_index[i]-1) #run transfer left

        else:
            if x == 53:
                if self.resistant_index[i]<= Colony._colony_size:
                    updateColony.transfer_plasmid(self, colony,self.resistant_index[i],self.resistant_index[i]+1) #run transfer right


#Todo: add end behavior
self.resistant_index = []





        #cell to left or right is resistant, carry out probability then transfer
