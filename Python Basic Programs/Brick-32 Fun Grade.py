#(1*)Write a program to find grade from percentage using function.

def grade(n):
    if n>=91 and n<=100:
        return "A+"
    elif n>=81 and n<=90:
        return "A"
    elif n>=71 and n<=80:
        return "B+"
    elif n>=61 and n<=70:
        return "B"
    elif n>=33 and n<=60:
        return "pass"
    else:
        return "Fail"
n=int(input("Enter a number: "))
x=grade(n)
print(x)
