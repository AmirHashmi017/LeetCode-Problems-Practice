def twoSum(nums, target):
    set={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if(complement in set):
            return [i,set[complement]]
        set[nums[i]]=i

nums=[2,7,11,15]
print(twoSum(nums,9))