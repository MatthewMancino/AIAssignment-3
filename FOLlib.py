import bisect

class Fact:
    factStr = None;
    fact = {}
    constant = None;
    def __init__(self,fStr,predicate,constant):
        self.fact[constant] = predicate
        self.predicate = predicate
        self.factStr = fStr
    def factCheck(variable):
        if (self.fact[variable] != None):
            return True



class Rule:
    ruleStr = None;
    LHS = [];
    RHS = None;
    RHS_predicate
    variables = {};
    LHS_predicates = []
    def __init__(self,rStr,L,R):
        self.LHS = list(L)
        for atom in LHS:
            B = string.split(atom,"(")
            self.LHS_predicates.append(B.pop(0))
            variables[string.split(B,")").pop(0)] = None;
        self.RHS = str(R)
        H = string.split(atom,"(")
        self.RHS_predicate = H.pop(0)
        self.ruleStr = rStr
    def forwardChain(self, facts):
        atoms_verified = 0;
        for atom in LHS:                                        #Each atom in LHS
            B = string.split(atom,"(")
            atom_predicate = B.pop(0)                           #Splits strings
            atom_variable = string.split(B,")").pop(0)
            if (variables[atom_variable] == None):              #If variable is not set
                for fact in facts:
                    if(fact.predicate == atom_predicate):
                        variables[atom_variable] = fact.constant
                        atoms_verified++
                        break
                    else:
                        return
            else:                                               #Find exact fact
                for fact in facts:
                    if(fact.factStr == atom):
                        atoms_verified++
                        break
                    else:
                        return

        if (atoms_verified == len(LHS)):
            print("ATOMS verified --- firing rule")
            for a in variables
                if (a in RHS):
                    RHS = string.replace(RHS,str(a),str(variables[a])
            facts.append(Fact(RHS,RHS_predicate,variables[a]))
        return





class Proof:
    def __init__(self):
        print("hi")
