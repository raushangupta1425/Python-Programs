#Write a program to find sum of all prime numbers between two given numbers using function.

def prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
print("**Find sum of all prime numbers between two numbers.**")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=0
for i in range(a,b+1):
    x=prime(i)
    if x==True:
        sum=sum+i
print("Sum is: ",sum)
