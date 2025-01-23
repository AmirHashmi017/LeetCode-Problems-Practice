import math
def minEatingSpeed(piles, h):
    start=1
    end=max(piles)
    res=end
    while start<=end:
        mid=(start+end)//2
        hoursrequired=0
        for i in range(len(piles)):
            hoursrequired += (piles[i] + mid - 1) // mid #Equal to ceil(piles[i]/mid)
        if(hoursrequired>h):
                start=mid+1
        elif(hoursrequired<=h):
            res=mid
            end=mid-1
    return res

print(minEatingSpeed([30,11,23,4,20],5))

