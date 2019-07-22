#from pgss.colony import Colony
from pgss.analyze import ColonyAnalyzer
from pgss.cell import Cell
from pgss.update_colony import ColonyUpdater

iterations = 25
#theColony = Colony()
#colony

def runSimulation():
   pass
    #for index in iterations:
       #theColony = ColonyUpdater.updateColony(theColony)
       
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
        print("Vertical gene transfer")
        horizontal_transfer = False
    
    
if __name__ == '__main__':
    runImport()
    runSimulation()

