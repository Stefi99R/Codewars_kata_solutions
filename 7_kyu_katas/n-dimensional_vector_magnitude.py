"""
Kata description:

Return the magnitude of a vector, given as an array of its component values.

The vector (2, 3, 5) would be represented as an array containing three values at indices 0, 1 and 2 respectively.
The array will always contain at least 2 and at most 100 elements (2 ≤ vector.Length ≤ 100), each of which will be
within the range [-100, 100].
An array containing four elements represents a vector in 4D space.

More info on finding the length of a vector: http://farside.ph.utexas.edu/teaching/301/lectures/node28.html
"""


def magnitude(vector):
    return (sum([i ** 2 for i in vector])) ** 0.5


if __name__ == "__main__":
    print(magnitude([0, 0]))
    print(magnitude([2 / 3.0, 1 / 3.0, 2 / 3.0]))
    print(magnitude([-2, -4, 4]))
