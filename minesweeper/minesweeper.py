def annotate(minefield):
    if len(set(''.join(minefield))) > 2 or len(set(map(lambda x: len(x), minefield))) > 1:
        raise ValueError("Wrong input")

    return [''.join([
            " " if count(minefield, x, y) == 0 else str(count(minefield, x, y)) if char == " " else char
            for y, char in enumerate(row)])
            for x, row in enumerate(minefield)]


def count(minefield, x, y):
    return sum([int(minefield[x + i][y + j] == "*")
                for i in range(-1, 2)
                for j in range(-1, 2)
                if (0 <= x + i < len(minefield)) and (0 <= y + j < len(minefield[0]))])
