"""
Kata description:

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace
at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""
from prompt_toolkit.key_binding.bindings.scroll import scroll_one_line_up


def solution(string, markers):
    lines = string.split('\n')
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    return '\n'.join(lines)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
