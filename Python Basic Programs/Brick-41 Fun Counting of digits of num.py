#(1*) Write a program to count digits of a number using function.

def counter(n):
    count=0
    while n!=0:
        n=n//10
        count=count+1
    return count
n=int(input("Enter a number: "))
x=counter(n)
print(x)
