import attr

@attr.s
class LSystem(object):
    axiom = attr.ib()
    rules = attr.ib()

    def __attrs_post_init__(self):
        self.state = self.axiom
        self.generation = 0

    def step(self, steps=1):
        for _ in range(steps):
            new_state = ""
            for symbol in self.state:
                if symbol in self.rules:
                    new_state += self.rules[symbol]
                else:
                    new_state += symbol
            self.state = new_state
        self.generation += steps
    
    def reset(self):
        self.axiom = self.state
    
    def _get_successor(self, symbol):
        return self.rules[symbol]
    
    def __len__(self):
        return len(self.state)

    def __str__(self):
        return self.state

    def __getitem__(self, n):
        return self.state[n]

    def __iter__(self):
        return iter(self.state)
