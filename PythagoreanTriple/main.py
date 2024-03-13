"""
Write a function that prints the numbers from 1 to 100 that form the Pythagorean triple.
"""


def triple():
    pythagorean_triple = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pythagorean_triple.append((i, j, int(c)))

    return pythagorean_triple


for i in triple():
    print(i)