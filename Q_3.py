# 3.  Write a Python program to create a list of tuples with the first element as the 
#     number and Second element as the square of the number.

my_list = [3, 9, 10, 13, 17, 19, 22, 23]
new_list = []

for i in my_list:
    t = (i, i*i)
    new_list.append(t)

print(new_list)
