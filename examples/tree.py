from PIL import Image
from lsystem import LSystem, Const, Var
from PillowTurtle import Turtle
from random import randint

turtle = Turtle()

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

    def interpret(self):
        turtle.color = (85, 26, 0)
        turtle.width = self.width
        turtle.forward(self.length)

class Leaf(Const):
    def interpret(self):
        turtle.color = (10, 230, 40)
        turtle.width = 2
        turtle.forward(10)

class Rot(Const):
    def __init__(self, angle):
        self.angle = angle
    
    def interpret(self):
        turtle.rotate(self.angle)

class Pop(Const):
    def interpret(self):
        turtle.pop()

class Push(Const):
    def interpret(self):
        turtle.push()

def main():
    im = Image.new("RGB", (1000, 1000))

    turtle.x = 500
    turtle.y = 1000
    turtle.rot = -90

    system = LSystem(
        axiom=(Branch(500, 20), ) 
    )

    system.step(7)
    system.interpret()

    turtle.draw(im)
    im.show()

if __name__ == "__main__":
    main()