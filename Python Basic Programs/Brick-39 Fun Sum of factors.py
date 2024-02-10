#(5*) Write a program to find sum of factors of a number using function.

def sumOfFactors(n):
    sum=0
    i=1
    while i<=n:
        if n%i==0:
            sum=sum+i
        i=i+1
    return sum
n=int(input("Enter a number: "))
x=sumOfFactors(n)
print(x)
