from PIL import Image
from PillowTurtle import Turtle
from plant.lsystem import LSystem, ContextVar
from plant.symbols import Forward, Rotate, Push, Pop
from random import randrange

class F(Forward):
    def __init__(self):
        super().__init__(30)

class Rot(Rotate):
    def replace(self):
        self.angle *= -1
        return (self, )

class Zero(ContextVar):
    def replace(self):
        neighbors = self.neighbors
        if None in neighbors:
            return (Zero(), )
        if isinstance(neighbors[0], Zero):
            if isinstance(neighbors[1], Zero):
                return (One(), )
            return (One(), Push(), Rot(-16), F(), One(), F(), One(), Pop())
        if isinstance(neighbors[1], Zero):
            return (Zero(), )
        return (One(), F(), One()) 

class One(ContextVar):
    def replace(self):
        neighbors = self.neighbors
        if None in neighbors:
            return (One(), )
        if isinstance(neighbors[0], One) or isinstance(neighbors[1], One):
            return (Zero(), )
        
        return (One(), )

def main():
    im = Image.new("RGB", (1000, 1000))
    turtle = Turtle([500, 1000], -90)

    lsystem = LSystem((F(), One())*3)
    lsystem.step(50)
    lsystem.interpret(turtle)
    print(lsystem[5].get_neighbors(lsystem))

    turtle.draw(im)
    im.show()

if __name__ == "__main__":
    main()