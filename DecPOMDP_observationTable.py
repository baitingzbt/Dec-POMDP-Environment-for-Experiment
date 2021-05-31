class FindOneAgentObsTable(object):
    
    def __init__(self, minX, minY, maxX, maxY, blockList, priestDict, hellDict, heavenDict):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY
        self.blockList = blockList
        self.priestDict = priestDict
        self.hellDict = hellDict
        self.heavenDict = heavenDict
    
    def __call__(self, allAgentsSPrimeTable, agent):
        s = allAgentsSPrimeTable[agent]    
        if s in self.priestDict.keys():
            if list(self.heavenDict.keys())[0] == (0, 3):
                return 'heaven-left'
            else:
                return 'heaven-right'
        else:
            x, y = s
            leftIsWall = (x == self.minX or (x-1, y) in self.blockList)
            rightIsWall = (x == self.maxX or (x+1, y) in self.blockList)
            if leftIsWall and rightIsWall:
                return 'both'
            elif leftIsWall:
                return 'left'
            elif rightIsWall:
                return 'right'
            else:
                return 'neither'
        

class ObservationFunction(object):
    
    def __init__(self, findOneAgentObsTable):
        self.findOneAgentObsTable = findOneAgentObsTable
    
    def __call__ (self, allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable):
        allAgentsObsExpected = {agent: self.findOneAgentObsTable(allAgentsSPrimeTable, agent) for agent in allAgentsActionTable.keys()}
        return int(allAgentsObsTable == allAgentsObsExpected)



    
    
    
    
    