from collections import Counter


YACHT = lambda c: 50 if len(c) is 1 else 0
ONES = lambda c: c[1] * 1
TWOS = lambda c: c[2] * 2
THREES = lambda c: c[3] * 3
FOURS = lambda c: c[4] * 4
FIVES = lambda c: c[5] * 5
SIXES = lambda c: c[6] * 6
FULL_HOUSE = lambda c: sum(list(c.elements())) if repeat(c) is 3 else 0
FOUR_OF_A_KIND = lambda c: number(c) * 4 if repeat(c) >= 4 else 0
LITTLE_STRAIGHT = lambda c: 30 if sorted(list(c.elements())) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda c: 30 if sorted(list(c.elements())) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda c: sum(list(c.elements()))

number = lambda c: c.most_common(1)[0][0]
repeat = lambda c: c.most_common(1)[0][1]

def score(dice, category):
    return category(Counter(dice))
