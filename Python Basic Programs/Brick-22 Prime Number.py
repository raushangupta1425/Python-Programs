#Write a program to find a number is prime number or not.

print("**Find a number is Prime number or not.**")
n=int(input("Enter a number: "))
if n<=1:
    print("Not prime")
else:
    flag=0
    for i in range(2,n//2+1,1):
        if n%i==0:
            print("Not prime")
            flag=1
            break
    if flag==0:
        print("Prime")
