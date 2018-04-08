from symbols import Forward, Rotate, Pop, Push, Var
from PIL import Image
from PillowTurtle import Turtle
from lsystem import LSystem

class F(Forward):
    def __init__(self):
        super().__init__(10)

class A(Var):
    def replace(self):
        return (X(), Rotate(15))*6

class X(Var):
    def replace(self):
        return (Push(), F()) + (Rotate(15), F())*3 + (Push(), Rotate(3*-15), X(), Rotate(-15), Y(), Pop(), Rotate(5*15), F(), Rotate(8*15), F()) + (Rotate(-15), F())*3 + (Pop(), )

class Y(Var):
    def replace(self):
        return (Push(), F()) + (Rotate(15), F())*3 + (Push(), Rotate(3*-15), Y(), Pop(), Rotate(5*15), F(), Rotate(8*15), F()) + (Rotate(-15), F())*3 + (Pop(), )

def main():
    im = Image.new("RGB", (1000, 1000))
    
    turtle = Turtle()
    turtle.pos = [500, 500]

    kolam = LSystem((A(), )*4)
    kolam.step(14)
    kolam.interpret(turtle)

    turtle.draw(im)

    im.show()

if __name__ == "__main__":
    main()