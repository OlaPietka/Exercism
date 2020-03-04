lyrics = ["a Partridge in a Pear Tree.",
         "two Turtle Doves",
         "three French Hens",
         "four Calling Birds",
         "five Gold Rings",
         "six Geese-a-Laying",
         "seven Swans-a-Swimming",
         "eight Maids-a-Milking",
         "nine Ladies Dancing",
         "ten Lords-a-Leaping",
         "eleven Pipers Piping",
         "twelve Drummers Drumming"]

days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']


def get_verse(n):
    verse = "On the {} day of Christmas my true love gave to me: ".format(days[n])

    if n is 0:
        verse += lyrics[0]
        return verse

    for i in range(n, 0, -1):
        verse += "{}, ".format(lyrics[i])
    verse += "and {}".format(lyrics[0])

    return verse


def recite(start_verse, end_verse):
    return [get_verse(n-1) for n in range(start_verse, end_verse+1)]
