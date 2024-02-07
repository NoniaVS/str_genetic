import numpy as np

class OnePointCrossover(object):
    
    def __init__(self):
        pass
    
    def generate_dna(self, _p1, _p2):
        """Crossover between two dnas by randomly selection one index and mixing them.
        dna_1 = '010011'
        dna_2 = '110100'
        
        index = 3
        
        dna_3 = '010100'

        Parameters
        ----------
        _p1 : Peasant type
            Peasant
        _p2 : Peasant type
            Peasant

        Returns
        -------
        str
            New DNA
        """
        
        assert (len(_p1.dna) == len(_p2.dna))
        
        r = np.random.choice(len(_p1.dna))
        dna = _p1.dna[:r] + _p2.dna[r:]
        
        return dna