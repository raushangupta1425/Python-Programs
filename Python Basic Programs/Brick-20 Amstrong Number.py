#Find a number is a amstrong number or not.
n=int(input("Enter a number :"))
a=n
count=0
while(n!=0):
    n=n//10
    count +=1
n=a
sum=0
while(n!=0):
    b=n%10
    sum += b**count
    n=n//10
if(sum==a):
    print("Amstrong Number")
else:
    print("Not a Amstrong Number")
