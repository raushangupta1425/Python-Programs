#(7*) Write a program to find a year is leap year on not using function.

def leap(n):
    if n%400==0:
        return "Leap Year"
    elif n%4==0 and n%100!=0:
        return "Leap Year"
    else:
        return "Not a leap year"
n=int(input("Enter a year: "))
x=leap(n)
print(x)
