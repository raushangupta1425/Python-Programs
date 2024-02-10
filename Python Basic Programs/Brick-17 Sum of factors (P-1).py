#Find sum of factors of number.
n=int(input("Enter a nunber :"))
sum=0
i=1
while(i<=n):
    if(n%i==0):
        sum= sum+i
    i=i+1
print("The result is :",sum)
