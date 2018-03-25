from lsystem import LSystem, Var, Const

# Variables
# Algae
class A(Var):
    def replace(self):
        return (A(), B())

class B(Var):
    def replace(self):
        return (A(),)

# Fractal binary tree
class Zero(Var):
    def replace(self):
        return (One(), SqrBracketOpen(), Zero(), SqrBracketClose(), Zero())

    def __str__(self):
        return "0"

class One(Var):
    def replace(self):
        return (One(),)*2

    def __str__(self):
        return "1"

# Koch snowflake
class F(Var):
    def replace(self):
        return (F(), Plus(), F(), Minus(), Minus(), F(), Plus(), F())

# Constants
class SqrBracketOpen(Const):
    def __str__(self):
        return "["

class SqrBracketClose(Const):
    def __str__(self):
        return "]"

class Plus(Const):
    def __str__(self):
        return "+"

class Minus(Const):
    def __str__(self):
        return "-"

# Taken from https://en.wikipedia.org/wiki/L-system
def test_algae():
    system = LSystem((A(),))
    system.step(7)

    assert str(system).replace(" ", "") == "ABAABABAABAABABAABABAABAABABAABAAB"

def test_fractal_binary_tree():
    system = LSystem((Zero(),))
    system.step(3)

    assert str(system).replace(" ", "") == "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0"

def test_koch_snowflake():
    system = LSystem((F(),))
    system.step(3)

    assert str(system).replace(" ", "") == "F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F+F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F"
