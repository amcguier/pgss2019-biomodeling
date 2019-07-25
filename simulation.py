from pgss.colony import Colony
from pgss.analyze import ColonyAnalyzer
from pgss.cell import Cell
from pgss.update_colony import ColonyUpdater

iterations = 10


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

