from src.Fitness import fitness
import random
import numpy as np

def genetic_algorithm(initial_workers, prob_mutation, prob_crossover, objective_fitness, number_survivors, length):
    initial_fitness = fitness(initial_workers)
    initial_fitness.sort()
    current_fitness = initial_fitness[-1]
    workers = initial_workers
    k = 0
    while current_fitness < objective_fitness :

        k +=1

        '''
        First do the crossover
        '''
        workers_new = []
        i = 0
        len_workers = len(workers)
        while len_workers > 1:
            len_workers = len(workers)

            if i >= len_workers:
                break

            j = i+1
            while j < len_workers:
                num = random.random()
                if num < prob_crossover:
                    cross_point = random.randint(0, length-1)
                    workers_new.append(workers[i][:cross_point] + workers[j][cross_point:])
                    workers_new.append(workers[j][:cross_point] + workers[i][cross_point:])
                    cross_point_2 = random.randint(0, length//2 - 1)
                    cross_point_3 = random.randint(length//2, length)
                    workers_new.append(workers[i][:cross_point_2] + workers[j][cross_point_2:cross_point_3]+workers[i][cross_point_3:])
                    workers_new.append(workers[j][:cross_point_2] + workers[i][cross_point_2:cross_point_3] + workers[j][cross_point_3:])
                    workers.remove(workers[i])
                    workers.remove(workers[j-1])
                    len_workers = len(workers)
                else:
                    j += 1
            i += 1

        new_population = workers + workers_new

        '''
        Mutation over new population
        '''
        for i in range(len(new_population)):
            num = random.random()
            if num < prob_mutation:
                element_mutated = random.randint(0, length-1)
                listed_string = list(new_population[i])
                if listed_string[element_mutated] == '0':
                    listed_string[element_mutated] = '1'
                else:
                    listed_string[element_mutated] = '0'
                mutated_worker = ''
                for x in listed_string:
                    mutated_worker +=''+x
                new_population[i] = mutated_worker

        '''
        Selection of the best workers
        '''

        fitness_values = fitness(new_population)
        sorted_list = list(reversed(np.argsort(fitness_values)))

        final_population = []
        for i in range(len(sorted_list)):
            final_population.append(new_population[sorted_list[i]])

        workers = final_population[:number_survivors]
        current_fitness = fitness(workers)[0]

    print('ALGORITHM FINISHED')
    print('The final fitness is', current_fitness, 'it has been reached in ', k, 'generations of workers')
    print('Final worker', workers[0])




