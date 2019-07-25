from pgss.cell import Cell
from pgss.colony import Colony
import csv
import matplotlib.pyplot as plt

# TODO:

class ColonyAnalyzer:

    ## no constructor necessary since the class creates its own data structures and writes them to a file
    colony_data_over_time = []
    time_data = []
    resistant = []
    nonresistant = []
    
    def __init__(self):
        self.colony_data_over_time = []

    def analyze_colony(self, colony, time):
        num_resistant = 0
        num_nonresistant = 0
        #average_horizontal_transmission = 0
        #average_cell_age = 0

        for cell in colony.cells:
            if cell.resistant:
                num_resistant += 1
            else:
                num_nonresistant += 1
                
        # average_cell_age += cell.cell_age
            # cell_age has not been added to the Cell constructor
        # average_cell_age /= Colony._colony_size
            # It has not been determined whether cell_age will be included as a parameter in the model

        self.colony_data_over_time.append([time, num_resistant, num_nonresistant])
        
        self.time_data.append(time)
        self.resistant.append(num_resistant)
        self.nonresistant.append(num_nonresistant)
        return self.colony_data_over_time
        
    def plot_data(self):
        plt.plot(self.time_data, self.resistant)
        plt.plot(self.time_data, self.nonresistant)
        
        plt.plot(self.time_data, self.resistant, label='Resistant')
        plt.plot(self.time_data, self.nonresistant, label='Nonresistant')
        plt.legend(loc='upper left')
        plt.xlabel('Time')
        plt.ylabel('Number of Bacteria')
        
                

    def write_to_csv(self, data):
        with open('colony_analysis.csv', mode = 'a') as colony_analysis:
            file_writer = csv.writer(colony_analysis, delimiter = ", ", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            file_writer.write(data)
            file_writer.close()
            # append entire dataset to file in one operation to reduce bottlenecks

    def print_data(self):
        print("Time\t# Res. \t# Nonres.")
        for data in self.colony_data_over_time:
            print(str(data[0]) + "\t" + str(data[1]) + "\t" + str(data[2]))

    # for testing class
    def main(self):
        self.write_to_csv(self, self.analyze_colony(self, Colony(), 0))

    main()
