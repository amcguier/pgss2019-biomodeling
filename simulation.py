from pgss.colony import Colony
from pgss.analyze import ColonyAnalyzer
from pgss.cell import Cell
from pgss.update_colony import ColonyUpdater

iterations = 25
theColony = Colony()
colony

def runSimulation():
   for index in iterations:
       theColony = ColonyUpdater.updateColony(theColony)
       
    
    
    
if __name__ == '__main__':
    runSimulation()

