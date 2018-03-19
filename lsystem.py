"""
Module for handle lsystems.
"""
from random import random
from functools import reduce

class LSystem(object):
    """A simple LSystem without extras"""
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules
        self.state = self.axiom
        self.generation = 0
    
    def step(self, steps=1):
        """Translate the current state into a new state by applying the rules. 

        Args:
            steps (int): Indicate how many times the rules will be applied.
        """
        for _ in range(steps):
            new_state = ""
            for symbol in self.state:
                if symbol in self.rules:
                    new_state += self._get_successor(symbol)
                else:
                    new_state += symbol
            self.state = new_state
        self.generation += steps
    
    def reset(self):
        """Reset the state to axiom."""
        self.axiom = self.state
    
    def _get_successor(self, symbol):
        """Find the proper rule for the symbol.

        Args:
            symbol (str): The symbol.

        Returns:
            str: The successor of the symbol.
        """
        
        return self.rules[symbol]

    def __len__(self):
        return len(self.state)

    def __str__(self):
        return self.state

    def __getitem__(self, n):
        return self.state[n]

    def __iter__(self):
        return iter(self.state)

class ProbLSystem(LSystem):
    """A stochastic LSystem."""
    def __init__(self, axiom, rules):
        super().__init__(axiom, rules)

        self.total = {}
        for symbol, successors in self.rules.items():
            self.total[symbol] = 0
            for successor in successors:
                self.total[symbol] += successor[0]

    def _get_successor(self, symbol):
        variants = self.rules[symbol]
        
        choosen_variant = random() * self.total[symbol]

        sum_prev = 0
        for variant in variants:
            sum_prev += variant[0]
            if sum_prev >= choosen_variant:
                return variant[1]

class ContexLSystem(LSystem):
    pass

class ParametricLSystem(LSystem):
    pass

