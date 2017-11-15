import bisect
import string
from copy import deepcopy

class Fact:
    factStr = None;
    fact = {}
    constant = None;
    def __init__(self,fStr,predicate,constant):
        self.fact[constant] = predicate
        self.predicate = predicate
        self.factStr = string.strip(fStr)
        self.constant = constant
    def factCheck(variable):
        if (self.fact[variable] != None):
            return True



class Rule:
    ruleStr = None;
    LHS = [];
    RHS = None;
    variables = {};
    LHS_predicates = [];

    #INIT complete
    def __init__(self,rStr,L,R):
        #print(rStr)
        self.LHS = list(L)
        self.variables = {};
        for atom in self.LHS:
            B = string.split(atom,"(")
            self.LHS_predicates.append(B.pop(0))
            varz = string.split(B.pop(0),")").pop(0)

            if "," in varz:
                varz = string.split(varz,",")
                for v in varz:
                    self.variables[v] = None;
                    #print(self.variables)
            else:
                self.variables[varz] = None;
        #print(self.variables)
        self.RHS = str(R)
        l = self.RHS.find("(") + 1
        r = self.RHS.find(")")

        self.RHS_predicate = self.RHS[0:l-1]

        # print(rStr)
        # print(str(self.LHS).strip())
        # print(str(self.LHS_predicates))
        # print(self.variables)
        # print("CREATE     "+self.RHS_predicate)
        self.ruleStr = rStr


    def unification(self,f1,f2):


        if ("," in f2.constant):
            f2_args = string.split(f2.constant,",");
        else:
            f2_args = []
            f2_args.append(f2.constant)


        hold = string.split(f1,"(")
        f1_predicate = hold.pop(0)
        f1_args = string.split(hold.pop(0),")").pop(0)
        if "," in f1_args:
            f1_args = string.split(f1_args,",")


        if(f1_predicate != f2.predicate or len(f1_args) != len(f2_args)):   #If predicate is not sthe same or args diff return none
            return None;
        subs = []
        for a in f1_args:
            if (a in self.variables.keys()):
                if(self.variables[a] == None and f2_args[f1_args.index(a)] not in self.variables.values()):
                    subs.append(a+"|"+f2_args[f1_args.index(a)])
                elif(self.variables[a] != f2_args[f1_args.index(a)]):
                    return None;
                else:
                    subs.append(a+"|"+f2_args[f1_args.index(a)])
            elif(a != f2_args[f1_args.index(a)]):
                return None;
        return subs




    def verifyAtom(self,iAtom,facts):

        #End goal of verify atom is to find a replacement such that all match


        if (iAtom >= len(self.LHS)):                #BASE CASE:IF all atoms are verifed, check to see if fact exists already
            #print(iAtom)
            rhs = self.RHS
            for var in self.variables:
                if (var in rhs):
                    rhs = string.replace(rhs,str(var),str(self.variables[var]))
            for f in facts:
                if rhs in f.factStr:
                    return False;

            return True;

        if (iAtom < len(self.LHS)):
            atom = self.LHS[iAtom]
        # if(iAtom == 2):
        #     print("HELP")
        #     print(atom)

        #KEEPS A copy of the substituitions at the atom level.
        vars_copy = deepcopy(self.variables)
        LHS_copy = deepcopy(self.LHS)


        # print("Atom "+str(iAtom)+ str(LHS_copy))
        #print(str(vars_copy))


        #If there are still facts to be checked on this level
        facts_left = True
        while (True):
            if(facts_left == False):
                #BASE CASE: NO FACTS AVAILIBLE GO UP A ATOM
                return False;
            else:
                #print(atom)
                  #RECURSIVE CASE:
                for fact in facts:
                    #FOR EACH FACT, CHECK IF YOU CAN MAKE FULL OR PARTIAL SUBSTIUTION
                    #print(fact.factStr)
                    if (fact.factStr == atom):
                        if(self.verifyAtom(iAtom+1,facts)):         #Check if fact matches atom
                            return True;
                        else:
                            continue
                    # if (fact.factStr == atom)

                    subs = self.unification(atom,fact);

                    #rint(subs)
                    if (subs == []):                                #Not a failure, but no substitutions
                        if (fact.factStr == atom):
                            if(self.verifyAtom(iAtom+1,facts)):         #Check if fact matches atom
                                return True;
                            else:
                                continue
                        else:
                            continue
                    elif(subs == None):
                        continue
                    else:

                        # print("\nBEFORE  "+str(iAtom))
                        # print(self.LHS)
                        # print(self.variables)



                        #Change bindings
                        for s in subs:
                            subby = string.split(s,"|")
                            self.variables[subby[0]] = subby[1]

                        #print(self.LHS)
                        self.replace()
                        #print(self.LHS)

                        # print("\nAFTER SUB"+str(iAtom))
                        # print(self.LHS)
                        # print(self.variables)

                        atom2 = self.LHS[iAtom]          #If current fact matches atom
                        # print(atom2)
                        # print(fact.factStr)
                        # print(fact.factStr == atom2)
                        # print(iAtom)
                        if (fact.factStr == atom2):                  #VERIFIED
                            if(self.verifyAtom(iAtom+1,facts)):         #recurse
                                return True;
                            else:
                                self.variables = dict(vars_copy)
                                self.LHS = list(LHS_copy)
                                atom = self.LHS[iAtom]

                                # print("\nAFTER REVERT"+str(iAtom))
                                # print(self.LHS)
                                # print(self.variables)
                                #print(atom)
                                continue
                        else:
                            self.variables = vars_copy
                            self.LHS = LHS_copy
                            atom = self.LHS[iAtom]

                            # print("\nBROKEN?")
                            # print(self.LHS)
                            # print(self.variables)
                            # print(atom)
                            continue

                facts_left = False;
                #print("No good facts")

    def replace(self):
        new = list()
        for atom in self.LHS:
            l = atom.find("(")
            r = atom.find(")")
            replacement_atom = atom
            #print(replacement_atom)
            contents = atom[l+1:r]
            if "," in contents:

                c_list = string.split(contents,",")
                #print(c_list)
                for c in c_list:
                    if (c in self.variables.keys() and self.variables[c] != None):
                        replacement_atom = string.replace(replacement_atom,str(c),str(self.variables[c]))
                        #print(replacement_atom)
                new.append(replacement_atom)
            else:
                if contents in self.variables.keys() and self.variables[contents] != None:
                    if contents in atom:
                         new.append(string.replace(replacement_atom,str(contents),str(self.variables[contents])))
                elif contents in self.variables.keys() and self.variables[contents] == None:
                    new.append(replacement_atom)
                elif contents not in self.variables.keys():
                    new.append(replacement_atom)
        self.LHS = new

    def forwardChain(self, facts):
        if(self.verifyAtom(0,facts) == True):

            content = None;
            for var in self.variables:
                if (var in self.RHS):
                    self.RHS = string.replace(self.RHS,str(var),str(self.variables[var]))


            r_i = self.RHS.find("(") + 1
            l_i = self.RHS.find(")")
            f = Fact(self.RHS,self.RHS_predicate,self.RHS[r_i:l_i])
            facts.append(f)
            #print(self.variables)
            for v in self.variables:
                self.variables[v] = None;
            print("FIRING RULE:     "+self.RHS+"    INFERRED")
            # print("UPDATED KB\n")
            #
            # for b in facts:
            #     print(b.factStr)
            # print("\n")
            return f
        # else:
        #     print("No inference found")

        return None;




class Proof:
    def __init__(self):
        print("hi")
