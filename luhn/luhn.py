class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isnumeric():
            return False

        card_num = [int(x) for x in self.card_num]

        for i in range(len(card_num) - 2, -1, -2):
            n = card_num[i] * 2
            card_num[i] = n if n < 10 else n - 9

        return sum(card_num) % 10 == 0