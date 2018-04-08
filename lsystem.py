"""
Module for handle lsystems and interpret them.
"""
from random import random

class LSystem(object):
    """A simple LSystem"""
    def __init__(self, axiom):
        self.axiom = axiom
        self.state = self.axiom
        self.generation = 0
    
    def step(self, steps=1):
        """Translate the current state into a new state by applying the rules. 

        Args:
            steps (int): Indicate how many times the rules will be applied.
        """
        for _ in range(steps):
            new_state = []
            for n, symbol in enumerate(self.state):
                # Update neighbors of context-sensitive symbols 
                if isinstance(symbol, ContextVar):
                    symbol.neighbors = symbol.__get_neighbors(n, self)
                new_state += symbol.replace()
            self.state = tuple(new_state)
        self.generation += steps
    
    def reset(self):
        """Reset the state to axiom."""
        self.axiom = self.state
    
    def interpret(self, *args):
        """Interpret every symbol in current state"""
        for symbol in self:
            symbol.interpret(args)

    def __len__(self):
        return len(self.state)

    def __str__(self):
        s = ""
        for symbol in self.state:
            s += str(symbol) + " "

        return s

    def __getitem__(self, n):
        return self.state[n]

    def __iter__(self):
        return iter(self.state)

class Symbol(object):
    def replace(self):
        return (self,)
    
    def interpret(self, *args):
        pass

    def __str__(self):
        return self.__class__.__name__

class Const(Symbol):
    CAN_NEIGHBOR = False

class Var(Symbol):
    CAN_NEIGHBOR = True

class ContextVar(Var):
    def __init__(self):
        self.neighbors = (None, None)
    
    def __get_neighbors(self, pos, lsystem):
        rneighbor, lneighbor = None, None
        lbound, rbound = lambda pos: pos >= 0, lambda pos: pos < len(lsystem)
        
        for i in range(1, max(len(lsystem)-pos, pos)):
            lpos, rpos = pos-i, pos+i

            if lbound(lpos):
                if lneighbor is None and isinstance(lsystem[lpos], Var):
                    lneighbor = lsystem[lpos]
                    if rneighbor is not None:
                        break

            if rbound(lpos):
                if rneighbor is None and isinstance(lsystem[rpos], Var):
                    rneighbor = lsystem[rpos]
                    if lneighbor is not None:
                        break
            
            if not(lbound(lpos)) and not(rbound(rpos)):
                break

        return (lneighbor, rneighbor)

def choose(symbol, *rules):
        total = sum([prob for (prob, rule) in rules])
        choosen_rule = random() * total

        sum_prev = 0
        for (prob, rule) in rules:
            sum_prev += prob
            if sum_prev >= choosen_rule:
                return rule(symbol)
