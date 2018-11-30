from random import *
from math import floor
from sklearn.utils import shuffle


# First we create de function that tells how many characters are the same.
def fitnessCalcule(currentSequence, expectedSequence):
    success = 0
    assert len(currentSequence) == len(expectedSequence)
    for k in range(len(currentSequence)):
        if currentSequence[k] == expectedSequence[k]:
            success += 1
    return success


# This class represents all the Genetic Algorithm, step by step.
class Algorithm:

    # First we started the Algorithm filling the poblation.
    def __init__(self, genes, numberOfGenes, expectedSequence, numberOfPopulation, mutationRate):
        self.fitnessList = []
        self.population = []
        self.counter = 0
        self.genes = genes
        self.numberOfGenes = numberOfGenes
        self.expectedSequence = expectedSequence
        self.numberOfPopulation = numberOfPopulation
        self.mutationRate = mutationRate

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
        while True:
            for k in range(len(self.population)):
                if self.fitnessList[k] == self.numberOfGenes:
                    print("Se encontró la secuencia correcta, es: " + str(self.population[k]))
                    print("El algoritmo tuvo que generar " + str(
                        self.counter) + " poblaciones nuevas para encontrar el valor.")
                    return
            self.reproduction()

    def fillFitnessList(self):
        fitness = []
        for j in range(len(self.population)):
            fitness.append(fitnessCalcule(self.population[j], self.expectedSequence))
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
    prueba = Algorithm(['a', 'e', 'i','o','u','c','f','p','r','l','d'], 14, ['p','a','r','a','l','e','l','e','p','i','p','e','d','o']
                       ,100, 0.01)

