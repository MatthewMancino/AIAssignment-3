import sys
import string
import bisect

import re
from FOLlib import Fact, Rule, Proof



def solve(facts,rules,goal):
    while goal not in facts:
        for y in rules:
            y.forwardChain(facts)

def main():

  facts = []
  rules = []
  string_data = []
  with open(sys.argv[1]) as F:
    data = F.read()
    #print(data)
    string_data = string.split(data,"\n")
    #print(len(string_data))
    for i,v in enumerate(string_data):
        hold = None;
        if (v.find("->") != -1):
            # print("Rule Found "+v)
            if (v.find("^") != -1):
                LHS = string.split(v," ^ ")
                hold = string.split(LHS[len(LHS) - 1], " -> ")
                LHS.insert(len(LHS)-1,hold.pop(0))
                LHS.pop()
                RHS = string.split(hold.pop(0),"\r")
                RHS = RHS.pop(0)
            else:
                LHS = string.split(v," -> ")
                RHS = string.split(LHS[len(LHS)-1],"\r")
                RHS = RHS.pop(0)
                LHS.pop(len(LHS) - 1)
            rules.append(Rule(v,LHS,RHS))
        elif (v.find("PROVE") != -1):
            # print("Proof found "+v)
            goal = string.split(v,"PROVE ").pop(1)
        else:
            # print("Fact found "+v)
            hold = string.split(v,'(')
            hold[1] = string.split(hold[1],')')[0]
            facts.append(Fact(v,hold[0],hold[1]))

    #PRINT INITIAL STATE
    print("FAKS")
    for b in facts:
        print(b.factStr)
    print("\nRULEZ")
    for c in rules:
        print(c.ruleStr)
    print("\nGOALS\n"+goal)


    solve(facts,rules,goal)

if __name__=='__main__':main()
