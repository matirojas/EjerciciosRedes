from random import *
from random import choice
from math import floor
from Tarea3.ArithmeticalTree import *
from sklearn.utils import shuffle
import matplotlib.pyplot as plt


def fitness(self, tree):
    return tree.evalTree()

# This class represents all the Genetic Algorithm, step by step.
class Algorithm:

    # First we started the Algorithm filling the poblation.
    def __init__(self, numberOfGenes, numberOfPopulation, mutationRate, expectedResult, ops, values, depth):
        self.fitnessList = []
        self.population = []
        self.counter = 0
        self.numberOfGenes = numberOfGenes
        self.numberOfPopulation = numberOfPopulation
        self.mutationRate = mutationRate
        self.genes = []
        self.ops = ops
        self.values = values
        self.depth = depth
        self.expectedResult = expectedResult

        for j in range(numberOfPopulation):
            self.population.append(ArithmeticalTree(random.choice(self.ops), random.choice(self.values), self.depth))
        self.fillFitnessList()
        self.start()

    def fillFitnessList(self):
        listOfFitness = []
        for k in range(len(self.population)):
            listOfFitness[k] = fitness(self.population[k])

    def start(self):
        arreglo = []
        while True:
            best = 0
            for k in range(len(self.population)):
                if self.fitnessList[k] == self.expectedResult:
                    print("Se encontró el arbol correcto, es: " + self.population[k].printTree())
                    print("El algoritmo tuvo que generar " + str(
                        self.counter) + " poblaciones nuevas para encontrar el arbol correcto.")
                    arreglo.append(best)
                    plt.plot(arreglo)
                    plt.xlabel("Generación")
                    plt.ylabel("Best fitness")
                    plt.title("Medición algoritmo")
                    plt.show()
                    return
            arreglo.append(best)
            self.reproduction()


    def reproduction(self):
        children = []
        parents = []
        numberOfParents = len(self.population) * 2
        tournamentK = floor(len(self.population) * 0.75)
        for j in range(numberOfParents):
            winner = self.tournament_selection(shuffle(self.population), tournamentK)
            parents.append(self.population[winner])

        for k in range(0, numberOfParents, 2):
            childrenAux = []
            father = parents[k]
            mother = parents[k + 1]
            mixingPoint = randint(0, self.numberOfGenes)
            for t in range(0, self.numberOfGenes):
                if t < mixingPoint:
                    childrenAux.append(father[t])
                else:
                    childrenAux.append(mother[t])
                for j in range(len(childrenAux)):
                    if random() < self.mutationRate:
                        childrenAux[j] = choice(self.genes)
            children.append(childrenAux)
        self.population = children
        self.fillFitnessList()
        self.counter += 1

    def tournament_selection(self, population, k):
        winner = None
        if k == 0:
            winner = 0
        for i in range(0, k):
            index = randint(0, k)
            if winner is None or self.fitnessList[index] > self.fitnessList[winner]:
                winner = index
        return winner



