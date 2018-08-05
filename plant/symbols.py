from PillowTurtle import Turtle
from plant.lsystem import LSystem, Symbol, Const

# Variables
class Forward(Symbol):
    def __init__(self, dist=5):
        self.dist = dist
    
    def interpret(self, args):
        args[0].forward(self.dist)

class ForwardWithoutDrawing(Forward):
    def interpret(self, args):
        args[0].up()
        super().interpret(self, args)
        args[0].down()

# Constants
class Rotate(Const):
    def __init__(self, angle):
        self.angle = angle
    
    def interpret(self, args):
        args[0].rotate(self.angle)

class Push(Const):
    def interpret(self, args):
        args[0].push()

class Pop(Const):
    def interpret(self, args):
        args[0].pop()