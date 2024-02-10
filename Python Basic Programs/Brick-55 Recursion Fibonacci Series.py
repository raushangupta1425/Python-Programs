#Write a program to print n times of Fibonacci series using recursion.

def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print("**Print n times of Fibonacci Series.**")
n=int(input("Enter a number: "))
for i in range(0,n):
    x=fibonacci(i)
    print(x)
