#Reversing a number.
n=int(input("Enter a number :"))
temp=0
while(n!=0):
    b=n%10
    temp =(temp*10)+b
    n=n//10
print("Reverse is :",temp)
