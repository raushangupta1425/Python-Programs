#Check wheather a number is a strong number or not.
from math import factorial
n=int(input("Enter a number :"))
a=n
sum=0
while(n!=0):
    b=n%10
    sum=sum+factorial(b)
    n=n//10
if(sum==a):
    print("It is a Strong Number.")
else:
    print("Not a Stong Number.")
