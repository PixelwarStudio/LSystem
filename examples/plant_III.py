from PIL import Image
from PillowTurtle import Turtle
from lsystem import LSystem, choose
from symbols import Forward, Rotate as Rot, Push, Pop
from random import randrange

class F(Forward):
    def __init__(self):
        super().__init__(10)

    def replace(self):
        angle = 25.7
        variants = (
            (F(), Push(), Rot(angle), F(), Pop(), F(), Push(), Rot(-angle), F(), Pop(), F()),
            (F(), Push(), Rot(angle), F(), Pop(), F()),
            (F(), Push(), Rot(-angle), F(), Pop(), F())
        )
        return variants[randrange(len(variants))]
        #return (F(), Push(), Rot(45), Pop(), F(), Push(), Rot(-45), F(), Pop(), F())
 

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
