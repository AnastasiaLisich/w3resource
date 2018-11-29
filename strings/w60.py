string = 'Hello beautiful World'

# answer = 'HellO BeautifuL WorlD'


list_of_words = string.split()

string2 = ''

for word in list_of_words:
    string2 += word[0].upper() + word[1:-1] + word[-1].upper() + ' '

print(string2[:-1])

