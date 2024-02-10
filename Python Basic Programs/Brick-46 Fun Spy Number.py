#(5*) Write a program to find a number is Spy Number or not using function.

def spy(n):
    sum=0
    prod=1
    while n!=0:
        b=n%10
        sum=sum+b
        prod=prod*b
        n=n//10
    if sum==prod:
        return "Spy Number"
    return "Not a Spy Number"
print("**Find a number is Spy Number or not.**")
n=int(input("Enter a number: "))
x=spy(n)
print(x)
