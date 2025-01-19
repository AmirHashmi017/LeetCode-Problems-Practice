def dailyTemperatures(temperatures):
    output=[0]*len(temperatures)
    for i in range(len(temperatures)-2,-1,-1):
        count=0
        days=0
        j=i+1
        while(j<len(temperatures)):
            print(j)
            print(temperatures[j])
            if(temperatures[i]<temperatures[j]):
                print(temperatures[i])
                print(temperatures[j])
                print(count)
                days=count
                days+=1
                break
            elif(output[j]>0):
                print(output[j])
                count+=output[j]
                j+=output[j]
            else:
                break
            print(j)
        output[i]=days
    return output

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
                

        
        