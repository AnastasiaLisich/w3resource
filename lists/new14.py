#Write a Python program to print the numbers of a specified list after removing even numbers from it

l = [11, 2, 13, 4, 15, 6, 17, 9, 101, 112, 123]

l1 = [elem for elem in l if elem % 2 == 1]

print(l1)



