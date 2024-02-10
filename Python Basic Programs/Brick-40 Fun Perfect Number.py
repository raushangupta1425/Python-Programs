#(5*) Write a program to find a number is perfect number or not using function.

def perfect(n):
    sum=0
    i=1
    while i<=n//2:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        return "Perfect Number"
    else:
        return "Not a Perfect Number"
n=int(input("Enter a number: "))
x=perfect(n)
print(x)
