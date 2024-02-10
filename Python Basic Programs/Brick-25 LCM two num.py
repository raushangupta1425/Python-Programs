#Write a program to find LCM of two number.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    max=a
else:
    max=b
i=max
while 1:
    if max%a==0 and max%b==0:
        print(max)
        break
    max=max+i
    
