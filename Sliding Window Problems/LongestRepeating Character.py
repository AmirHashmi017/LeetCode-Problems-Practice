def characterReplacement( s, k):    
    left=0
    right=1
    maxlength=0
    while(right<len(s)):
        shifted=0
        length=1
        print(s[left], s[right])
        if(s[left]==s[right]):
            print(s[left], s[right])
            length+=1
            print(length)
        elif(shifted<k):
            print(s[left], s[right])
            length+=1
            shifted+=1
            print(length)
        elif(shifted>=k):
            print(s[left], s[right])
            print("Yes")
            left=right
            maxlength=max(maxlength,length)
            length=1
            shifted=0
        right+=1
    maxlength=max(maxlength,length)
    return maxlength
    

print(characterReplacement("ABAB",2))