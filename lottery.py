"""A simple lottery to demonstrate module and script interaction in Python."""

import random

PEOPLE = ('Dale', 'Will')

def winner(people=PEOPLE):
    """Choose a winner at random from the given list of people."""
    x = random.randrange(0,len(people))
    return people[x]

# The if statement below is only true if we are calling this file as a script.
if __name__ == '__main__':
    print '... and the winner is!'
    your_input = raw_input()
    print winner(PEOPLE)
