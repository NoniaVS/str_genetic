from src.Workers import Workers
from src.GeneticAlgorithm import genetic_algorithm

amount = int(input("Enter the number of workers you want at the beginning: "))
length = int(input('Enter the amount of elements in each worker: '))
prob_crossover = float(input('Enter the probability that a crossover happens between two workers: '))
prob_mutation = float(input('Enter the probability that a mutation happens to a worker: '))
number_survivors = int(input('Enter the number of workers you want to save from each generation: '))

workers = Workers(amount, length)
initial_workers = workers.generate_workers()
print(initial_workers)
objective_fitness = length

genetic_algorithm(initial_workers, prob_mutation, prob_crossover, objective_fitness, number_survivors, length)



