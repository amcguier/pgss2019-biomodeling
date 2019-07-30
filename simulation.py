# If an ImportError occurs, make sure Path variable includes the locations of the Python installation and Python scripts
# e.g. "C:\Users\xxx\Python37\" and "C:\Users\xxx\Python37\Scripts\"
# If this fails, reinstall Python using a custom installation and make sure to select "Add Python to environment variables"

from pgss.colony import Colony
from pgss.analyze import ColonyAnalyzer
from pgss.cell import Cell
from pgss.update_colony import ColonyUpdater

iterations = 100
size = 200
bacteria_type = ''
resistance = 100
gene_transfer = True
reproduction = 0
drug_survival = 0
_num_initial_resistant = 0

import csv
import sys


def parse():
        global bacteria_type, resistance, size, gene_transfer, drug_survival, _num_initial_resistant, reproduction
        #file = open("inputFile.txt")
        with open('Input.csv', newline='') as csvfile: 
            inputreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            rowcount = 0
            headerslist = None
            values = None
            
            for row in inputreader:
                if rowcount == 0:
                    headerslist = list(row)
                    rowcount += 1
                else:
                    values = list(row)
                
            rowcount = 0     
            for header in headerslist:
                if header == 'Bacteria Type':
                    bacteria_type = values[rowcount]
                elif header == 'Colony Size':
                    size = int(values[rowcount])
                elif header == 'Chance of Resistance':
                    resistance = int(values[rowcount])
                elif header == 'Does Horizontal Tranfer Occur':
                    answer = values[rowcount]
                    gene_transfer = answer == 'YES'
                elif header == 'Reproduction Time':
                    reproduction = int(values[rowcount])
                elif header == 'Drug Survival Chance':
                    drug_survival = int(values[rowcount])
                else:
                    _num_initial_resistant = int(values[rowcount])
                    

                    
                rowcount += 1

        #for line in file.readlines():
         #   strippedline=line.strip()
          #  if strippedline != "":
                #this section runs through every line, assessed which info is provided per line,
                #and assigns it to the appropriate variables. Then, all the info is printed
           #         parts = strippedline.split(":")
            #        if strippedline.startswith('Bacteria Type:'):
             #           bacteria_type = parts[1]
            
             #       if strippedline.startswith('Colony Size:'):
              #          size = int(parts[1])
               #     if strippedline.startswith('Chance of Resistance:'):
                #        resistance = int(parts[1])
                 #   if strippedline.startswith('Does Horizontal Transfer Occur?:'):
                  #      if parts[1] == 'True':
                   #         gene_transfer = True
                    #    else:
                     #       gene_transfer = False
                    #if strippedline.startswith('Reproduction Time:'):
                    #    reproduction = int(parts[1])
                    #if strippedline.startswith('Drug Survival Chance:'):
                    #    drug_survival = int(parts[1])
                    #if strippedline.startswith('Number Initially Resistant:'):
                     #   _num_initial_resistant = int(parts[1])

def runSimulation():
    colony = Colony(bacteria_type,size,resistance, reproduction, drug_survival, _num_initial_resistant)
    updater = ColonyUpdater()
    analyzer = ColonyAnalyzer()

    analyzer.analyze_colony(colony, 0)
    for index in range(iterations):
        time = updater.updateColony(colony)
        analyzer.analyze_colony(colony, time)
        print(index)
    analyzer.print_data()
    analyzer.plot_data()
    analyzer.bar_graph()
    analyzer.bar_graph_2()
    analyzer.write_to_csv(sys.argv[1])
    updater.plot_probability_rates()

if __name__ == '__main__':
    #runImport()
    #parse()
    runSimulation()

