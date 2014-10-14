#!/usr/bin/env python
#
import sys
from random import randint

def main():
    action = str(sys.argv[1].lower())
    if action not in ['card', 'qcard']:
        print "Invalid input: \"card [int]\" or \"qcard\" only please"
        sys.exit(1)

    if action == 'qcard':
        with open('q.db', 'r') as f:
            data = [x.rstrip() for x in f.readlines()]
            card = spinner(len(data))

            print data[card]

    elif action == 'card':
        try:
            num_cards = int(sys.argv[2])
            if num_cards > 5:
                print "5 cards or less dipshit"
                sys.exit(1)
        except ValueError:
            num_cards = 1
        except IndexError:
            num_cards = 1

        # get the next argument for the number of cards
        with open('a.db', 'r') as f:
            data = [x.rstrip() for x in f.readlines()]

        already_used = []
        done = False
        for x in xrange(1, num_cards+1):
            card = spinner(len(data))
            if card in already_used:
                while not done:
                    card = spinner(len(data))
                    if card not in already_used:
                        done = True
            done = False
            already_used.append(card)
            print data[card]            

def spinner(length):
    card = randint(0, length)
    return card

main()
