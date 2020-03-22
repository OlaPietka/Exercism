import rstr
import random


class Robot:
    regex = r'^[A-Z]{2}\d{3}$'

    def __init__(self):
        self.name = self.random_name()

    def reset(self):
        self.name = self.random_name()

    def random_name(self):
        random.seed()
        return rstr.xeger(self.regex)
