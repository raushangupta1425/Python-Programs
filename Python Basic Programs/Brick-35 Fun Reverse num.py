#(7*) Write a program to reverse a number using function.

def reverse(n):
    temp=0
    while n!=0:
        b=n%10
        temp=temp*10+b
        n=n//10
    return temp
n=int(input("Enter a number: "))
x=reverse(n)
print(x)
