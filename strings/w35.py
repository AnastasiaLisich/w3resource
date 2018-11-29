# 35. Write a Python program to display a number with a comma separator.

task = 125456000
# answer = '1,250,348'

def separate_number(number):
    result = ''
    tick_tack = 0
    task2 = str(number)
    for digit in reversed(task2):
        result += digit
        tick_tack += 1
        if tick_tack % 3 == 0 and len(task2) > tick_tack:
            result += ','

    return ''.join(reversed(result))

print(separate_number(task))


def rev(s):
    return ''.join(reversed(s))

s = rev(str(task))
answer = rev(','.join(
    s[n:n+3] for n in range(0, len(s), 3)
))
print(answer)

# '{:,}'.format(3454456345622345).replace(',', ' ')
