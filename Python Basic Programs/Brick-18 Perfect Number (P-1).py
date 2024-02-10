#Find a number is a perfect number or not.
n=int(input("Enter a number :"))
sum=0
for i in range(1,n//2+1,1):
    if(n%i==0):
        sum = sum+i
if(sum==n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
