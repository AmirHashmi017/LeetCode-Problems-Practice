def productExceptSelf(nums):
    output=[1]*len(nums)
    prefix=1
    for i in range(0,len(nums),1):
        output[i]=prefix
        prefix*=nums[i]
    
    postfix=1
    for i in range(len(nums)-1,-1,-1):
        output[i]*=postfix
        postfix*=nums[i]
    
    return output

nums=[1,2,3,4]
print(productExceptSelf(nums))