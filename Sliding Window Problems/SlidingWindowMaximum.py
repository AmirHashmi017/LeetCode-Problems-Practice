import heapq
#Solution with Heapq in O(nlogn)
def maxSlidingWindowHeapq(nums, k):
    if(len(nums)==0):
        return []
    heap=[]
    maximumwindow=[]
    for i in range(0,k,1):
        heapq.heappush(heap,(-nums[i],i))
    maximumwindow.append(-heap[0][0])
    left=1
    for j in range(k,len(nums),1):
        heapq.heappush(heap,(-nums[j],j))
        while(heap[0][1]<left):
            heapq.heappop(heap)
        maximumwindow.append(-heap[0][0])
        left+=1
    return maximumwindow

print(maxSlidingWindowHeapq([1,3,-1,-3,5,3,6,7],3))
