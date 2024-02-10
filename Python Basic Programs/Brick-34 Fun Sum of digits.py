#(10*) Write a program to find sum of digits of a number using function.

def sumofdigit(n):
    sum=0
    while n!=0:
        b=n%10
        sum=sum+b
        n=n//10
    return sum
n=int(input("Enter a number: "))
x=sumofdigit(n)
print(x)
        
