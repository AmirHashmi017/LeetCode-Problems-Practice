def minWindow(s, t):
    hashtable1={}
    if(len(s)<len(t)):
        return ""
    for i in range(len(t)):
        if(t[i] not in hashtable1):
            hashtable1[t[i]]=0
        hashtable1[t[i]]+=1
    need=len(set(t))
    have=0
    hashtable2={}
    minleft = -1
    minright = -1
    minlength=float('inf')
    minoutput=""
    output=""
    left=0
    for right in range(len(s)):
        if(s[right] not in hashtable2):
            hashtable2[s[right]]=0
        hashtable2[s[right]]+=1
        if(s[right] in hashtable1 and hashtable2[s[right]]==hashtable1[s[right]]):
            have+=1
        while(have==need):
            if((right-left)+1<minlength):
                minleft=left
                minright=right
                minlength=(right-left)+1
            hashtable2[s[left]]-=1
            if(s[left] in hashtable1 and hashtable2[s[left]]<hashtable1[s[left]]):
                have-=1
            left+=1
        
    if(minleft==-1 and minright==-1):
        return ""
    return s[minleft:minright+1]

print(minWindow("aaaaaaaaaaaabbbbbcdd","abcdd"))
