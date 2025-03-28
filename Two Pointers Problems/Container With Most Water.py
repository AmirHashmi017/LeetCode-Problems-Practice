def maxArea(height):
    maxarea=0
    left=0
    right=len(height)-1
    while(left<right):
        area=min(height[left],height[right])*(right-left)
        maxarea=max(area,maxarea)
        if(height[left]<=height[right]):
            left+=1
        else:
            right-=1
    return maxarea

height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))