def characterReplacement( s, k):    
    hashmap={}
    left=0
    maxlength=0
    for right in range(len(s)):
        if(hashmap.get(s[right])!=None):
            hashmap[s[right]]=1+hashmap.get(s[right])
        else:
            hashmap[s[right]]=1
        while((right-left+1)-max(hashmap.values())>k):
            hashmap[s[left]]-=1
            left+=1
        maxlength=max(maxlength,right-left+1)
    return maxlength
    
s="KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
print(characterReplacement(s,4))