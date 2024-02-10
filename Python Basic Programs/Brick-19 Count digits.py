#Counting of digits in a number.
n=int(input("Enter a number :"))
count=0
while(n!=0):
    n=n//10
    count +=1
print("Counts of digit in this number :",count)
