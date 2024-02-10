#(3*) Write a program to find a number is Strong Number or not using function.

from math import factorial
def strong(n):
    a=n
    sum=0
    while n!=0:
        b=n%10
        sum=sum+factorial(b)
        n=n//10
    if sum==a:
        return "Strong Number"
    else:
        return "Not a Strong Number"
n=int(input("Enter a number: "))
x=strong(n)
print(x)
