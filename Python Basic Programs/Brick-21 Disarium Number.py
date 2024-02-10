#Find a number is a disarium number or not.
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
    count -=1
if(sum==a):
    print("Disarium Number")
else:
    print("Not a Disarium Number")
