# 5.  Write a python program to print following pattern.
#     ABCDEFGHIJK  
#      ABCDEFGHI     
#       ABCDEFG       
#        ABCDE          
#         ABC             
#          A

string = "ABCDEFGHIJK"
space = " "

length = len(string)

i = 11
j = 11

while(j>=0):
    print((space*(11-i)) + string[0:j] + (space*(11-i)))
    i = i - 1
    j = j - 2
    