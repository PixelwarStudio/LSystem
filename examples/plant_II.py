from PIL import Image
from PillowTurtle import Turtle
from lsystem import LSystem, Var
from symbols import Forward, Rotate as Rot, Push, Pop

class F(Forward):
    def __init__(self):
        super().__init__(4)
    def replace(self):
        return (F(), F())

class B(Var):
    def replace(self):
        angle = 20
        return (F(), Push(), Rot(angle), B(), Pop(), F(), Push(), Rot(-angle), B(), Pop(), Rot(angle), B())

def main():
    im = Image.new("RGB", (1000, 1000))
    turtle = Turtle([500, 1000], -90)

    lsystem = LSystem((B(), ))
    lsystem.step(7)
    lsystem.interpret(turtle)

    turtle.draw(im)
    im.show()

if __name__ == "__main__":
    main()