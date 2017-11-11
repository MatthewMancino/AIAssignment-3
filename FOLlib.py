import bisect

class Fact:
    fact = {}
    name = None
    def __init__(self,adjective,content):
        self.fact[content] = adjective
        self.name = adjective
    def factCheck(content):
        if (self.fact[content] != None):
            return True



class Rule:
    LHS = {};
    RHS = {};
    variables = [];
    def __init__(self):
        print("hi")
    def forwardChain(self, facts):
        for a in facts:
            bisect





class Proof:
    def __init__(self):
        print("hi")
