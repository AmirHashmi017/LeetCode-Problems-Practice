def topKFrequent(nums, k):
    count={}
    buckets=[[]for i in range(len(nums)+1)]
    for num in nums:
        if(num not in count):
            count[num]=0
        count[num]+=1
    
    for num in set(nums):
        buckets[count[num]].append(num)
    
    output=[]
    for i in range(len(buckets)-1,-1,-1):
        for num in buckets[i]:
            if(len(output)==k):
                return output
            output.append(num)
    return output


nums=[1,1,1,2,2,3]
print(topKFrequent(nums,2))