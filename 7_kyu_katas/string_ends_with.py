"""
Kata description:

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument
(also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(string, ending):
    return True if ending in string[(len(string)) - len(ending):] else False


print(solution('abc', 'bc'))
print(solution('abc', 'd'))
