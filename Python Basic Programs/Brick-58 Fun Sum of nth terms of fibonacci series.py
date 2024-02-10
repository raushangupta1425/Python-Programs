#(10*)Write a program to print sum of first nth terms of fibonacci series.

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    sum=1
    a=0
    b=1
    n=n-2
    while n!=0:
        c=a+b
        sum=sum+c
        a=b
        b=c
        n=n-1
    return sum
print("**Print sum of forst nth terms of fibonacci series.**")
n=int(input("Enter a number: "))
x=fibonacci(n)
print(x)
