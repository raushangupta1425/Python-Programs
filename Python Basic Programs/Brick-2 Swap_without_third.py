#How to swap two numbers without using third variable.
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
a=a+b
b=a-b
a=a-b
print("The value of first number is : ",a)
print("The value of second number is : ",b)
