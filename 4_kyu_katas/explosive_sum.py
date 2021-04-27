"""
Kata description:

How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of
writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the
same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct
ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples
Basic
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42
Explosive
exp_sum(50) # 204226
exp_sum(80) # 15796476
exp_sum(100) # 190569292
"""


def exp_sum(n):
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(1, n ):
        for j in range(i , n + 1):
            table[j] +=  table[j - i]
    return table[n] + 1


if __name__ == "__main__":
    print(exp_sum(80))
    print(exp_sum(100))
    print(exp_sum(50))