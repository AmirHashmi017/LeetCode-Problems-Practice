def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slowindex=0
    fastindex=0
    
    for i in range(0,len(nums),1):
        index=abs(nums[i])-1
        if(nums[index]<0):
            return abs(nums[i])
        nums[index]*=-1 
    return -1