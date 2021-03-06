import numpy as np
import math as math


class Genetic:

    def __init__(self, number_parents, max_generation, population, *data):
        self.data = data
        self.number_parents = number_parents
        self.max_generation = max_generation
        self.initial_population = population

        self.current_generation = 0
        self.population_size = self.initial_population.shape
        self.offspring_size = (self.population_size[0]-self.number_parents, self.population_size[1])

        self.history_population_enable = True
        self.history_parents_enable = True

        self.fitness = self.fitness_basic

        self.population_history = []
        self.parents_history = []
        self.current_parents = []
        self.current_population = self.initial_population
        self.current_offspring = []
        self.evolution_trace = []

    def fitness_basic(self, cpl, dpl): 
        apl = zip(cpl, dpl)
        cps = len(cpl)
        value = 0
        for cv in apl:
            value += (cv[1]-cv[0])**2
        return math.sqrt(value)/cps

    def fitness(self, fitness_function):
        self.fitness = fitness_function

    def select(self):
        self.current_parents = np.empty((self.number_parents, self.population_size[1]))
        fitness_list = []
        for i in range(self.population_size[0]):
            fitness_list.append(self.fitness_basic(self.current_population[i], value))
        print(fitness_list)
        self.sorted_idx = np.argsort(fitness_list)
        print(self.sorted_idx)
        for i in range(self.number_parents):
            self.current_parents[i] = self.current_population[self.sorted_idx[i]]
        self.evolution_trace.append(self.current_population[self.sorted_idx[0]])
        #self.current_parents = sorted(fitness_list)[:self.number_parents]
        if self.history_parents_enable:
            self.parents_history.append(self.current_parents)
        print(self.current_parents)

    def crossover(self):
        #print(self.offspring_size)
        self.current_offspring = np.zeros(self.offspring_size)
        #print(self.current_offspring)
        #print(self.current_parents)
        middle = math.floor(self.offspring_size[1]/2)
        #print(middle)
        for i in range(self.offspring_size[0]):
            parent1 = i%self.number_parents
            parent2 = (i+1)%self.number_parents

            self.current_offspring[i][0:middle] = self.current_parents[parent1][0:middle]
            self.current_offspring[i][middle:] = self.current_parents[parent2][middle:]
        print(self.current_offspring)

    def mutate(self):
        print("mutate")
        #print(self.current_offspring)

        for i in range(self.offspring_size[0]):
            for j in range(self.offspring_size[1]):
                self.current_offspring[i][j] += np.random.randint(-2,2)
        print(self.current_offspring)
        self.current_population = np.concatenate((self.current_parents,self.current_offspring), axis=0)

    def bestfit(self):
        fitness_list = []
        for i in range(self.population_size[0]):
            fitness_list.append(self.fitness_basic(self.current_population[i], value))
        self.sorted_idx = np.argsort(fitness_list)
        return self.current_population[self.sorted_idx[0]]
        
    def clear(self):
        self.current_offspring = []
        self.current_parents = []

    def launch(self):
        for i in range(self.max_generation):
            print("Next generation")
            self.current_generation += 1
            self.select()
            self.crossover()
            self.mutate()
            #print(self.current_population)
            print(self.bestfit())
            self.clear()

value = [21, 8, 4, 24]
'''pop = np.random.randint(low=0, high=30, size=(30,4))
gen = Genetic(8, 40, pop)
print(pop)
gen.launch()
print(np.array(gen.evolution_trace))'''
# Add a pattern system

list = [[1,2,3],[[1,2,3],[4,[4,3],3,2]]]



print(list)
