def dailyTemperatures(temperatures):
    stack=[]
    output=[0]*len(temperatures)
    for i in range(len(temperatures)):
        count=0
        while(stack and stack[-1][0]<temperatures[i]):
            value,index=stack.pop()
            output[index]=i-index
        stack.append((temperatures[i],i))
    return output

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
                

        
        