import DecPOMDP_transitionTable as tt
class FindOneAgentReward(object):
    
    def __init__(self, priestDict, hellDict, heavenDict, allAgentsInHeaven_after, allAgentsInHell_after):
        self.priestDict = priestDict
        self.hellDict = hellDict
        self.heavenDict = heavenDict
        self.allAgentsInHeaven_after = allAgentsInHeaven_after
        self.allAgentsInHell_after = allAgentsInHell_after
    
    def __call__(self, s, sPrime, normalCost, middleStageDict):
        if self.allAgentsInHeaven_after:
            return normalCost + self.heavenDict[sPrime]
        elif self.allAgentsInHell_after:
            return normalCost + self.hellDict[sPrime]
        else:
            if s == sPrime:
                return normalCost
            elif sPrime in self.priestDict.keys():
                return normalCost + self.priestDict[sPrime]
            else:
                return normalCost + middleStageDict[sPrime]


class RewardFunction(object):
    
    def __init__(self, allAgentsNormalCost, priestDict, hellDict, heavenDict, allAgentsMiddleStageDict):
        self.allAgentsNormalCost = allAgentsNormalCost
        self.allAgentsMiddleStageDict = allAgentsMiddleStageDict
        self.priestDict = priestDict
        self.hellDict = hellDict
        self.heavenDict = heavenDict
    
    def __call__(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable):
        allAgentsInHeaven = tt.checkIfAllInHeaven(allAgentsPositionTable, self.heavenDict)
        allAgentsInHell = tt.checkIfAllInHell(allAgentsPositionTable, self.hellDict)
        if not allAgentsInHeaven and not allAgentsInHell:
            allAgentsInHeaven_after = tt.checkIfAllInHeaven(allAgentsSPrimeTable, self.heavenDict)
            allAgentsInHell_after = tt.checkIfAllInHell(allAgentsSPrimeTable, self.hellDict)
            findAgentReward = FindOneAgentReward(self.priestDict, self.hellDict, self.heavenDict, allAgentsInHeaven_after, allAgentsInHell_after)
            rewardDict = {agent: findAgentReward(allAgentsPositionTable[agent], allAgentsSPrimeTable[agent], self.allAgentsNormalCost[agent], self.allAgentsMiddleStageDict[agent])\
                          for agent in allAgentsPositionTable.keys()}
        else:
            rewardDict = {agent: 0 for agent in allAgentsActionTable.keys()}
        return rewardDict






