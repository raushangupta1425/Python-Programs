def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]==target-nums[i]:
                return [i,j]
print("**WAP to find index value of those two number from list which sum is equal to target.**")
nums=eval(input("Enter list: "))
target=int(input("Enter target: "))
x=twoSum(nums,target)
print(x)