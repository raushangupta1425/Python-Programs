#How to swap three number without using fourth variable.
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print("The value of a is : ",a)
print("The value of b is : ",b)
print("The value of c is : ",c)
