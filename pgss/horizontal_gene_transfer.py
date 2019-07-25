#file for housing gene transfer
from pgss.cell import Cell
from pgss.colony import Colony

class Horizontal_Gene_Transfer:
    hgt_probability = 1000 #Probability of hgt
    def __init__(self):
        self.resistant_index = []
    #create a probability that horizontal transfer turns on
    #run a for loop for probability of turning on the transfer for all num_cells
    #make another for loop for cells that have the transfer turned on
    #run through the list of all, if they are turned on, then check the cells

    for i in (0,Colony._colony_size)
        if Cell.resistant = True
            self.resistant_index.append(i)

        else: None

    for i in (0,self.resistant_index)
        x = random.randint(0,self.hgt_probability)
        if x == 2
            #run transfer left
        else:
            if x == 53
            #run transfer right
            else: None



        #cell to left or right is resistant, carry out probability then transfer
