import heapq
import collections
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

#Solution with Dequeue in O(n)
def maxSlidingWindowDequeue(nums, k):
    maximumwindow=[]
    q=collections.deque()
    left=0
    right=0
    while(right<len(nums)):
        while(q and nums[q[-1]]<nums[right]):
            q.pop()
        q.append(right)
        if(q[0]<left):
            q.popleft()
        if((right-left+1)>=k):
            maximumwindow.append(nums[q[0]])
            left+=1           
        right+=1
    return maximumwindow

print(maxSlidingWindowDequeue([1,3,-1,-3,5,3,6,7],3))