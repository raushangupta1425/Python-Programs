#How to find a year is a leap year or not.
n=int(input("Enter a year :"))
if(n%400==0):
    print("Leap Year")
elif(n%4==0 and n%100!=0):
    print("Leap Year")
else:
    print("Not a leap year.")
