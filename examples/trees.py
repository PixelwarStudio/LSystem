from math import sqrt
from plant.lsystem import LSystem, Interpretable, Var, Const
from plant.symbols import Forward, Rotate, Push, Pop
from PIL import Image
from PillowTurtle import Turtle

c = 1
p = 0.3
q = c-p
h = sqrt(p*q)

class R(Rotate, Const):
    pass

class F(Forward, Var):
    def replace(self):
        x = self.dist
        return (
            S(x),
            Push(), R(80), T(10), Pop(),
            Push(), R(-80), T(10), Pop(),
            F(x)
        )

class T(Forward, Var):
    def replace(self):
        x = self.dist
        return (T(x*1.2),)

class S(Forward, Const):
    pass


if __name__ == "__main__":
    im = Image.new("RGB", (1000, 1000))
    turtle = Turtle([500, 1000], -90)

    system = LSystem((F(50), ))
    system.step(14)
    system.interpret(turtle)

    turtle.draw(im)
    im.show()