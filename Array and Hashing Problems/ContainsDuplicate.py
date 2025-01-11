def containsDuplicate(nums):
    visited={}
    for i in range(len(nums)):
        if(nums[i] not in visited):
           visited[nums[i]]=nums[i]
        else:
           return True
    return False

nums=[1,2,3,1]
print(containsDuplicate(nums))