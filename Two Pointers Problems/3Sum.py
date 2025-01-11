def threeSum(nums):
    output=[]
    nums.sort()
    for i in range(len(nums)):
        if(nums[i]>0):
            break
        if(i>0 and nums[i]==nums[i-1]):
            continue
        left=i+1
        right=len(nums)-1
        while(left<right):
            threesum=nums[i]+nums[left]+nums[right]
            if(threesum<0):
                left+=1
            elif(threesum>0):
                right-=1
            else:
                output.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return output

nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))