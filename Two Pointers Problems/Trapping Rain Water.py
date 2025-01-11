def trap(height):
    if(not height):
        return 0
    left=0
    right=len(height)-1
    maxleft=height[left]
    maxright=height[right]
    trappingwater=0
    while(left<right):
        if(maxleft<=maxright):
            left+=1
            water=maxleft-height[left]
            if(water>0):
                trappingwater+=water
            maxleft=max(maxleft,height[left])
        else:
            right-=1
            water=maxright-height[right]
            if(water>0):
                trappingwater+=water
            maxright=max(maxright,height[right])
    return trappingwater

height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))