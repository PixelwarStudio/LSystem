from PIL import Image
from PillowTurtle import Turtle
from plant.lsystem import LSystem, ContextVar, Const, Var
from plant.symbols import Forward, Rotate, Push, Pop
from random import randrange

class F(Forward, Const):
    def __init__(self):
        super().__init__(5)

class Rot(Rotate, Var):
    IGNORE = True

    def replace(self):
        return (Rot(-self.angle), )

class Zero(ContextVar):
    def replace(self):
        left, right = self.left_context, self.right_context

        if isinstance(left[0], Zero) and isinstance(right[0], Zero):
            return (Zero(),)
        elif isinstance(left[0], Zero) and isinstance(right[0], One):
            return (One(), Push(), Rot(27.5), F(), One(), F(), One(), Pop())
        elif isinstance(left[0], One) and isinstance(right[0], Zero):
            return (Zero(),)
        elif isinstance(left[0], One) and isinstance(right[0], One):
            return (One(), F(), One())
        return (Zero(),)

class One(ContextVar):
    def replace(self):
        left, right = self.left_context, self.right_context

        if isinstance(left[0], Zero) and isinstance(right[0], Zero):
            return (One(),)
        elif isinstance(left[0], Zero) and isinstance(right[0], One):
            return (One(),)
        elif isinstance(left[0], One) and isinstance(right[0], Zero):
            return (Zero(),)
        elif isinstance(left[0], One) and isinstance(right[0], One):
            return (Zero(),)
        return (One(),)

def main():
    im = Image.new("RGB", (1000, 1000))
    turtle = Turtle([500, 1000], -90)

    lsystem = LSystem((F(), One())*3, context_limit=1)
    lsystem.step(30)
    lsystem.interpret(turtle)

    turtle.draw(im)
    im.show()

if __name__ == "__main__":
    main()