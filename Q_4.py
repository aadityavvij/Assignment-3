# 4.  Write a program to prompt the user for a grade between 4 and 10. If the grade 
#     is out of range print error message.

g = int(input("Enter Your Grade\n"))

if (g==10):
    print("Your Grade is 'A+' and Outstanding Performance")

elif (g==9):
    print("Your Grade is 'A' and Excellent Performance")

elif (g==8):
    print("Your Grade is 'B+' and Very Good Performance")

elif (g==7):
    print("Your Grade is 'B' and Good Performance")

elif (g==6):
    print("Your Grade is 'C+' and Average Performance")

elif (g==5):
    print("Your Grade is 'C' and Below Average Performance")

elif (g==4):
    print("Your Grade is 'D' and Poor Performance")

else:
    print("Error!")