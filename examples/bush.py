from PIL import Image
from PillowTurtle import Turtle
from lsystem import LSystem
from symbols import Forward, Rotate as Rot, Push, Pop

class F(Forward):
    def __init__(self):
        super().__init__(15)

    def replace(self):
        angle = 25
        return (
            F(), F(), Rot(angle),
            Push(), Rot(angle), F(), Rot(-angle), F(), Rot(-angle), F(), Pop(),
            Rot(-angle),
            Push(), Rot(-angle), F(), Rot(angle), F(), Rot(angle), F(), Pop()
        )

def main():
    im = Image.new("RGB", (1000, 1000))
    turtle = Turtle([500, 1000], -90)

    lsystem = LSystem((F(), ))
    lsystem.step(4)
    lsystem.interpret(turtle)

    turtle.draw(im)
    im.show()

if __name__ == "__main__":
    main()