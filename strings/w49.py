# Write a Python program to count and display the vowels of a given text.

string = 'Magic winter forest'

vowels = 'aeiou'

amount_vowels = 0
all_vowels = []


for letter in string:
    if letter in vowels:
        amount_vowels += 1
        all_vowels.append(letter)


print(amount_vowels)
print(all_vowels)

print('-' * 80)

answer = [x for x in string if x in 'aeiou']
print(len(answer))
print(answer)
