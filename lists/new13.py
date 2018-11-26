#Write a Python program to generate a 3*4*6 3D array whose each element is *

from pprint import pprint

[
    [['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*']],
    [['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*']],
    [['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*'],['*', '*', '*', '*', '*', '*']],
]




outer = []
for _ in range(3):
    middle = []
    for _ in range(4):
        inner = []
        for _ in range(6):
            inner.append('*')
        middle.append(inner)
    outer.append(middle)

pprint(outer)

print('='*80)

outer = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
pprint(outer)
