def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]==target-nums[i]:
                return [i,j]
nums=eval(input())
target=int(input())
x=twoSum(nums,target)
print(x)
