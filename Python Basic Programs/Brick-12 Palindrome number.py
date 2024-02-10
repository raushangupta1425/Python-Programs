#Find a number is Palindrome number or not.
n=int(input("Enter a number :"))
a=n
temp=0
while(n!=0):
    b=n%10
    temp=(temp*10)+b
    n=n//10
if(temp==a):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
