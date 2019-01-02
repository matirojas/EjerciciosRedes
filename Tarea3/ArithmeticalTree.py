import copy
import random


class ArithmeticalTree:
    def __init__(self, listOps, listValues, depth):
        self.random = random.choice([0, 1])
        self.listValues = listValues
        self.listOps = listOps
        self.valueNode = None
        self.r = None
        self.l = None
        self.depth = depth
        self.lengthOps = len(self.listOps)
        self.lengthValues = len(self.listValues)
        self.create()

    def copyTree(self):
        return copy.deepcopy(self)

    def printTree(self):
        print(self.treeToString())

    def evalTree(self):
        return eval(str(self.treeToString()))

    def treeToString(self):
        if self.r is None:
            return self.valueNode
        if self.l is None:
            return self.valueNode
        return "(" + self.l.treeToString() + " " + self.valueNode + " " + self.r.treeToString() + ")"

    def printEvalTree(self):
        print(self.evalTree())

    def create(self):
        if self.random == 0 or self.depth == 0:
            self.valueNode = self.listValues[random.randint(0, self.lengthValues - 1)]
            return
        self.valueNode = self.listOps[random.randint(0, self.lengthOps - 1)]
        self.r = ArithmeticalTree(self.listOps, self.listValues, self.depth - 1)
        self.l = ArithmeticalTree(self.listOps, self.listValues, self.depth - 1)