from PillowTurtle import Turtle
from plant.lsystem import LSystem, Symbol, Var, Const, AbstractPush, AbstractPop, Interpretable

class Forward(Symbol, Interpretable):
    def __init__(self, dist=5):
        self.dist = dist
    
    def interpret(self, args):
        args[0].forward(self.dist)

class ForwardWithoutDrawing(Symbol, Interpretable):
    def __init__(self, dist=5):
        self.dist = dist

    def interpret(self, args):
        args[0].up()
        super().interpret(self, args)
        args[0].down()

class Rotate(Symbol, Interpretable):
    def __init__(self, angle):
        self.angle = angle
    
    def interpret(self, args):
        args[0].rotate(self.angle)

class Push(AbstractPush, Interpretable):
    def interpret(self, args):
        args[0].push()

class Pop(AbstractPop, Interpretable):
    def interpret(self, args):
        args[0].pop()