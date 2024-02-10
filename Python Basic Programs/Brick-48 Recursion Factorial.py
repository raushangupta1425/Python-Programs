# Write a program to find factorial of a number using recursion function.

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print("**Find factorial of a given number.**")
n=int(input("Enter a number: "))
x=factorial(n)
print(x)
