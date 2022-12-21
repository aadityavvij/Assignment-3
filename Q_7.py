# 7.  Write a python program to print Fibonacci sequence also print average of the 
#     resultant Fibonacci series.

n = int(input("Enter number of terms of Fibonacci series to be printed\n"))


def fib(n):
    if(n<=0):
        print("Enter a positive number")

    elif(n==1):
        return 0

    elif(n==2):
        return 1

    else:
        return fib(n-1) + fib(n-2)


for i in range(1, n+1):
    print(fib(i))