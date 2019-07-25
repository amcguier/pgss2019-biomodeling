from pgss.colony import Colony
from pgss.analyze import ColonyAnalyzer
from pgss.cell import Cell
from pgss.update_colony import ColonyUpdater

iterations = 50


def runSimulation():
    colony = Colony()
    updater = ColonyUpdater()
    analyzer = ColonyAnalyzer()

    analyzer.analyze_colony(colony, 0)
    for index in range(iterations):
        time = updater.updateColony(colony)
        analyzer.analyze_colony(colony, time)
    analyzer.print_data()
    #TODO: store data from analyzer in file

    def parse():
        file = open("inputFile.txt")
        
        for line in file.readlines():
            strippedline=line.strip()
            if strippedline != "":
                #this section runs through every line, assessed which info is provided per line,
                #and assigns it to the appropriate variables. Then, all the info is printed
                    parts = strippedline.split(":")
                    if strippedline.startswith('Bacteria Type:'):
                        bacteria_type = parts[1]
                        print(bacteria_type)
                    if strippedline.startswith('Colony Size:'):
                        size = int(parts[1])
                        print(size)
                    if strippedline.startswith('Chance of Resistance:'):
                        resistance = int(parts[1])
                        print(resistance)
                    if strippedline.startswith('Does Horizontal Transfer Occur?:'):
                        gene_transfer = parts[1]
                        print(gene_transfer)
                    if strippedline.startswith('Reproduction Time:'):
                        reproduction = int(parts[1])
                        print(reproduction)
                    if strippedline.startswith('Drug Survival Chance:'):
                        drug_survival = int(parts[1])
                        print(drug_survival)
                
        
    def runImport():
        bacteria_type = input("What type of bacteria is being modeled?")
        print(bacteria_type)
        size = input("What is the initial colony size?")
        print(size)
        resistance = input("What is the initial resistance chance?")
        print(resistance)
        gene_transfer = input("Does the bacteria use horizontal gene transfer to share genetic information, true or false?")
        print(gene_transfer)
        reproduction = input("How long does it take (in minutes) for the bacteria to reproduce once?")
        print(reproduction)
        drug_survival = input("What is the drug survival chance?")
        print(drug_survival)

        if gene_transfer == "true":
            print("Horizontal gene transfer")
            horizontal_transfer = True

        else:
            print("No horizontal gene transfer")
            horizontal_transfer = False


if __name__ == '__main__':
    #runImport()
    runSimulation()

