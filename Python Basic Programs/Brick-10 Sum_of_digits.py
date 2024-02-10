#Find the sum of digits of a user input.
n=int(input("Enter a number : "))
a=n
sum=0
while(n!=0):
    t=n%10
    sum +=t
    n=n//10
print("The sum is :",sum)
    
