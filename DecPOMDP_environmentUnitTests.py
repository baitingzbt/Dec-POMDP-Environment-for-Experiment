import sys
sys.path.append('../src/')

import unittest
from ddt import ddt, data, unpack
import DecPOMDP_transitionTable as tt
import DecPOMDP_rewardTable as rt
import DecPOMDP_observationTable as ot




@ddt
class TestMap(unittest.TestCase):

    '''
    1. TRANSITION FUNCTION
    '''	
    
   # base case
    @data(
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 2), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (1, 1)}, 1),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (1, 2), 'agentTwo': (1, 2)}, 1),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 0)}, {'agentOne': (1, 2), 'agentTwo': (1, 2)}, 1),
        )
    @unpack
    def test_transitionFunction_1m(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime)    
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)

    
    @data(
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (1, 2), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (0, 2), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (0, 1)}, 0),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (1, 3), 'agentTwo': (1, 1)}, 0),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 0)}, {'agentOne': (1, 0), 'agentTwo': (1, 2)}, 0),
        )
    @unpack
    def test_transitionFunction_1n(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime) 
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
   
    
    # change starting points (not in hell or heaven)
    @data(
        ({'agentOne': (1, 1), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (1, 1), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 1), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (0, 2), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (1, 1)}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 2), 'agentTwo': (1, 2)}, 1),
        ({'agentOne': (1, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (1, 1), 'agentTwo': (1, 0)}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (2, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 1), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (0, 2), 'agentTwo': (2, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (0, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 2), 'agentTwo': (0, 3)}, 1),
        )
    @unpack
    def test_transitionFunction_2m(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime) 
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
        
    @data(
        ({'agentOne': (1, 1), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 1), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (1, 0), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (0, 1), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (0, 2), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (1, 2)}, 0),
        ({'agentOne': (2, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 2), 'agentTwo': (1, 1)}, 0),
        ({'agentOne': (1, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (1, 1)}, 0),
        ({'agentOne': (1, 0), 'agentTwo': (2, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 2), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (0, 2), 'agentTwo': (2, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 3), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (2, 2), 'agentTwo': (0, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (1, 2), 'agentTwo': (0, 3)}, 0),
        )
    @unpack
    def test_transitionFunction_2n(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime)   
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
    
    
    # one agent in heaven/hell, the other one is not
    @data(
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 3), 'agentTwo': (1, 1)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (0, 3), 'agentTwo': (1, 2)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, -1), 'agentTwo': (0, 1)}, {'agentOne': (0, 2), 'agentTwo': (1, 2)}, 1),
        
        ({'agentOne': (1, 1), 'agentTwo': (2, 3)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (1, 1), 'agentTwo': (2, 3)}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (2, 3)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 1), 'agentTwo': (2, 3)}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (2, 3)}, {'agentOne': (0, 1), 'agentTwo': (0, -1)}, {'agentOne': (1, 1), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (0, 2), 'agentTwo': (0, 3)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (0, 2)}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 2), 'agentTwo': (0, 3)}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 2), 'agentTwo': (0, 3)}, 1),
        )
    @unpack
    def test_transitionFunction_3m(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime) 
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
    @data(
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (1, 3), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (2, 1), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 4), 'agentTwo': (1, 1)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 3), 'agentTwo': (1, 2)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (1, 2)}, {'agentOne': (0, -1), 'agentTwo': (0, 1)}, {'agentOne': (0, 1), 'agentTwo': (1, 1)}, 0),
        
        ({'agentOne': (1, 1), 'agentTwo': (2, 3)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (0, 1), 'agentTwo': (2, 3)}, 0),
        ({'agentOne': (1, 0), 'agentTwo': (2, 3)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (3, 1), 'agentTwo': (2, 3)}, 0),
        ({'agentOne': (1, 0), 'agentTwo': (2, 3)}, {'agentOne': (0, 1), 'agentTwo': (0, -1)}, {'agentOne': (2, 1), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (0, 2), 'agentTwo': (0, 3)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 1), 'agentTwo': (0, 2)}, 0),
        ({'agentOne': (2, 2), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 1), 'agentTwo': (0, 2)}, 0),
        ({'agentOne': (2, 2), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 1), 'agentTwo': (0, 2)}, 0),
        )
    @unpack
    def test_transitionFunction_3n(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime) 
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
    
   
    # one in heaven/hell, the other one is in hell/heaven, but not together
    @data(
        ({'agentOne': (2, 3), 'agentTwo': (0, 3)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (0, 3)}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (0, 3)}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (0, 3)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (2, 3)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 3), 'agentTwo': (2, 2)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (0, 3), 'agentTwo': (2, 3)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, -1), 'agentTwo': (0, 1)}, {'agentOne': (0, 2), 'agentTwo': (2, 3)}, 1),
        )
    @unpack
    def test_transitionFunction_4m(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime)    
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
    @data(
        ({'agentOne': (2, 3), 'agentTwo': (0, 3)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (1, 3), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (2, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (2, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (2, 1), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (2, 3)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 4), 'agentTwo': (1, 1)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 3), 'agentTwo': (1, 2)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, -1), 'agentTwo': (0, 1)}, {'agentOne': (0, 1), 'agentTwo': (1, 1)}, 0),
        )
    @unpack
    def test_transitionFunction_4n(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime)    
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
       
    # both in heaven / both in hell
    @data(
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, -1), 'agentTwo': (0, 1)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, 1),
        )
    @unpack
    def test_transitionFunction_5m(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime) 
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
    @data(
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (1, 3), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (2, 1), 'agentTwo': (2, 2)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 4), 'agentTwo': (1, 1)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 3), 'agentTwo': (1, 2)}, 0),
        ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, -1), 'agentTwo': (0, 1)}, {'agentOne': (0, 1), 'agentTwo': (1, 1)}, 0),
        )
    @unpack
    def test_transitionFunction_5n(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        findSPrime = tt.FindSPrime(0, 0, 2, 3, [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(2, 3): -10}, {(0, 3): 10})
        transitionFunction = tt.TransitionFunction(tt.checkIfAllInHeaven, tt.checkIfAllInHell, findSPrime) 
        calculatedResult=transitionFunction(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
        



    
    @data(
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {(2, 3): -10}, True),
        ({'agentOne': (2, 2), 'agentTwo': (2, 3)}, {(2, 3): -10}, False),
        ({'agentOne': (1, 2), 'agentTwo': (2, 3)}, {(2, 3): -10}, False),
        ({'agentOne': (1, 1), 'agentTwo': (2, 2)}, {(2, 3): -10}, False),
        
        ({'agentOne': (1, 1), 'agentTwo': (1, 1)}, {(1, 1): -10}, True),
        ({'agentOne': (2, 2), 'agentTwo': (2, 2)}, {(2, 2): -10}, True),
        ({'agentOne': (0, 2), 'agentTwo': (0, 2)}, {(0, 2): -10}, True),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {(1, 2): -10}, True),
        
        ({'agentOne': (2, 3), 'agentTwo': (1, 1)}, {(1, 1): -10}, False),
        ({'agentOne': (2, 2), 'agentTwo': (2, 3)}, {(2, 2): -10}, False),
        ({'agentOne': (1, 2), 'agentTwo': (0, 2)}, {(0, 2): -10}, False),
        ({'agentOne': (1, 1), 'agentTwo': (1, 2)}, {(1, 2): -10}, False),
        )
    @unpack
    def test_checkIfAllInHeaven(self, allAgentsPositionTable, heavenDict, expectedResult):
        calculatedResult=tt.checkIfAllInHeaven(allAgentsPositionTable, heavenDict)
        self.assertEqual(calculatedResult, expectedResult)

    @data(
        ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {(2, 3): -10}, True),
        ({'agentOne': (2, 2), 'agentTwo': (2, 3)}, {(2, 3): -10}, False),
        ({'agentOne': (1, 2), 'agentTwo': (2, 3)}, {(2, 3): -10}, False),
        ({'agentOne': (1, 1), 'agentTwo': (2, 2)}, {(2, 3): -10}, False),
        
        ({'agentOne': (1, 1), 'agentTwo': (1, 1)}, {(1, 1): -10}, True),
        ({'agentOne': (2, 2), 'agentTwo': (2, 2)}, {(2, 2): -10}, True),
        ({'agentOne': (0, 2), 'agentTwo': (0, 2)}, {(0, 2): -10}, True),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {(1, 2): -10}, True),
        
        ({'agentOne': (2, 3), 'agentTwo': (1, 1)}, {(1, 1): -10}, False),
        ({'agentOne': (2, 2), 'agentTwo': (2, 3)}, {(2, 2): -10}, False),
        ({'agentOne': (1, 2), 'agentTwo': (0, 2)}, {(0, 2): -10}, False),
        ({'agentOne': (1, 1), 'agentTwo': (1, 2)}, {(1, 2): -10}, False),
        )
    @unpack
    def test_checkIfAllInHell(self, allAgentsPositionTable, hellDict, expectedResult):
        calculatedResult=tt.checkIfAllInHell(allAgentsPositionTable, hellDict)
        self.assertEqual(calculatedResult, expectedResult)
    


    '''
    2. REWARD FUNCTION
    '''
    
    @data(
       ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (2, 2)}, {'agentOne': -0.1, 'agentTwo': -0.1}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 2), 'agentTwo': (2, 2)}, {'agentOne': -0.1, 'agentTwo': -0.1}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (1, 1)}, {'agentOne': -0.1, 'agentTwo': -0.1}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': -0.1, 'agentTwo': -0.1}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 0)}, {'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': -0.1, 'agentTwo': -0.1}),
        )
    @unpack
    def test_rewardFunction_1(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_1 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.1}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_1(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    
    # change normal costs
    @data(
       ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 2), 'agentTwo': (2, 2)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 2), 'agentTwo': (2, 2)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': (0, 2), 'agentTwo': (1, 1)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, 0)}, {'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
        )
    @unpack
    def test_rewardFunction_2(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_2 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.2}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_2(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)  

    

    # one agent entering priest
    @data(
       ({'agentOne': (1, 1), 'agentTwo': (1, 2)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (2, 2)}, {'agentOne': -2.1, 'agentTwo': -0.2}),
        ({'agentOne': (1, 2), 'agentTwo': (1, 1)}, {'agentOne': (0, 1), 'agentTwo': (0, -1)}, {'agentOne': (1, 2), 'agentTwo': (1, 0)}, {'agentOne': -0.1, 'agentTwo': -2.2}),
        )
    @unpack
    def test_rewardFunction_3(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_3 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.2}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_3(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    
    
    # both agents entering priest
    @data(
       ({'agentOne': (1, 1), 'agentTwo': (1, 1)}, {'agentOne': (0, -1), 'agentTwo': (0, -1)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)},  {'agentOne': -2.1, 'agentTwo': -2.2})
        )
    @unpack
    def test_rewardFunction_4(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_4 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.2}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_4(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    
    # already in priest, after move, in priest again (move into a block or stayed)
    @data(
       ({'agentOne': (1, 0), 'agentTwo': (1, 1)}, {'agentOne': (-1, -1), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (1, 1)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
       ({'agentOne': (1, 0), 'agentTwo': (1, 1)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (1, 1)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
       ({'agentOne': (1, 1), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (0, -1)}, {'agentOne': (1, 1), 'agentTwo': (1, 0)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
       ({'agentOne': (1, 1), 'agentTwo': (1, 0)}, {'agentOne': (0, 1), 'agentTwo': (0, -1)}, {'agentOne': (1, 2), 'agentTwo': (1, 0)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
       ({'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (0, 0), 'agentTwo': (0, 0)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
       ({'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': (0, -1), 'agentTwo': (0, -1)}, {'agentOne': (1, 0), 'agentTwo': (1, 0)}, {'agentOne': -0.1, 'agentTwo': -0.2}),
        )
    @unpack
    def test_rewardFunction_5(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_5 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.2}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_5(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)
    
    
    # after move, meeting up in heaven
    @data(
       ({'agentOne': (0, 2), 'agentTwo': (0, 2)}, {'agentOne': (0, 1), 'agentTwo': (0, 1)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 9.9, 'agentTwo': 9.8}),
       ({'agentOne': (0, 3), 'agentTwo': (0, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 9.9, 'agentTwo': 9.8}),
        )
    @unpack
    def test_rewardFunction_6(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_6 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.2}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_6(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    
    # after move, meeting up in hell
    @data(
       ({'agentOne': (2, 2), 'agentTwo': (2, 2)}, {'agentOne': (0, 1), 'agentTwo': (0, 1)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': -10.1, 'agentTwo': -10.2}),
       ({'agentOne': (2, 3), 'agentTwo': (2, 2)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': -10.1, 'agentTwo': -10.2}),
        )
    @unpack
    def test_rewardFunction_7(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_7 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.2}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_7(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    
    # already both in hell before move
    @data(
       ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, 1), 'agentTwo': (0, 1)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, -1), 'agentTwo': (0, -1)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (1, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (-1, 0), 'agentTwo': (1, 0)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 1)}, {'agentOne': (2, 3), 'agentTwo': (2, 3)}, {'agentOne': 0, 'agentTwo': 0}),
              
       
       ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (1, 0)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 1), 'agentTwo': (-1, 0)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, 0), 'agentTwo': (0, 0)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 0, 'agentTwo': 0}),
       ({'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': (0, -1), 'agentTwo': (-1, 0)}, {'agentOne': (0, 3), 'agentTwo': (0, 3)}, {'agentOne': 0, 'agentTwo': 0}),
        )
    @unpack
    def test_rewardFunction_8(self, allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable, expectedResult):
        middleStages = {agent: {state: 0 for state in [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]} for agent in ['agentOne', 'agentTwo']}
        rewardFunction_8 = rt.RewardFunction({'agentOne': -0.1, 'agentTwo': -0.2}, {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10}, middleStages)
        calculatedResult=rewardFunction_8(allAgentsPositionTable, allAgentsActionTable, allAgentsSPrimeTable)
        self.assertEqual(calculatedResult, expectedResult)  
    

    
    
    '''
    3. OBSERVATION FUNCTION
    '''
    
    
    @data(
        # agent one, not in priest
        ({'agentOne': (1, 2), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (0, 1)}, {'agentOne': 'neither', 'agentTwo': 'neither'}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, 0)}, {'agentOne': 'both', 'agentTwo': 'neither'}, 1),
        ({'agentOne': (0, 2), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (0, -1)}, {'agentOne': 'left', 'agentTwo': 'neither'}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (1, 2)}, {'agentOne': (0, 0), 'agentTwo': (1, 0)}, {'agentOne': 'right', 'agentTwo': 'neither'}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (-1, 0)}, {'agentOne': 'both', 'agentTwo': 'neither'}, 1),
        )
    @unpack
    def test_oneAgentObservation_1(self, allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable, expectedResult):
        findOneAgentObsTable = ot.FindOneAgentObsTable(0, 0, 2, 3,  [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(1, 0): -2}, {(0, 3): -10}, {(2, 3): 10})
        observationFunction_1 = ot.ObservationFunction(findOneAgentObsTable)
        calculatedResult=observationFunction_1(allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable)
        self.assertEqual(calculatedResult, expectedResult)
    
    @data(
        # agent two, not in priest
        ({'agentOne': (1, 2), 'agentTwo': (0, 2)}, {'agentOne': (1, 0), 'agentTwo': (0, 1)}, {'agentOne': 'neither', 'agentTwo': 'left'}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (1, 2)}, {'agentOne': (-1, 0), 'agentTwo': (0, 0)}, {'agentOne': 'both', 'agentTwo': 'neither'}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (2, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, -1)}, {'agentOne': 'right', 'agentTwo': 'right'}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (2, 3)}, {'agentOne': (-1, 0), 'agentTwo': (0, 0)}, {'agentOne': 'right', 'agentTwo': 'both'}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (0, 2)}, {'agentOne': (0, -1), 'agentTwo': (1, 0)}, {'agentOne': 'both', 'agentTwo': 'left'}, 1),
        )
    @unpack
    def test_oneAgentObservation_2(self, allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable, expectedResult):
        findOneAgentObsTable = ot.FindOneAgentObsTable(0, 0, 2, 3,  [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(1, 0): -2}, {(0, 3): -10}, {(2, 3): 10})
        observationFunction_2 = ot.ObservationFunction(findOneAgentObsTable)
        calculatedResult=observationFunction_2(allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    @data(
        # agent one, in priest, heaven left
        ({'agentOne': (1, 0), 'agentTwo': (1, 2)}, {'agentOne': (1, 0), 'agentTwo': (0, 1)}, {'agentOne': 'heaven-left', 'agentTwo': 'neither'}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (2, 2)}, {'agentOne': (0, 0), 'agentTwo': (0, -1)}, {'agentOne': 'heaven-left', 'agentTwo': 'right'}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (2, 3)}, {'agentOne': (1, 0), 'agentTwo': (0, -1)}, {'agentOne': 'heaven-left', 'agentTwo': 'both'}, 1),
        )
    @unpack
    def test_oneAgentObservation_3l(self, allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable, expectedResult):
        findOneAgentObsTable = ot.FindOneAgentObsTable(0, 0, 2, 3,  [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10})
        observationFunction_3l = ot.ObservationFunction(findOneAgentObsTable)
        calculatedResult=observationFunction_3l(allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    @data(
        # agent one, in priest, heaven right
        ({'agentOne': (1, 0), 'agentTwo': (1, 2)}, {'agentOne': (0, 1), 'agentTwo': (0, 1)}, {'agentOne': 'heaven-right', 'agentTwo': 'neither'}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (0, 2)}, {'agentOne': (0, -1), 'agentTwo': (0, 0)}, {'agentOne': 'heaven-right', 'agentTwo': 'left'}, 1),
        ({'agentOne': (1, 0), 'agentTwo': (2, 3)}, {'agentOne': (-1, 0), 'agentTwo': (1, 0)}, {'agentOne': 'heaven-right', 'agentTwo': 'both'}, 1),
        )
    @unpack
    def test_oneAgentObservation_3r(self, allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable, expectedResult):
        findOneAgentObsTable = ot.FindOneAgentObsTable(0, 0, 2, 3,  [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(1, 0): -2}, {(0, 3): -10}, {(2, 3): 10})
        observationFunction_3r = ot.ObservationFunction(findOneAgentObsTable)
        calculatedResult=observationFunction_3r(allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    @data(
        # agent two, in priest, heaven left
        ({'agentOne': (1, 2), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (0, 1)}, {'agentOne': 'neither', 'agentTwo': 'heaven-left'}, 1),
        ({'agentOne': (0, 3), 'agentTwo': (1, 0)}, {'agentOne': (0, 0), 'agentTwo': (0, 0)}, {'agentOne': 'both', 'agentTwo': 'heaven-left'}, 1),
        ({'agentOne': (2, 3), 'agentTwo': (1, 0)}, {'agentOne': (-1, 0), 'agentTwo': (0, -1)}, {'agentOne': 'both', 'agentTwo': 'heaven-left'}, 1),
        )
    @unpack
    def test_oneAgentObservation_4l(self, allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable, expectedResult):
        findOneAgentObsTable = ot.FindOneAgentObsTable(0, 0, 2, 3,  [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(1, 0): -2}, {(2, 3): -10}, {(0, 3): 10})
        observationFunction_4l = ot.ObservationFunction(findOneAgentObsTable)
        calculatedResult=observationFunction_4l(allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    @data(
        # agent two, in priest, heaven right
        ({'agentOne': (1, 2), 'agentTwo': (1, 0)}, {'agentOne': (1, 0), 'agentTwo': (0, -1)}, {'agentOne': 'neither', 'agentTwo': 'heaven-right'}, 1),
        ({'agentOne': (2, 2), 'agentTwo': (1, 0)}, {'agentOne': (0, 1), 'agentTwo': (1, 0)}, {'agentOne': 'right', 'agentTwo': 'heaven-right'}, 1),
        ({'agentOne': (0, 2), 'agentTwo': (1, 0)}, {'agentOne': (0, -1), 'agentTwo': (-1, 0)}, {'agentOne': 'left', 'agentTwo': 'heaven-right'}, 1),
        )
    @unpack
    def test_oneAgentObservation_4r(self, allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable, expectedResult):
        findOneAgentObsTable = ot.FindOneAgentObsTable(0, 0, 2, 3,  [(0, 0), (2, 0), (0, 1), (2, 1), (1, 3)], {(1, 0): -2}, {(0, 3): -10}, {(2, 3): 10})
        observationFunction_4r = ot.ObservationFunction(findOneAgentObsTable)
        calculatedResult=observationFunction_4r(allAgentsSPrimeTable, allAgentsActionTable, allAgentsObsTable)
        self.assertEqual(calculatedResult, expectedResult)  
    
    
    
    def tearDown(self):
       pass
 
if __name__ == '__main__':
    unittest.main(verbosity=2)