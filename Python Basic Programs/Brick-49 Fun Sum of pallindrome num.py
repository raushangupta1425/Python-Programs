# Write a program to find sum of all pallindrome numbers between given two numbers.

def pallindrome(n):
    a=n
    sum=0
    while n!=0:
        b=n%10
        sum=sum*10+b
        n=n//10
    if sum==a:
        return True
    return False
print("**Find sum of all pallindrome numbers between two numbers.**")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=0
for i in range(a,b+1):
    x=pallindrome(i)
    if x==True:
        sum=sum+i
print("Sum is: ",sum)
