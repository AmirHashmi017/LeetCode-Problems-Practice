def largestRectangleArea(heights):
    stack=[]
    count=1
    minheight=heights[0]
    left=0
    right=0
    while(right<len(heights) and left<len(heights)):
        print(stack)
        if(count==1):
            stack.append(heights[right]*count)
            print(stack)
            count+=1
            right+=1
        else:
            print(minheight)
            minheight=min(minheight,heights[right])
            print(minheight)
            area=(minheight*count)
            print(count)
            print(area)
            if(area>stack[-1]):
                stack.append(area)
                right+=1
                count+=1
            else:
                count=1
                left+=1
                right=left
                minheight=heights[right]
        if(right==len(heights) and left<len(heights)-1):
            count=1
            left+=1
            right=left
            minheight=heights[right]
    return max(stack)

print(largestRectangleArea([1,1]))