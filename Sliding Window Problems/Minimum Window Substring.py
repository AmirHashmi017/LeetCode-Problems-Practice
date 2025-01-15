def minWindow(s, t):
    hashtable1={}
    if(len(s)<len(t)):
        return ""
    for i in range(len(t)):
        if(t[i] not in hashtable1):
            hashtable1[t[i]]=0
        hashtable1[t[i]]+=1
    hashtable2={}
    minoutput=""
    output=""
    left=0
    right=0
    while left<len(s) and right<len(s):
        print(left)
        print(right)
        print(s[right])
        if(s[right] in hashtable1):
            if(s[right] not in hashtable2):
                hashtable2[s[right]]=0
            if(hashtable2[s[right]]<hashtable1[s[right]]):
                hashtable2[s[right]]+=1
        output+=s[right]
        print(hashtable2)
        right+=1
        if(hashtable1==hashtable2):
            print(hashtable1)
            print(hashtable2)
            print(output)
            if(len(minoutput)==0 or len(output)<len(minoutput)):
                minoutput=output
                print(minoutput)
                output=""
                hashtable2.clear()
                print(hashtable2)
                left+=1
                right=left
        if (right==len(s) and left<=len(s)-1):
            output=""
            hashtable2.clear()
            left+=1
            right=left   
    if(hashtable1==hashtable2):
        if(len(minoutput)==0 or len(output)<len(minoutput)):
            minoutput=output         
                
    return minoutput

print(minWindow("aaaaaaaaaaaabbbbbcdd","abcdd"))
