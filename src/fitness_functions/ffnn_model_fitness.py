"""
Fitness function that trains models and computes the loss
"""

import numpy as np
from copy import deepcopy

class FFNNModelFitness(object):
    
    def __init__(self, **kwargs):
        """FFNNModelFitness constructor
        """
        
        self.__kwargs = deepcopy(kwargs)
        self.__inp_data = deepcopy(self.__kwargs["inp_data"])
        self.__out_data = deepcopy(self.__kwargs["out_data"])
        
        self.__inp_train = None
        self.__out_train = None
        self.__inp_test = None
        self.__out_test = None
        self.__get_random_split()
        
    
    def __get_random_split(self):
        """Split the inp_data and out_data for training and testing
        """
        
        ind = np.arange(0, self.__inp_data.shape[0])
        choices = np.random.choice(ind, int(self.__inp_data.shape[0] * 0.1))
        
        self.__inp_train = np.copy(self.__inp_data)
        self.__out_train = np.copy(self.__out_data)
        self.__inp_train = np.delete(self.__inp_train, choices, axis = 0)
        self.__out_train = np.delete(self.__out_train, choices, axis = 0)
        self.__inp_test = np.copy(self.__inp_data[choices, :])
        self.__out_test = np.copy(self.__out_data[choices])
        
        self.__inp_train, self.__out_train = self.__unison_shuffled_copies(self.__inp_train, self.__out_train)
        self.__inp_test, self.__out_test = self.__unison_shuffled_copies(self.__inp_test, self.__out_test)
        
    
    def __unison_shuffled_copies(self, a, b):
        """Function to shuffle pairs of np.ndarrays

        Parameters
        ----------
        a : np.ndarray
            Array
        b : np.ndarray
            Array

        Returns
        -------
        np.ndarray, np.ndarray
            Shuffled arrays
        """
        
        assert len(a) == len(b)
        p = np.random.permutation(len(a))
    
        return a[p], b[p]
        
    
    def evaluate_peasant(self, _peasant):
        """Function to compute the fitness of the DNA. The functions calls to fit the
        model and test it. The result of the tesing would be the fitness.

        Parameters
        ----------
        _peasant : Peasant type
            Peasant to be evaluated
        """
        
        _peasant.fit_model(self.__inp_train, self.__out_train)
        fitness = _peasant.test_model(self.__inp_test, self.__out_test)
        
        _peasant.fitness = fitness