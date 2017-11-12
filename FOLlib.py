import bisect

class Fact:
    factStr = None;
    fact = {}
    def __init__(self,fStr,adjective,variable):
        self.fact[variable] = adjective
        self.factStr = fStr
    def factCheck(variable):
        if (self.fact[variable] != None):
            return True



class Rule:
    ruleStr = None;
    LHS = [];
    RHS = None;
    variables = [];
    def __init__(self,rStr,L,R):
        self.LHS = list(L)
        self.RHS = str(R)
        self.ruleStr = rStr
    def forwardChain(self, facts):
        for atom in LHS:




class Proof:
    def __init__(self):
        print("hi")
