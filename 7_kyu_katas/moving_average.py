"""
Kata description:

Background
Moving average of a set of values and a window size is a series of local averages.

Example:

Values: [1, 2, 3, 4, 5]
Window size: 3

Moving average is calculated as:


 1, 2, 3, 4, 5
 |     |
 ^^^^^^^
 (1+2+3)/3 = 2


  1, 2, 3, 4, 5
     |     |
     ^^^^^^^
     (2+3+4)/3 = 3


  1, 2, 3, 4, 5
        |     |
        ^^^^^^^
        (3+4+5)/3 = 4

Here, the moving average would be [2, 3, 4]
Task
Given a list values of integers and an integer n representing size of the window, calculate and return the moving
average.

When integer n is equal to zero or the size of values list is less than window's size, return None
"""


def moving_average(values, n):
    if n == 0:
        return None

    averages = []

    for i in range(len(values)):
        if i + n > len(values):
            break
        averages.append(sum(values[i:i + n]) // n)

    return averages if averages else None


print(moving_average([1, 2, 3, 4, 5], 3))
