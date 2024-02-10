#(10*)Write a program to find a number is part of the fabonacci series or not.

def fibonacci(n):
    if n==0 or n==1:
        return True
    a=0
    b=1
    while 1:
        c=a+b
        if c==n:
            return True
        elif c>n:
            return False
        a=b
        b=c
print("**Check wheather a number is part of Fibonacci series on not.**")
n=int(input("Enter a number: "))
x=fibonacci(n)
print(x)
