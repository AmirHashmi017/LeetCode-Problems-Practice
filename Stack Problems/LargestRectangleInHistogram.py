def largestRectangleArea(heights):
    stack=[]
    maxarea=0
    for i in range(len(heights)):
        width=0
        while(stack and heights[i]<stack[-1][0]):
            height,index=stack[-1]
            width=(i-index)
            maxarea=max(maxarea,height*width)
            stack.pop()
        
        stack.append((heights[i],i-width))
    
    while(stack):
        height,width=stack[-1]
        area=height*(len(heights)-width)
        maxarea=max(maxarea,area)
        stack.pop()
    
    return maxarea

print(largestRectangleArea([2,1,5,6,2,3]))