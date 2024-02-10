#(10*) Write a program to print fabonacci series of n terms using function.

def fibonacci(n):
    if n==1 or n==0:
        print(0)
    elif n==2:
        print(0)
        print(1)
    else:
        print(0)
        print(1)
        n=n-2
        a=0
        b=1
        while(n!=0):
            c=a+b
            print(c)
            a=b
            b=c
            n=n-1
print("**Print fabonacci series of n terms.**")
n=int(input("Enter a number: "))
fibonacci(n)
