#Write a program to swap two number using third variable with function.

def swap(a,b):
    c=a
    a=b
    b=c
    print(a,b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
swap(a,b)
