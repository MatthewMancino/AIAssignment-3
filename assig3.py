import sys
import string
import bisect

import re
from FOLlib import Fact, Rule, Proof

def main():
  #print(sys.argv[1])
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
            print("Rule Found "+v)
            if (v.find("^") != -1):
                hold = string.split(v," ^ ")
                hold.append(string.split(hold[len(hold) - 1], " -> ")[1])
                print(hold)
        elif (v.find("PROVE") != -1):
            print("Proof found "+v)
        else:
            print("Fact found "+v+"\n")
            hold = string.split(v,'(')
            hold[1] = string.split(hold[1],')')[0]
            facts.append(Fact(hold[0],hold[1]))

    for x in facts:
        print(x.name)

    for y in rules:
        y.forwardChain(facts)


if __name__=='__main__':main()
