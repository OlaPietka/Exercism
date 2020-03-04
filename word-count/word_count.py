import re
from collections import Counter

RE = "(?:[0-9]+|[a-z]+(?:'[a-z])?)"


def count_words(sentence):
    return Counter(re.findall(RE, sentence.lower()))