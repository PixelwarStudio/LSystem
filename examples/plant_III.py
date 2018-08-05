from PIL import Image
from PillowTurtle import Turtle
from plant.lsystem import LSystem, choose
from plant.symbols import Forward, Rotate as Rot, Push, Pop
from random import randrange

class F(Forward):
    def __init__(self):
        super().__init__(10)

    def replace(self):
        angle = 25.7
        return choose(
            (1, (F(), Push(), Rot(angle), F(), Pop(), F(), Push(), Rot(-angle), F(), Pop(), F())),
            (1, (F(), Push(), Rot(angle), F(), Pop(), F())),
            (1, (F(), Push(), Rot(-angle), F(), Pop(), F()))
        )
 

def main():
    im = Image.new("RGB", (1000, 1000))
    turtle = Turtle([500, 1000], -90)

    lsystem = LSystem((F(),))
    lsystem.step(5)
    lsystem.interpret(turtle)

    turtle.draw(im)
    im.show()

if __name__ == "__main__":
    main()
