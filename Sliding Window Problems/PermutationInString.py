def checkInclusion(s1, s2):
    hashtable1=[0]*26
    hashtable2=[0]*26
    if(len(s1)>len(s2)):
        return False
    for i in range(len(s1)):
        index1=ord(s1[i])-ord('a')
        index2=ord(s2[i])-ord('a')
        hashtable1[index1]+=1
        hashtable2[index2]+=1
    if(hashtable1==hashtable2):
        return True
    for right in range(len(s2)-len(s1)):
        index=ord(s2[right])-ord('a')
        hashtable2[index]-=1
        hashtable2[ord(s2[right+len(s1)])-ord('a')]+=1
        if(hashtable1==hashtable2):
            return True
    return False

print(checkInclusion("adc","dcda"))