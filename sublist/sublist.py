SUBLIST = "Sublist"
SUPERLIST = "Super list"
EQUAL = "Equal"
UNEQUAL = "Unequal"


def combinations(list, n):
    return [list[i:i+n] for i in range(len(list)-n + 1)]


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif list_one in combinations(list_two, len(list_one)):
        return SUBLIST
    elif list_two in combinations(list_one, len(list_two)):
        return SUPERLIST

    return UNEQUAL
