from pgss.cell import Cell
from pgss.colony import Colony
import csv
import matplotlib.pyplot as plt

class ColonyAnalyzer:
    
    def __init__(self):
        self.colony_data_over_time = []
        self.time_data = []
        self.resistant = []
        self.nonresistant = []

    def analyze_colony(self, colony, time):
        num_resistant = 0
        num_nonresistant = 0

        for cell in colony.cells:
            if cell.resistant:
                num_resistant += 1
            else:
                num_nonresistant += 1
                
        # allows entire dataset to be appended to holistic data array in machine-friendly format
        self.colony_data_over_time.append([time, num_resistant, num_nonresistant])
        # appends data to individual data arrays; used for graphical representation of data
        self.time_data.append(time)
        self.resistant.append(num_resistant)
        self.nonresistant.append(num_nonresistant)
        
    def plot_data(self):
        plt.plot(self.time_data, self.resistant, label='Resistant')
        plt.plot(self.time_data, self.nonresistant, label='Nonresistant')
        plt.legend(loc='upper left')
        plt.xlabel('Time')
        plt.ylabel('Number of Bacteria')
        plt.show()

    # file name can be passed in with command line arguments  
    def write_to_csv(self, file_name):
        with open(file_name, mode='a') as file:
            file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #file_writer.writerow(self.colony_data_over_time)
            file_writer.writerow(self.time_data)
            file_writer.writerow(self.resistant)
            file_writer.writerow(self.nonresistant)
            # appends all data from one run in large chunks to reduce bottlenecking

    # for quick visualization of data
    def print_data(self):
        print("Time\t# Res. \t# Nonres.")
        #for data in self.colony_data_over_time:
            #print(str(data[0]) + "\t" + str(data[1]) + "\t" + str(data[2]))
        # the following code is more intuitive given the new individual data arrays
        for i in range(len(self.colony_data_over_time)):
            print(str(self.time_data[i]) + "\t" + str(self.resistant[i]) + "\t" + str(self.nonresistant[i]))

    # for testing class
    # redacted due to issues importing pgss module; probably involves file hierarchy
    #def main(self):
    #    self.write_to_csv(self, self.analyze_colony(self, Colony(), 0))

    #main()
