# 2.  Write a python script to print next date of input date.

d = int(input("Day - "))
m = int(input("Month - "))
y = int(input("Year - "))

long = [1, 3, 5, 7, 8, 10, 12]
short = [4, 6, 9, 11]

if (d<1) | (y>2025) | (y<1800):
    print("Invalid Date!")

elif (m in long) & (d<31):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m in long) & (d==31) & (m!=12):
    print(f"Next date is: 01/{m+1}/{y}")

elif (m==12) & (d==31):
    print(f"Next date is: 01/01/{y+1}")

elif (m in short) & (d<30):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m in short) & (d==30):
    print(f"Next date is: 01/{m+1}/{y}")

elif (m==2) & (y%4==0) & (d<29):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m==2) & (y%4==0) & (d==29):
    print(f"Next date is: 01/{m+1}/{y}")

elif (m==2) & (y%4!=0) & (d<28):
    print(f"Next date is: {d+1}/{m}/{y}")

elif (m==2) & (y%4!=0) & (d==28):
    print(f"Next date is: 01/{m+1}/{y}")

else:
    print("Invalid Date!")