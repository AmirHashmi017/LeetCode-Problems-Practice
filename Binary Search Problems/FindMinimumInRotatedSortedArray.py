def findMin(nums):
    left=0
    right=len(nums)-1
    minimum=nums[0]
    while(left<=right):
        if(nums[left]<nums[right]):
            return min(minimum,nums[left])
        mid=(left+right)//2
        minimum=min(minimum,nums[mid])
        if(nums[mid]>=nums[left]):
            left=mid+1
        else:
            right=mid-1
    return minimum

print(findMin([2,3,4,5,1]))