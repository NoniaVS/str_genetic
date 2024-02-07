import numpy as np
import matplotlib.pyplot as plt

from src import GeneticAlgorithm
from src.peasants import SimplePeasant, FFNNPeasant
from src.fitness_functions import IntegerSum, FFNNModelFitness
from src.crossovers import OnePointCrossover
from src.mutators import OneGenMutator


if __name__ == "__main__":
    
    if True:
        
        """
        This algorithm generates large strings of ones or zeros and triest to 
        evolve to a string with only ones.
        """
        
        dna_feat = {"length": 200,
                    "ref": np.array([0, 1]),
                    "ref_prob": None}
        
        population_feat = {"peasant_number": 200,
                           "generations": 1000,
                           "surv_prop": 0.75}
        
        GA = GeneticAlgorithm(dna_features = dna_feat,
                              population_features = population_feat,
                              peasant = SimplePeasant,
                              fitness_function = IntegerSum(),
                              crossover = OnePointCrossover(),
                              mutator = OneGenMutator(mutation_prob = 0.2),
                              print_evolution = False)
        
        GA.evolve_population()
        
        fig, ax = plt.subplots(1, 1, figsize=(10,10))
        
        evolution = GA.evolution_fitness
        ax.plot(-np.log(evolution[:, 0]), label = "best")
        ax.plot(-np.log(np.mean(evolution, axis = 1)), label = "mean")
        
        plt.legend()
        plt.show()
        
    
    # Simple FFNN algorithm to distinguis between positive and negative values
    if False:
        dna_feat = {"length": 3,
                    "ref": np.array([0, 2, 4, 6, 8]),
                    "ref_prob": np.array([0.3] + [0.7/4] * 4)}
        
        
        population_feat = {"peasant_number": 20,
                           "generations": 1000,
                           "surv_prop": 0.75}
        
        samples = 1000
        inp_data = np.zeros((samples, 1))
        out_data = np.zeros(samples)
        for es in range(samples):
            number = np.random.rand()
            mult = np.random.rand()
            
            target_number = (number - mult)*10
            inp_data[es, 0] = target_number
            if target_number >= 0:
                out_data[es] = 1
            else:
                out_data[es] = 0
        
        GA = GeneticAlgorithm(dna_features = dna_feat,
                              population_features = population_feat,
                              peasant = FFNNPeasant,
                              fitness_function = FFNNModelFitness(inp_data = inp_data,
                                                                  out_data = out_data),
                              crossover = OnePointCrossover(),
                              mutator = OneGenMutator(mutation_prob = 0.2),
                              print_evolution = True)
        
        GA.evolve_population()
        
        fig, ax = plt.subplots(1, 1, figsize=(10,10))
        
        evolution = GA.evolution_fitness
        ax.plot(-np.log(evolution[:, 0]), label = "best")
        ax.plot(-np.log(np.mean(evolution, axis = 1)), label = "mean")
        
        plt.legend()
        plt.show()