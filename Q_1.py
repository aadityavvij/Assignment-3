# 1.  Write a Python program to count the number of occurrences of each word or 
#     character in the string entered by the user. (Count the Number of Occurrences 
#     of each character only if the single word is entered by the user).

string = input("Enter string\n")

dict = {}

if(" " in string):
    a = string.split()
    for i in a:
        c = string.count(i)
        dict.update({i : c})
        
else:
    for i in string:
        c = string.count(i)
        dict.update({i : c})
    

print(dict)
