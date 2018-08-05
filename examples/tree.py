from PIL import Image
from plant.lsystem import LSystem, Const, Var
from plant.symbols import Rotate as Rot, Push, Pop
from PillowTurtle import Turtle
from random import randint

class Branch(Var):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def replace(self):
        w = int(self.width/2)
        if 27 > self.length:
            return (
                self,
                Push(), Rot(randint(-30, 30)), Leaf(), Pop(),
                Push(), Rot(randint(-30, 30)), Leaf(), Pop(),
                Push(), Rot(randint(-30, 30)), Leaf(), Pop()
            )
        return (
            self,
            Push(), Rot(-45), Branch(self.length*.54, w), Pop(),
            Push(), Rot(-19), Branch(self.length*.52, w), Pop(),
            Push(), Rot(5), Branch(self.length*.49, w), Pop(),
            Push(), Rot(19), Branch(self.length*.51, w), Pop(),
            Push(), Rot(62), Branch(self.length*.45, w), Pop()
        )

    def interpret(self, args):
        turtle = args[0]
        turtle.color = (85, 26, 0)
        turtle.width = self.width
        turtle.forward(self.length)

class Leaf(Const):
    def interpret(self, args):
        turtle = args[0]
        turtle.color = (10, 230, 40)
        turtle.width = 2
        turtle.forward(10)

def main():
    im = Image.new("RGB", (1000, 1000))
    turtle = Turtle([500, 1000], -90)

    system = LSystem(
        axiom=(Branch(300, 20), ) 
    )

    system.step(7)
    system.interpret(turtle)

    turtle.draw(im)
    im.show()

if __name__ == "__main__":
    main()