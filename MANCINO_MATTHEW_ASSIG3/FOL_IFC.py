import sys
import string
import bisect

import re
from copy import deepcopy
from FOLlib import Fact, Rule, Proof


def checkKB(goal,facts):
    #print("Checking Facts")
    for k in facts:
        if k.factStr == goal:
            return True;

def solve(facts,rules,goal):
    initial_rules = list()
    initial_rules = list(deepcopy(rules))
    #print(initial_rules)
    table = []
    iteration = 0
    while(True):
        print("\n\nIteration "+str(iteration))
        table.append([])
        if(iteration == 0):
            for y in rules:
                #print("Testing Rule"+y.ruleStr)
                newrule = y.forwardChain(facts)
                if(newrule != None):
                    table[iteration].append(newrule)
            #print("         Facts inferred on iteration" + str(iteration))
            for fi in table[iteration]:
                print(fi.factStr)
        else:
            for y in rules:                     #FOR EACH RULE
                for conj in y.LHS:              #For each conjunction
                    for t in table[iteration-1]:                 #[]
                        if (y.unification(conj,t) != None or y.unification(conj,t) != []):
                            #print("Testing Rule "+y.ruleStr)
                            newrule = y.forwardChain(facts)
                            break
                    break
                #print("Skipping Rule "+y.ruleStr)
                if(newrule != None):
                    table[iteration].append(newrule)
            #print("         Facts inferred on iteration" + str(iteration))
            for fi in table[iteration]:
                print(fi.factStr)



        rules = list(deepcopy(initial_rules))
        if checkKB(goal,facts):
            print("Proved")
            return
        if(table[iteration-1] == []):
            print(goal+"   Not Proved")
            return
        iteration += 1

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
    print("\nINITIAL FACTS")
    for b in facts:
        print(b.factStr)
        #print(b.constant)
    print("\nINITAL RULES")
    for c in rules:
        print(c.ruleStr)
    print("\nGOALS\n"+goal+"\n")


    solve(facts,rules,goal)

if __name__=='__main__':main()