#Find a number is a Perfect Number or not.
n=int(input("Enter a number :"))
sum=0
i=1
while(i<=n//2):
    if(n%i==0):
        sum +=i
    i=i+1
if(n==sum):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
