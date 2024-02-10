#(10*)Write a program to print n terms number of fibonacci series.

def fibonacci(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    a=0
    b=1
    count=2
    while 1:
        c=a+b
        count=count+1
        if count==n:
            return c
        a=b
        b=c
print("**Find nth terms number of fibonacci series.**")
n=int(input("Enter a number: "))
x=fibonacci(n)
print(x)
