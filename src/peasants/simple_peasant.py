

import numpy as np
from copy import deepcopy

class SimplePeasant(object):
    
    def __init__(self, **kwargs):
        """ SimplePeasant is more like a container of information in this example. The DNA is a straightfoward
        string of numbers, so there is not more complex functions.
        """
        
        self.__kwargs = deepcopy(kwargs)
        self.__dna_features = self.__kwargs["dna_features"]
        self.__dna = self.__kwargs.get("dna", self.__random_initilization())
        self.__fitness = None
        
    @property
    def dna(self):
        return deepcopy(self.__dna)
        
    @property
    def fitness(self):
        return self.__fitness
    
    @fitness.setter
    def fitness(self, value):
        self.__fitness = value
        
    @property
    def dna_features(self):
        return deepcopy(self.__dna_features)
        
    
    def __random_initilization(self):
        """Function to initialize the SimplePeasant with random DNA

        Returns
        -------
        str
            DNA of this SimplePeasant
        """
        
        dna_length = self.__dna_features["length"]
        random_numbers = np.random.choice(2, dna_length)
        random_dna = [str(gen) for gen in random_numbers]
        
        return "".join(random_dna)