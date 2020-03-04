def find_anagrams(word, candidates):
    return [x for x in candidates if (sorted(word.lower()) == sorted(x.lower())) and (word.lower() != x.lower())]
