def is_isogram(string):
    string = string.lower().replace(' ', '').replace('-', '')
    return len(set(string )) == len(list(string ))
