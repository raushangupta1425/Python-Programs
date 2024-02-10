#Write a program to swap two number without using third variable with function.

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
swap(a,b)
