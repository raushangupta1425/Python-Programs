#Find factorial of a user input.

n=int(input("Enter a number :"))
fact=1
while(n!=0):
    fact =fact*n
    n=n-1
print("The factorial is :",fact)
