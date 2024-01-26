def fitness(list_workers):
    '''
    evaluates the fitness of a list of workers
    '''
    fitness_workers = []

    for i in range(len(list_workers)):
        value = 0
        for j in range(len(list_workers[i])):
            value += int(list_workers[i][j])
        fitness_workers.append(value)

    return fitness_workers