
# Write a Python program to generate all sublists of a list.

x = ['A', 'B', 'C', 'D', 'E']


# len(x) -> 5
# range(5) -> [0, 1, 2, 3, 4]

length = len(x)

for i in range(length):
    for j in range(i, length):
        sublist = x[i:j+1]
        print(sublist)


# ABCDE
# =====
# A
# AB
# ABC
# ABCD
# ABCDE
# B
# BC
# BCD
# BCDE
# C
# CD
# CDE
# D
# DE
# E




A : 2
B : 3
C : 1
D : 1
E : 1






