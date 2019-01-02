from Tarea3.ArithmeticalTree import *


class AST:
    def __init__(self, listOps, listValues, depth):
        self.listOps = listOps
        self.listValues = listValues
        self.depth = depth
        self.lengthOps = len(listOps)
        self.lengthValues = len(listValues)

    def create(self):
        return ArithmeticalTree(self.listOps, self.listValues, self.depth)



listOps = ['+', '*', '-']
listVal = ["1", "2", "3", "4"]
a = ArithmeticalTree(listOps,listVal,10)
a.printTree()
a.printEvalTree()