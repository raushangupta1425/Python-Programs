#(10*) Write a program to find a number is Prime Number or not using function.

def prime(n):
    if n<=1:
        return "Not a Prime Number"
    for i in range(2,n//2+1):
        if n%i==0:
            return "Not a Prime Number"
    return "Prime Number"
print("**Find a number is Prime number of not.**")
n=int(input("Enter a number: "))
x=prime(n)
print(x)
