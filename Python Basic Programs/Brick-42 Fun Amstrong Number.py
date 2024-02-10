#(10*) Write a program to find a number is Amstrong Number of not using function.

def amstrong(n):
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
        return "Amstrong Number"
    else:
        return "Not a Amstrong Number"
n=int(input("Enter a number: "))
x=amstrong(n)
print(x)
