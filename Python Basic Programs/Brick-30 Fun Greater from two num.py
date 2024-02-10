#(1*)Write a program to find greatest value from two number using function.

def greater(a,b):
    if a>b:
        return "first is greater"
    elif a==b:
        return "Both are equal"
    else:
        return "second is greater"
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
x=greater(a,b)
print(x)
        
