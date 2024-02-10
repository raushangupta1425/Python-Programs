#Find greater number of three numbers.
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))
if(a>=b and a>=c):
    print("First number is greater.")
elif(b>=a and b>=c):
    print("Second number is greater.")
elif(c>=a and c>=b):
    print("Third number is greater.")
else:
    print("All are equal.")
