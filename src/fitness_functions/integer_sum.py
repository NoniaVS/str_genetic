import numpy as np

class IntegerSum(object):
    
    def __init__(self):
        pass
    
    def evaluate_peasant(self, _peasant):
        """Function to compute the fitness of the DNA to sum the length of the array.

        Parameters
        ----------
        _peasant : Peasant type
            Peasant to be evaluated
        """
        
        converted_dna = np.array([int(gen) for gen in _peasant.dna])
        _peasant.fitness = np.abs(np.sum(converted_dna) - converted_dna.shape[0])