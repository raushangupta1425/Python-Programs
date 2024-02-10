#(3*) Write a program to find a number is Decerium Number or not using function.

def decerium(n):
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
        count=count-1
        n=n//10
    if sum==a:
        return "Decerium Number"
    else:
        return "Not a Decerium"
n=int(input("Enter a number: "))
x=decerium(n)
print(x)
