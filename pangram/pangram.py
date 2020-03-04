from collections import Counter
import re

def is_pangram(sentence):
    return len(Counter(re.sub('[^a-z]+', '', sentence.lower()))) >= 26