from pgss.cell import Cell
import random

class Colony:
    _colony_size = 1000 # Number of cells in colony
    _num_initial_resistant = 0 # Number cells that will initially be forced to be resistant
    _initial_resistance_chance = 100 # Probability of being resistant for remaining cells 
    gene_transfer = True

    def __init__(self, bacteria_type, colony_size, chance_resistant, reproduction_time, drug_survival_chance, _num_initial_resistant, gene_transfer):
        self._colony_size = colony_size
        self._initial_resistance_chance = chance_resistant
        self._num_initial_resistant = _num_initial_resistant
        self.cells = []
        self.gene_transfer = gene_transfer

        # Create _num_initial_resistant cells with forced resistance
        for i in range(0,self._num_initial_resistant):
            new_cell = Cell(resistant=True, death_probability_rate=.1, reproduction_probability_rate=.15)
            self.cells.append(new_cell)

        # Create remaining cells with _initial_resistance_chance chance of being resistant
        for i in range(0,self._colony_size - self._num_initial_resistant):
            if random.randint(0,self._initial_resistance_chance) == 2:
                # Add a cell with antibiotic resistance
                new_cell = Cell(resistant=True, death_probability_rate=.1, reproduction_probability_rate=.15)
            else:
                # Add a cell without antibiotic resistance
                new_cell = Cell(resistant=False, death_probability_rate=.1, reproduction_probability_rate=.15)
            self.cells.append(new_cell)
