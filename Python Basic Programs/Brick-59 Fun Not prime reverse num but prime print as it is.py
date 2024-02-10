"""(DOC STRING:) WAP to take a number as inpit and find sum of its digit, if
the sum of digit is not a prime, print its reverse but if it is prime number
then print as it is."""

def prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True
def sumofdigit(n):
    sum=0
    while n!=0:
        b=n%10
        sum=sum+b
        n=n//10
    return sum
def reverse(n):
    sum=0
    while n!=0:
        b=n%10
        sum=sum*10+b
        n=n//10
    return sum
print("**Sum of digits of a number is not prime then reverse it but prime then print as it is.**")
n=int(input("Enter a number: "))
total=sumofdigit(n)
x=prime(total)
if x==True:
    print(total)
else:
    y=reverse(total)
    print(y)
