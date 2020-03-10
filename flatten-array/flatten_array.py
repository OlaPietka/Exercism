def flatten(iterable):
    li = []

    for i in iterable:
        if i is not None:
            if type(i) is not list:
                li.append(i)
            else:
                li.extend(flatten(i))
    return li
