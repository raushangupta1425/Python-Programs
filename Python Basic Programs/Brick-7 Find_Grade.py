#Find grade of percentage.
n=int(input("Enter a number : "))
if(n>=91 and n<=100):
    print("Grade : A+")
elif(n>=81 and n<=90):
    print("Grade : A")
elif(n>=71 and n<=80):
    print("Grade : B+")
elif(n>=61 and n<=70):
    print("Grade : B")
elif(n>=33 and n<=60):
    print("Grade : C")
else:
    print("Fail")
