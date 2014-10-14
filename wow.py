#!/usr/bin/env python
#
import re
import sys
from random import randint

def main():
    with open('q.db', 'r') as f:
        qdata = [x.rstrip() for x in f.readlines()]
        qcard = qdata[spinner(len(qdata))]
        done = False

        while not done:
            if numblanks(qcard) > 1:
                qcard = qdata[spinner(len(qdata))]
            else:
                done = True
                
    # get the next argument for the number of cards
    with open('a.db', 'r') as f:
        adata = [x.rstrip() for x in f.readlines()]
        acard = adata[spinner(len(adata))]

    # question, put answer at end
    if re.search('\?$', qcard) and not re.search('_____', qcard):   
        print "{0} {1}".format(qcard, acard)
    else:
        print qcard.replace('_____', acard)

def numblanks(q):
    return len(re.findall('_____', q))

def replaceblanks(qcard, acard):
    return message

def spinner(length):
    card = randint(0, length)
    return int(card)

main()
