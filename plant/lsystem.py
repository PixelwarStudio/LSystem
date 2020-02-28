"""
Module for handle lsystems and interpret them.
"""
from random import random

class LSystem(object):
    """A simple LSystem"""
    def __init__(self, axiom, context_limit=0):
        self.axiom = axiom
        self.state = self.axiom
        self.context_limit = context_limit

        self.generation = 0
    
    def step(self, steps=1):
        """Translate the current state into a new state by applying the rules. 

        Args:
            steps (int): Indicate how many times the rules will be applied.
        """
        for _ in range(steps):
            new_state = []
            for symbol in self:
                # Update contexts of context-sensitive symbols 
                if isinstance(symbol, ContextVar):
                    symbol.left_context = self.get_left_context(symbol)
                    symbol.right_context = self.get_right_context(symbol)

                if isinstance(symbol, Var):
                    new_state += symbol.replace()
                elif isinstance(symbol, Symbol):
                    new_state.append(symbol)
            self.state = tuple(new_state)
        self.generation += steps

    def get_left_context(self, symbol):
        context = [None]*self.context_limit
        pos = self.state.index(symbol)
        context_size = 0

        i = pos-1
        while i > 0 and context_size < self.context_limit:
            if isinstance(self[i], AbstractPop):
                while not(isinstance(self[i], AbstractPush)):
                    i -= 1
            elif not(self[i].IGNORE):
                context[context_size] = self[i]
                context_size += 1
                i -= 1
            else:
                i -= 1

        return context
    
    def get_right_context(self, symbol):
        context = [None]*self.context_limit
        pos = self.state.index(symbol)
        context_size = 0

        i = pos+1
        while i < len(self) and context_size < self.context_limit:
            if isinstance(self[i], AbstractPush):
                while not(isinstance(self[i], AbstractPop)):
                    i += 1
            elif not(self[i].IGNORE):
                context[context_size] = self[i]
                context_size += 1
                i += 1
            else:
                i += 1

        return context
    
    def reset(self):
        """Reset the state to axiom."""
        self.axiom = self.state
    
    def interpret(self, *args):
        """Interpret every symbol in current state"""
        for symbol in self:
            if isinstance(symbol, Interpretable):
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

class Interpretable(object):
    def interpret(self):
        pass

class Symbol(object):
    IGNORE = False

    def __str__(self):
        return self.__class__.__name__

class Const(Symbol):
    IGNORE = True

class Var(Symbol):
    def replace(self):
        pass

class AbstractPush(Const):
    pass

class AbstractPop(Const):
    pass

class ContextVar(Var):
    def __init__(self):
        self.left_context = []
        self.right_context = []