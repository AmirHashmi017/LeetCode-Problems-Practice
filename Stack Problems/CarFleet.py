def carFleet(target, position, speed):
    hashmap={}
    stack=[]
    for i in range(len(position)):
        hashmap[position[i]]=speed[i]
    sortedposition=sorted(position)
    for i in range(len(sortedposition)-1,-1,-1):
        time=float(target-sortedposition[i])/hashmap[sortedposition[i]]
        if(not stack or time>stack[-1]):
            stack.append(time)
    
    return len(stack)

print(carFleet(10,[6,8],[3,2]))