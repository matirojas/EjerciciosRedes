import random
import matplotlib.pyplot as plt
from numpy import random
from random import uniform
from Perceptor import Perceptron


class Learning:

    def __init__(self):
        self.randominputsx = []
        self.randominputsy = []
        self.perceptronanswer = []
        self.randomPesos = (random.uniform(-2, 2), random.uniform(-2, 2))
        self.bias = random.randint(-10,10)
        self.Perceptron = Perceptron(self.randomPesos, self.bias)


    def randomset(self):

       for i in range(0,1000):
           self.randominputsx.append(uniform(0,100))
           self.randominputsy.append(uniform(0,500))
           self.perceptronanswer.append(self.Perceptron.feed(self.randominputsx[i],self.randominputsy[i]))

    def plot(self):
        self.randomset()
        plt.scatter(self.randominputsx,self.randominputsy,c=self.perceptronanswer)
        x= range(0,101)
        y = []
        for i in range(0,101):
            y.append(self.fun(x[i]))
        plt.plot(x,y)
        plt.show()


    def fun(self,x):
        y = 2*x + 1
        return y

L = Learning()
L.plot()
