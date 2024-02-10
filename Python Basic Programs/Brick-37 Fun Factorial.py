#(10*) Write a program to find factorial of a number using function.

def factorial(n):
    fact=1
    while n!=0:
        fact=fact*n
        n=n-1
    return fact
n=int(input("Enter a number: "))
x=factorial(n)
print(x)
