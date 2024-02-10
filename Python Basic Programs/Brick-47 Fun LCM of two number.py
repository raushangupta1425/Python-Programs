#(10*) Write a program to find LCM of two number using function.

def lcm(a,b):
    if a>b:
        max=a
    else:
        max=b
    i=max
    while 1:
        if max%a==0 and max%b==0:
            return max
        max=max+i
print("**Find the LCM of given two nummber.**")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
x=lcm(a,b)
print(x)
