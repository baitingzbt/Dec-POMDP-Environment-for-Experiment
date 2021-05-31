def checkIfAllInHeaven(allAgentsPositionTable, heavenDict):
    if all(pos in heavenDict.keys() for pos in allAgentsPositionTable.values())\
        and len(set(allAgentsPositionTable.values())) == 1:
        return True
    else:
        return False
    
def checkIfAllInHell(allAgentsPositionTable, hellDict):
    if all(pos in hellDict.keys() for pos in allAgentsPositionTable.values())\
        and len(set(allAgentsPositionTable.values())) == 1:
        return True
    else:
        return False


class FindSPrime(object):
    
    def __init__(self, minX, minY, maxX, maxY, blockList, hellDict, heavenDict):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY
        self.blockList = blockList
        self.hellDict = hellDict
        self.heavenDict = heavenDict
    
    def __call__(self, s, action):
        x, y = s
        dx, dy = action
        sPrimeConsideringBoundary = (max(self.minX, min(x+dx, self.maxX)), max(self.minY, min(y+dy, self.maxY)))
        sPrime = s if sPrimeConsideringBoundary in self.blockList else sPrimeConsideringBoundary
        return sPrime


class TransitionFunction(object):
    
    def __init__(self, checkIfAllInHeaven, checkIfAllInHell, findSPrime):
        self.checkIfAllInHeaven = checkIfAllInHeaven
        self.checkIfAllInHell = checkIfAllInHell
        self.findSPrime = findSPrime

    def __call__(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable):
        allAgentsInHeaven = self.checkIfAllInHeaven(allAgentsPositionTable, self.findSPrime.heavenDict)
        allAgentsInHell = self.checkIfAllInHell(allAgentsPositionTable, self.findSPrime.hellDict)
        if allAgentsInHeaven or allAgentsInHell:
            allSPrimeExpected = allAgentsPositionTable
        else:
            allSPrimeExpected = {agent: self.findSPrime(allAgentsPositionTable[agent], allAgentsActionTable[agent]) for agent in allAgentsActionTable.keys()}
        
        return int(allSPrimeExpected == allAgentsSPrimeTable)


