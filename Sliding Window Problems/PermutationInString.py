def checkInclusion(s1, s2):
    hashtable1={}
    for i in range(len(s1)):
        index=ord(s1[i])-ord('a')
        if index not in hashtable1:
            hashtable1[index]=0
        hashtable1[index]+=1
    
    left=0
    right=0
    maxwindowsize=len(s1)
    windowsize=0
    hashtable2={}
    print(hashtable1)
    while(right<len(s2)):
        if(windowsize>=maxwindowsize):
            print(hashtable2)
            if(hashtable1==hashtable2):
                return True
            else:
                windowsize=0
                hashtable2.clear()
                print(hashtable2)
                left+=1
                right=left
        print(right)
        index=ord(s2[right])-ord('a')
        if index not in hashtable2:
            hashtable2[index]=0
        hashtable2[index]+=1
        windowsize+=1
        right+=1
    if(hashtable1==hashtable2):
        return True
    return False

print(checkInclusion("adc","dcda"))