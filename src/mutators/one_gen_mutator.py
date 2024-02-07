import numpy as np

class OneGenMutator(object):
    
    def __init__(self, **kwargs):
        """OneGenMutator constructor
        """
        
        self.__mutation_probability = kwargs["mutation_prob"]
    
    def mutate_dna(self, _dna, _sele, _prob):
        """Function to mutate the input DNA. The mutation only modifies one gen.
        The probability can be None.

        Parameters
        ----------
        _dna : str
            DNA to be mutated
        _sele : np.ndarray
            Array with the possible selection (DNA will store the index to this array)
        _prob : np.ndarray
            Array with the probabilities to select each index of _sele

        Returns
        -------
        str
            Mutated DNA string
        """
        
        r = np.random.rand()
        if r > self.__mutation_probability:
            return _dna
        
        r = np.random.choice(len(_dna))
        dna = _dna[:r] if r != 0 else ""
        
        if _prob is None:
            dna += str(np.random.choice(range(_sele.shape[0])))
        else:
            dna += str(np.random.choice(range(_sele.shape[0]), p = _prob))
            
        dna += _dna[r+1:] if r+1 < len(_dna) else ""
        
        return dna