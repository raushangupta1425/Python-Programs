#Write a program to find sum of all Armstrong Numbers between two numbers.

def armstrong(n):
    a=n
    count=0
    while n!=0:
        n=n//10
        count=count+1
    n=a
    sum=0
    while n!=0:
        b=n%10
        sum=sum+(b**count)
        n=n//10
    if sum==a:
        return True
    return False
print("**Find sum of all Armstrong Numbers between two numbers.**")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=0
for i in range(a,b+1):
    x=armstrong(i)
    if x==True:
        sum=sum+i
print("Sum is:",sum)
