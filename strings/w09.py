

str1 = 'Abracadabra'
index = 3

str2 = ''
for i in range(len(str1)):
    if i == index:
        continue
    else:
        str2 += str1[i]


# for i, letter in enumerate(str1):
#     if i != index:
#         str2 += letter


print(str2)
print(str1[:index] + str1[index + 1:])
