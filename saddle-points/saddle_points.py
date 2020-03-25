def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Wrong shape")

    points = []
    for i, row in enumerate(matrix):
        for j, number in enumerate(row):
            if number == max(row) and number == min([row[j] for row in matrix]):
                points.append({"row": i + 1, "column": j + 1})

    return points
