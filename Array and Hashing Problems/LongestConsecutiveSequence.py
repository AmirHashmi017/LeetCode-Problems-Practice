def longestConsecutive(nums):
    unique=set(nums)
    longest=0
    for num in unique:
        if(num-1) not in unique:
            length=1
            while(num+length) in unique:
                length+=1
            longest=max(longest,length)
    
    return longest

nums=[100,4,200,1,3,2]
print(longestConsecutive(nums))