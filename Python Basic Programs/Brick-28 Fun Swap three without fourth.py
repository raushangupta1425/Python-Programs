#(3*)Write a program to swap three variable without using fourth variable with function.

def swap(a,b,c):
    a=a+b+c
    b=a-b-c
    c=a-b-c
    a=a-b-c
    print(a,b,c)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
swap(a,b,c)
