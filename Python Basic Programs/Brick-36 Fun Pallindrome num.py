#(10*) Write a program to find a number is pallindrome number of not using function.

def pallindrome(n):
    a=n
    temp=0
    while n!=0:
        b=n%10
        temp=temp*10+b
        n=n//10
    if temp==a:
        return "Pallindrome"
    else:
        return "Not a Pallindrome"
n=int(input("Enter a number: "))
x=pallindrome(n)
print(x)
