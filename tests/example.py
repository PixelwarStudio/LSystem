from plant.lsystem import LSystem, Var, Const

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

# LSystems
algae = lambda : LSystem((A(),))
fractal_binary_tree = lambda : LSystem((Zero(),))
koch_snowflake = lambda : LSystem((F(),))