from random import *
from math import floor
import math
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt


# First we create de function that tells how many characters are the same.
def queenFitnessCalcule(currentSequence):
    lenght = len(currentSequence)
    matrix = np.zeros((lenght, lenght))
    for i in range(lenght):
        aux = currentSequence[i]
        matrix[i][aux] = 1
    result = lenght
    exit = 0
    # filas y columnas
    for i in range(lenght):
        for j in range(lenght):
            if matrix[i][j] == 1:
                for k in range(j + 1, lenght):
                    if matrix[i][k] == 1:
                        exit = 1
                    else:
                        continue
                for k in range(i + 1, lenght):
                    if matrix[k][j] == 1:
                        exit = 1
            else:
                continue
        if exit == 1:
            result -= 1
        exit = 0

    for i in range(lenght):
        for j in range(i + 1, lenght):
            if abs(currentSequence[j] - currentSequence[i]) == abs(j - i):
                result -= 1
    return result


# This class represents all the Genetic Algorithm, step by step.
class Algorithm:

    # First we started the Algorithm filling the poblation.
    def __init__(self, numberOfGenes, numberOfPopulation, mutationRate):
        self.fitnessList = []
        self.population = []
        self.counter = 0
        self.numberOfGenes = numberOfGenes
        self.numberOfPopulation = numberOfPopulation
        self.mutationRate = mutationRate
        self.genes = []
        for i in range(numberOfGenes):
            self.genes.append(i)
        for j in range(numberOfPopulation):
            sequence = []
            for k in range(self.numberOfGenes):
                sequence.append(choice(self.genes))
            self.population.append(sequence)
        self.fillFitnessList()
        self.start()

    # This function compares if we find the correct sequence. If we did then return, in another case
    #  it generates a new population with auxiliary functions.
    def start(self):
        arreglo = []
        while True:
            best = 0
            for k in range(len(self.population)):
                if self.fitnessList[k] > best:
                    best = self.fitnessList[k]
                if self.fitnessList[k] == self.numberOfGenes:
                    print("Se encontró la secuencia correcta, es: " + str(self.population[k]))
                    print("El algoritmo tuvo que generar " + str(
                        self.counter) + " poblaciones nuevas para encontrar el valor.")
                    arreglo.append(best)
                    plt.plot(arreglo)
                    plt.xlabel("Generación")
                    plt.ylabel("Best fitness")
                    plt.show()

                    return
            arreglo.append(best)
            self.reproduction()

    def fillFitnessList(self):
        fitness = []
        for j in range(len(self.population)):
            fitness.append(queenFitnessCalcule(self.population[j]))
        self.fitnessList = fitness

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


if __name__ == '__main__':
    Algorithm(4, 10, 0.01)