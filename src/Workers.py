import random

class Workers:

    def __init__(self, amount, length):

        self.amount = amount
        self.length = length


    def generate_workers(self):
        '''
        generates a list of random binary strings
        '''

        list_workers = []
        for i in range(self.amount):
            key = ''
            for j in range(self.length):
                num = str(random.randint(0,1))
                key += num
            list_workers.append(key)

        return list_workers
