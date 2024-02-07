import numpy as np
from copy import deepcopy

class GeneticAlgorithm(object):
    
    def __init__(self, **kwargs):
        """Constructor of GeneticAlgorithm class
        """

        self.__kwargs = deepcopy(kwargs) # Always is better to deepcopy the input dictionaries
        
        self.__dna_features = self.__kwargs["dna_features"]
        self.__population_features = self.__kwargs["population_features"]
        self.__fitness_function = self.__kwargs["fitness_function"]
        self.__crossover = self.__kwargs["crossover"]
        self.__mutator = self.__kwargs["mutator"]
        self.__peasant = self.__kwargs["peasant"]
        self.__print_evolution = self.__kwargs.get("print_evolution", True)
        
        ## Population data
        self.__population = self.__generate_population()
        self.__evolution_fitness = None
    
    @property
    def evolution_fitness(self):
        return deepcopy(self.__evolution_fitness)
    
        
    def __generate_population(self):
        """Generates the complete list of Peasants

        Returns
        -------
        list
            List of Peasants
        """
        
        pop_size = self.__population_features["peasant_number"]
        population = []
        for ii in range(pop_size):
            peasant = self.__peasant(dna_features = self.__dna_features)
            population.append(peasant)
            
        return population
    
    
    def evolve_population(self):
        """Function to evolve the first population until convergence or max
        generations
        """
        
        n_generations = self.__population_features["generations"]
        survival_probability = self.__population_features["surv_prop"]
        n_population = len(self.__population)
        self.__evolution_fitness = np.zeros((n_generations, n_population))
        
        for generation in range(n_generations):
            
            # Compute fitness for generation
            for peasant in self.__population:
                self.__fitness_function.evaluate_peasant(peasant)
                
            # Sort population by their fitness and print the dna of the best
            self.__population.sort(key=lambda x: x.fitness)
            if self.__print_evolution:
                print(f"Generation {generation} : DNA {self.__population[0].dna} : Fitness {self.__population[0].fitness}")
            
            # Save generational fitness
            generation_fitness = np.zeros(n_population)
            for enum, peasant in enumerate(self.__population):
                generation_fitness[enum] = peasant.fitness
                
            self.__evolution_fitness[generation, :] = generation_fitness
            if np.abs(self.__population[0].fitness) < 1e-5:
                break
            
            # Select parents
            parent_population = self.__population[:int(n_population*survival_probability)]
            self.__population = []
            
            # Generate offsprings from parents
            for enum in range(n_population):
                par_1, par_2 = np.random.choice(parent_population, 2)
                dna = self.__crossover.generate_dna(par_1, par_2)
                
                # Mutate offspring dna
                dna = self.__mutator.mutate_dna(dna,
                                                _sele = par_1.dna_features["ref"],
                                                _prob = par_1.dna_features["ref_prob"])
                
                peasant = self.__peasant(dna = dna, dna_features = par_1.dna_features)
                self.__population.append(peasant)
        
        self.__evolution_fitness = self.__evolution_fitness[:generation, :]