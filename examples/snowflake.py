from plant.lsystem import Var, Const, LSystem
from plant.symbols import Forward, Rotate as Rot
from PillowTurtle import Turtle
from PIL import Image

class F(Forward):
    def __init__(self):
        super().__init__(2)

    def replace(self):
        return (F(), Rot(60), F(), Rot(-120), F(), Rot(60), F())
    
    def interpret(self, args):
        turtle = args[0]
        turtle.forward(self.dist)

def main():
    im = Image.new("RGB", (1000, 1000))

    turtle = Turtle([750, 250], 180)

    snowflake = LSystem((F(), Rot(-120), F(), Rot(-120), F()))
    snowflake.step(5)
    snowflake.interpret(turtle)

    turtle.draw(im)

    im.show()

if __name__ == "__main__":
    main()
