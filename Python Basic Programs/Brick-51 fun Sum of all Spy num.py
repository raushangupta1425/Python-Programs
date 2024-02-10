#Write a program to find sum of all spy numbers between two numbers.

def spy(n):
    sum=0
    prod=1
    while n!=0:
        b=n%10
        sum=sum+b
        prod=prod*b
        n=n//10
    if sum==prod:
        return True
    return False
print("**Find sum of all spy numbers between two numbers.**")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=0
for i in range(a,b+1):
    x=spy(i)
    if x==True:
        sum=sum+i
print("Sum is: ",sum)
