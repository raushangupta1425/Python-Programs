#(5*)Write a program to find greater number from three using function.

def greater(a,b,c):
    if a>=b and a>=c:
        return "first is greater"
    elif b>=a and b>=c:
        return "second is greater"
    else:
        return "third is greater"
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
x=greater(a,b,c)
print(x)
        
