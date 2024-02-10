#(3*)Write a program to find a number is positive or negative with function.

def sign(n):
    if n>0:
        return "Positive"
    elif n==0:
        return "Zero"
    else:
        return "Negative"
n=int(input("Enter a number: "))
x=sign(n)
print(x)
