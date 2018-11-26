#Write a Python program to generate all permutations of a list in Python.
string = input('Enter elements: ')

steps = [[]]
a, b = 0, 1
new = []
while b < len(string):
    if a >= 0:
        new.extend([(a, b)] + s for s in steps)
        a -= 1
    else:
        a, b = b, b + 1
        steps.extend(new)
        new = []

permutations = []
for step in steps:
    x = list(string)
    for i, j in step:
        x.insert(-j, x.pop(-i - 1))
    permutations.append(' '.join(x))

for p in permutations:
    print(p)
